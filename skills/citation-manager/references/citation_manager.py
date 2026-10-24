"""
Citation Manager — Quản lý danh mục Tài liệu tham khảo (TLTK) chuẩn HVNH & đối chiếu
trích dẫn trong bản thảo với danh mục.

Quy trình:
  1. Khai báo nguồn trong file YAML (xem sources_template.yaml) — mỗi nguồn có
     type: book | article, language: vi | en, và các trường tương ứng.
  2. assign_numbers() đánh số theo đúng chuẩn HVNH: tách khối Tiếng Việt / Tiếng Anh,
     xếp ABC theo TÊN (VN) hoặc HỌ (nước ngoài), rồi đánh số liên tục xuyên hai khối
     (khối Tiếng Việt trước, khối Tiếng Anh sau — theo đúng thứ tự add_reference_section_hvnh
     trong academic-docx-writer/references/word_docx_recipes.py).
  3. render_reference_list() xuất danh mục TLTK dạng text đúng format HVNH.
  4. cross_check() đối chiếu số trích dẫn [n] xuất hiện trong bản thảo (.docx/.md/.txt)
     với danh mục: báo THIẾU (được trích nhưng không có trong danh mục) và MỒ CÔI
     (có trong danh mục nhưng chưa từng được trích).

Đây là công cụ dùng CÙNG với academic-docx-writer: sau khi có danh mục đã đánh số ở
đây, dùng hvnh_book()/hvnh_journal_article()/add_reference_section_hvnh() trong
word_docx_recipes.py để chèn vào file .docx thật — citation_manager.py không tự
sinh file .docx, chỉ quản lý dữ liệu nguồn + đối chiếu logic đánh số/trích dẫn.
"""
import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None

try:
    import docx
except ImportError:
    docx = None


# ==============================================================================
# NẠP DANH MỤC NGUỒN TỪ YAML
# ==============================================================================
def load_sources(yaml_path):
    """Đọc file YAML danh mục nguồn. Mỗi nguồn là 1 dict với tối thiểu:
    id (định danh nội bộ duy nhất), type ('book'|'article'), language ('vi'|'en'),
    author, year, title — và publisher/place (book) hoặc journal/volume/issue/pages (article).
    """
    if yaml is None:
        raise RuntimeError("Cần cài PyYAML để đọc file .yaml: pip install pyyaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    sources = data.get("sources", [])
    _validate_sources(sources)
    return sources


def _validate_sources(sources):
    seen_ids = set()
    for i, s in enumerate(sources):
        sid = s.get("id")
        if not sid:
            raise ValueError(f"Nguồn thứ {i + 1} thiếu trường 'id' bắt buộc.")
        if sid in seen_ids:
            raise ValueError(f"Trùng id nguồn: '{sid}' xuất hiện nhiều hơn 1 lần.")
        seen_ids.add(sid)
        if s.get("type") not in ("book", "article"):
            raise ValueError(f"Nguồn '{sid}': type phải là 'book' hoặc 'article', nhận '{s.get('type')}'.")
        if s.get("language") not in ("vi", "en"):
            raise ValueError(f"Nguồn '{sid}': language phải là 'vi' hoặc 'en', nhận '{s.get('language')}'.")
        for field in ("author", "year", "title"):
            if not s.get(field):
                raise ValueError(f"Nguồn '{sid}': thiếu trường bắt buộc '{field}'.")
        if s["type"] == "book":
            for field in ("publisher", "place"):
                if not s.get(field):
                    raise ValueError(f"Nguồn '{sid}' (type=book): thiếu trường bắt buộc '{field}'.")
        else:
            for field in ("journal", "volume", "issue", "pages"):
                if not s.get(field):
                    raise ValueError(f"Nguồn '{sid}' (type=article): thiếu trường bắt buộc '{field}'.")


# ==============================================================================
# SẮP XẾP & ĐÁNH SỐ THEO CHUẨN HVNH
# ==============================================================================
def _sort_key_vi(source):
    """VN xếp ABC theo TÊN (giữ nguyên trật tự thông thường, không đảo họ lên trước)."""
    author = source["author"].strip()
    given_name = author.split()[-1] if author.split() else author
    return given_name.upper()


def _sort_key_en(source):
    """Nước ngoài xếp ABC theo HỌ. Giả định author dạng 'Họ, Tên' hoặc 'Họ T.'
    (chuẩn trích dẫn quốc tế) — lấy token đầu tiên trước dấu phẩy hoặc cả chuỗi
    nếu không có dấu phẩy."""
    author = source["author"].strip()
    surname = author.split(",")[0].strip() if "," in author else author.split()[0]
    return surname.upper()


def sort_sources(sources):
    """Tách khối vi/en, mỗi khối xếp ABC riêng theo đúng quy tắc HVNH."""
    vi = sorted([s for s in sources if s["language"] == "vi"], key=_sort_key_vi)
    en = sorted([s for s in sources if s["language"] == "en"], key=_sort_key_en)
    return vi, en


def assign_numbers(sources):
    """Trả về dict {source_id: số thứ tự}, đánh số liên tục: khối Tiếng Việt trước
    (theo thứ tự đã sort), rồi khối Tiếng Anh (tiếp tục đánh số, không reset về 1)."""
    vi, en = sort_sources(sources)
    numbering = {}
    n = 0
    for s in vi + en:
        n += 1
        numbering[s["id"]] = n
    return numbering, vi, en


# ==============================================================================
# XUẤT DANH MỤC TLTK DẠNG TEXT (đúng format HVNH)
# ==============================================================================
def _format_entry(source, number):
    if source["type"] == "book":
        body = f"{source['author']} ({source['year']}), {source['title']}, {source['publisher']}, {source['place']}."
    else:
        page_prefix = "pp." if source["language"] == "en" else "tr."
        body = (
            f"{source['author']} ({source['year']}), “{source['title']}”, "
            f"{source['journal']}, {source['volume']}({source['issue']}), {page_prefix}{source['pages']}."
        )
    return f"{number}. {body}"


def render_reference_list(sources):
    """Trả về chuỗi text danh mục TLTK đầy đủ, tách khối Tiếng Việt / Tiếng Anh,
    đúng format và thứ tự chuẩn HVNH — dùng để rà tay hoặc dán tạm trước khi
    chuyển sang add_reference_section_hvnh() dựng bản .docx thật."""
    numbering, vi, en = assign_numbers(sources)
    lines = []
    if vi:
        lines.append("Tiếng Việt")
        for s in vi:
            lines.append(_format_entry(s, numbering[s["id"]]))
        lines.append("")
    if en:
        lines.append("Tiếng Anh")
        for s in en:
            lines.append(_format_entry(s, numbering[s["id"]]))
    return "\n".join(lines).strip()


# ==============================================================================
# TRÍCH XUẤT SỐ TRÍCH DẪN [n] TỪ BẢN THẢO
# ==============================================================================
_CITATION_RE = re.compile(r"\[(\d+)(?:\s*,\s*tr\.[^\]]+)?\]")


def extract_cited_numbers(text):
    """Trả về dict {số: số lần xuất hiện} cho mọi trích dẫn dạng [n] hoặc [n, tr.xxx]
    tìm thấy trong text. Nhiều số trong 1 câu như '[19], [25]' được tách riêng vì
    mỗi cặp ngoặc vuông là 1 match độc lập."""
    counts = {}
    for m in _CITATION_RE.finditer(text):
        n = int(m.group(1))
        counts[n] = counts.get(n, 0) + 1
    return counts


def load_manuscript_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".docx":
        if docx is None:
            raise RuntimeError("Cần cài python-docx để đọc file .docx: pip install python-docx")
        d = docx.Document(file_path)
        return "\n".join(p.text for p in d.paragraphs)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# ==============================================================================
# ĐỐI CHIẾU TRÍCH DẪN ↔ DANH MỤC
# ==============================================================================
def cross_check(sources, manuscript_text):
    """So khớp trích dẫn [n] trong bản thảo với danh mục nguồn đã đánh số.
    Trả về dict:
      missing  -> list số [n] xuất hiện trong bản thảo nhưng KHÔNG có trong danh mục
      orphan   -> list (số, source_id) có trong danh mục nhưng KHÔNG được trích lần nào
      cited_counts -> dict {số: số lần trích} để tiện rà soát nguồn trích quá nhiều/quá ít
    """
    numbering, vi, en = assign_numbers(sources)
    number_to_id = {v: k for k, v in numbering.items()}
    cited_counts = extract_cited_numbers(manuscript_text)

    missing = sorted(n for n in cited_counts if n not in number_to_id)
    orphan = sorted(
        (n, sid) for n, sid in number_to_id.items() if n not in cited_counts
    )

    return {
        "missing": missing,
        "orphan": orphan,
        "cited_counts": cited_counts,
        "numbering": numbering,
    }


def print_cross_check_report(result, sources):
    id_to_source = {s["id"]: s for s in sources}
    print("=== CITATION MANAGER: BÁO CÁO ĐỐI CHIẾU TRÍCH DẪN ===")
    print(f"Tổng số nguồn trong danh mục: {len(sources)}")
    print(f"Tổng số trích dẫn [n] khác nhau tìm thấy trong bản thảo: {len(result['cited_counts'])}")

    if result["missing"]:
        print(f"\n❌ THIẾU TRONG DANH MỤC ({len(result['missing'])}): được trích trong bài nhưng không có nguồn tương ứng")
        for n in result["missing"]:
            print(f"  - [{n}] được trích {result['cited_counts'][n]} lần, nhưng KHÔNG có trong danh mục nguồn.")
    else:
        print("\n✅ Không có trích dẫn nào bị thiếu nguồn trong danh mục.")

    if result["orphan"]:
        print(f"\n⚠️ MỒ CÔI TRONG DANH MỤC ({len(result['orphan'])}): có trong danh mục nhưng chưa từng được trích")
        for n, sid in result["orphan"]:
            s = id_to_source[sid]
            print(f"  - [{n}] {sid}: {s['author']} ({s['year']}) — chưa xuất hiện dạng [{n}] trong bản thảo.")
    else:
        print("\n✅ Mọi nguồn trong danh mục đều đã được trích dẫn ít nhất 1 lần.")

    return len(result["missing"]) == 0 and len(result["orphan"]) == 0


# ==============================================================================
# CLI
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="Quản lý danh mục TLTK chuẩn HVNH & đối chiếu trích dẫn với bản thảo.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="In danh mục TLTK đã đánh số theo chuẩn HVNH")
    p_list.add_argument("sources_yaml")

    p_check = sub.add_parser("check", help="Đối chiếu trích dẫn [n] trong bản thảo với danh mục nguồn")
    p_check.add_argument("sources_yaml")
    p_check.add_argument("manuscript")

    args = parser.parse_args()

    if not os.path.exists(args.sources_yaml):
        print(f"[ERROR] Không tìm thấy file danh mục: {args.sources_yaml}", file=sys.stderr)
        sys.exit(1)
    try:
        sources = load_sources(args.sources_yaml)
    except (ValueError, RuntimeError) as e:
        print(f"[ERROR] Danh mục nguồn không hợp lệ ({args.sources_yaml}): {e}", file=sys.stderr)
        sys.exit(1)

    if args.command == "list":
        print(render_reference_list(sources))
    elif args.command == "check":
        if not os.path.exists(args.manuscript):
            print(f"[ERROR] Không tìm thấy bản thảo: {args.manuscript}", file=sys.stderr)
            sys.exit(1)
        text = load_manuscript_text(args.manuscript)
        result = cross_check(sources, text)
        ok = print_cross_check_report(result, sources)
        sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()

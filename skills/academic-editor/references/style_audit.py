"""
Academic Editor — Bộ rà soát văn phong học thuật sau đại học (Style Audit)
Quét một bản thảo (.docx / .md / .txt) đã viết sẵn để phát hiện:
  1. Sáo ngữ / "AI smell" (theo bảng tra cứu academic_writing_mastery.md §3.1)
  2. Khẳng định tuyệt đối hóa thiếu cơ sở (Overclaim)
  3. Nguy cơ diễn đạt tương quan thành nhân quả (Correlation → Causation risk)

Đây là công cụ RÀ SOÁT (đọc lại bản thảo có sẵn), khác với academic-docx-writer /
academic-slide-writer (dùng để DỰNG tài liệu/slide mới từ đầu). Dùng cả ba cùng nhau:
soạn bằng 2 skill kia, rà lại bằng skill này trước khi nộp.

Giới hạn đã biết: đây là bộ lọc dựa trên từ khóa/regex, KHÔNG phải mô hình hiểu ngữ
nghĩa — có thể bỏ sót sáo ngữ diễn đạt theo cách khác, và có thể báo nhầm (false
positive) khi câu văn hợp lệ vô tình chứa cụm từ trong danh sách. Luôn đọc lại từng
điểm được báo trước khi sửa, không tự động thay thế hàng loạt.
"""
import argparse
import os
import re
import sys

try:
    import docx  # python-docx, chỉ cần khi đọc file .docx
except ImportError:
    docx = None

# ==============================================================================
# 1. BẢNG SÁO NGỮ / "AI SMELL" — nguồn: academic_writing_mastery.md §3.1
# ==============================================================================
CLICHE_PATTERNS = [
    (r"trong bối cảnh (hiện nay|hiện tại|ngày nay)", "Mở đầu sáo rỗng, không cung cấp thông tin",
     'Bắt đầu trực diện bằng đối tượng và số liệu, ví dụ: "Thị trường ... ghi nhận..."'),
    (r"trong thời đại (4\.0|công nghệ số|số hóa)", "Mở đầu sáo rỗng, không cung cấp thông tin",
     "Bắt đầu trực diện bằng đối tượng và số liệu nghiên cứu."),
    (r"đóng vai trò (vô cùng|hết sức|rất) quan trọng", "Tính từ cảm tính, mơ hồ, thiếu định lượng",
     'Định lượng cụ thể, ví dụ: "Là nguồn thu nhập cốt lõi, đóng góp X% trong tổng cơ cấu..."'),
    (r"góp phần không nhỏ", "Tính từ cảm tính, mơ hồ, thiếu định lượng",
     "Định lượng mức đóng góp cụ thể thay vì diễn đạt mơ hồ."),
    (r"có thể thấy rằng", "Khẩu ngữ, áp đặt quan điểm chủ quan",
     'Dẫn thẳng vào bằng chứng: "Số liệu thực nghiệm tại Bảng X.Y chỉ ra rằng..."'),
    (r"không thể phủ nhận rằng", "Khẩu ngữ, áp đặt quan điểm chủ quan",
     "Dẫn thẳng vào bằng chứng thay vì khẳng định chủ quan."),
    (r"mang tính đột phá", "Thổi phồng kết quả thiếu cơ sở",
     'Nêu con số cụ thể: "Đạt độ chính xác ROC-AUC = ..., vượt trội X% so với mô hình cơ sở"'),
    (r"đạt kết quả vô cùng ấn tượng", "Thổi phồng kết quả thiếu cơ sở",
     "Nêu con số cụ thể thay vì tính từ cảm thán."),
    (r"ngày càng trở nên cấp thiết", "Khẩu hiệu hành chính, không mang tính học thuật",
     'Nêu hệ quả định lượng, ví dụ: "Làm gia tăng chi phí ... lên gấp X lần"'),
    (r"tiến hành thực hiện việc", "Dài dòng, lặp từ vô nghĩa",
     'Rút gọn trực tiếp, ví dụ: "Phân tích..." thay vì "Tiến hành thực hiện việc phân tích..."'),
    (r"đưa ra một cái nhìn sâu sắc", "Dịch vụng từ tiếng Anh (give a deep insight)",
     'Diễn đạt cụ thể hơn: "Làm rõ cơ chế hành vi...", "Nhận diện quy luật..."'),
]

# ==============================================================================
# 2. KHẲNG ĐỊNH TUYỆT ĐỐI HÓA THIẾU CƠ SỞ (Overclaim) — nguồn §1.1 thang đo Epistemic Modality
# ==============================================================================
OVERCLAIM_PATTERNS = [
    r"hoàn toàn đúng",
    r"chắc chắn 100%",
    r"chân lý tuyệt đối",
    r"đột phá không thể chối cãi",
    r"vô song",
    r"chắc chắn do\b",
    r"hiển nhiên vì\b",
    r"không (thể|ai) bàn cãi",
]

# ==============================================================================
# 3. NGUY CƠ DIỄN ĐẠT TƯƠNG QUAN THÀNH NHÂN QUẢ — nguồn §1.2
# ==============================================================================
CORRELATION_MARKERS = [r"tương quan", r"có mối liên hệ", r"có liên quan", r"đi kèm với"]
CAUSAL_VERBS = [
    r"gây ra", r"dẫn đến", r"làm cho\b", r"khiến cho\b", r"khiến\b",
    r"tác động trực tiếp làm", r"bắt buộc dẫn đến", r"tạo ra\b",
]

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?…])\s+|\n+")


def _split_sentences(paragraph_text):
    return [s.strip() for s in _SENTENCE_SPLIT_RE.split(paragraph_text) if s.strip()]


def _find_matches(patterns, text):
    hits = []
    for pat in patterns:
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            hits.append((m.start(), m.end(), m.group(0)))
    return hits


# ==============================================================================
# ĐỌC NỘI DUNG TỪ FILE (.docx / .md / .txt)
# ==============================================================================
def load_paragraphs(file_path):
    """Trả về list các đoạn văn (bỏ đoạn rỗng) từ file .docx, .md hoặc .txt."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".docx":
        if docx is None:
            raise RuntimeError("Cần cài python-docx để đọc file .docx: pip install python-docx")
        d = docx.Document(file_path)
        return [p.text for p in d.paragraphs if p.text.strip()]
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # .md / .txt: đoạn văn phân tách bởi dòng trống
        raw_paras = re.split(r"\n\s*\n", content)
        return [p.strip() for p in raw_paras if p.strip()]


# ==============================================================================
# CHẤM ĐIỂM MỘT ĐOẠN VĂN
# ==============================================================================
def audit_paragraph(paragraph_text, paragraph_index):
    """Trả về list finding cho một đoạn văn: mỗi finding là 1 dict."""
    findings = []

    for pattern, reason, suggestion in CLICHE_PATTERNS:
        for m in re.finditer(pattern, paragraph_text, flags=re.IGNORECASE):
            findings.append({
                "paragraph": paragraph_index,
                "category": "Sáo ngữ / AI smell",
                "matched_text": m.group(0),
                "reason": reason,
                "suggestion": suggestion,
                "context": _context_snippet(paragraph_text, m.start(), m.end()),
            })

    for pattern in OVERCLAIM_PATTERNS:
        for m in re.finditer(pattern, paragraph_text, flags=re.IGNORECASE):
            findings.append({
                "paragraph": paragraph_index,
                "category": "Khẳng định tuyệt đối hóa (Overclaim)",
                "matched_text": m.group(0),
                "reason": "Mức độ khẳng định vượt quá sức nặng bằng chứng thông thường có thể chứng minh được",
                "suggestion": "Kiểm tra lại: có bằng chứng thực nghiệm đủ mạnh (p<0.001, kiểm định bác bỏ H0) để giữ mức khẳng định này không? Nếu không, hạ xuống 'cho thấy/chỉ ra/gợi ý' theo thang đo Epistemic Modality.",
                "context": _context_snippet(paragraph_text, m.start(), m.end()),
            })

    for sentence in _split_sentences(paragraph_text):
        has_corr = any(re.search(p, sentence, flags=re.IGNORECASE) for p in CORRELATION_MARKERS)
        if not has_corr:
            continue
        for cv in CAUSAL_VERBS:
            m = re.search(cv, sentence, flags=re.IGNORECASE)
            if m:
                findings.append({
                    "paragraph": paragraph_index,
                    "category": "Nguy cơ Tương quan → Nhân quả",
                    "matched_text": m.group(0),
                    "reason": "Câu vừa nêu 'tương quan' vừa dùng động từ nhân quả trong cùng câu — chỉ hợp lệ nếu thiết kế nghiên cứu là RCT/IV/DID/RDD",
                    "suggestion": 'Nếu chỉ là dữ liệu cắt ngang/tương quan: đổi thành "có mối tương quan đồng biến/nghịch biến với..." hoặc "phản ánh mối liên hệ thống kê có ý nghĩa". Chỉ giữ động từ nhân quả nếu có thiết kế thực nghiệm/bán thực nghiệm hỗ trợ.',
                    "context": sentence,
                })
                break  # một câu chỉ cần báo 1 lần cho mục này, tránh trùng lặp

    return findings


def audit_text(paragraphs):
    """paragraphs: list[str]. Trả về list finding trên toàn bộ văn bản."""
    all_findings = []
    for i, para in enumerate(paragraphs, start=1):
        all_findings.extend(audit_paragraph(para, i))
    return all_findings


def audit_file(file_path):
    paragraphs = load_paragraphs(file_path)
    return audit_text(paragraphs), len(paragraphs)


def _context_snippet(text, start, end, radius=40):
    lo = max(0, start - radius)
    hi = min(len(text), end + radius)
    prefix = "…" if lo > 0 else ""
    suffix = "…" if hi < len(text) else ""
    return f"{prefix}{text[lo:hi]}{suffix}"


# ==============================================================================
# BÁO CÁO
# ==============================================================================
def print_report(findings, total_paragraphs, source_name=""):
    print("=== ACADEMIC EDITOR: BÁO CÁO RÀ SOÁT VĂN PHONG ===")
    if source_name:
        print(f"Nguồn: {source_name}")
    print(f"Tổng số đoạn văn: {total_paragraphs}")
    print(f"Tổng số điểm cần xem xét: {len(findings)}")
    if not findings:
        print("✅ Không phát hiện sáo ngữ / overclaim / nguy cơ tương quan-nhân quả theo bộ lọc hiện có.")
        print("Lưu ý: bộ lọc dựa trên từ khóa, không thay thế việc đọc lại toàn văn bằng con người.")
        return
    by_category = {}
    for f in findings:
        by_category.setdefault(f["category"], []).append(f)
    for cat, items in by_category.items():
        print(f"\n--- {cat} ({len(items)} điểm) ---")
        for f in items:
            print(f"  [Đoạn {f['paragraph']}] \"{f['matched_text']}\"")
            print(f"    Ngữ cảnh : {f['context']}")
            print(f"    Lý do    : {f['reason']}")
            print(f"    Gợi ý    : {f['suggestion']}")


def write_markdown_report(findings, total_paragraphs, output_path, source_name=""):
    lines = ["# Báo cáo rà soát văn phong học thuật", ""]
    if source_name:
        lines.append(f"**Nguồn:** {source_name}")
    lines.append(f"**Tổng số đoạn văn:** {total_paragraphs}")
    lines.append(f"**Tổng số điểm cần xem xét:** {len(findings)}")
    lines.append("")
    if not findings:
        lines.append("✅ Không phát hiện sáo ngữ / overclaim / nguy cơ tương quan-nhân quả theo bộ lọc hiện có.")
    else:
        by_category = {}
        for f in findings:
            by_category.setdefault(f["category"], []).append(f)
        for cat, items in by_category.items():
            lines.append(f"## {cat} ({len(items)} điểm)")
            lines.append("")
            for f in items:
                lines.append(f"- **Đoạn {f['paragraph']}** — \"{f['matched_text']}\"")
                lines.append(f"  - Ngữ cảnh: {f['context']}")
                lines.append(f"  - Lý do: {f['reason']}")
                lines.append(f"  - Gợi ý: {f['suggestion']}")
            lines.append("")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return output_path


# ==============================================================================
# CLI
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="Rà soát sáo ngữ / overclaim / nguy cơ tương quan-nhân quả trong bản thảo học thuật.")
    parser.add_argument("input_file", help="Đường dẫn file .docx / .md / .txt cần rà soát")
    parser.add_argument("--out", help="Nếu truyền, ghi báo cáo dạng Markdown ra file này thay vì chỉ in console")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"[ERROR] Không tìm thấy file: {args.input_file}", file=sys.stderr)
        sys.exit(1)

    findings, total_paragraphs = audit_file(args.input_file)
    print_report(findings, total_paragraphs, source_name=args.input_file)

    if args.out:
        write_markdown_report(findings, total_paragraphs, args.out, source_name=args.input_file)
        print(f"\nĐã ghi báo cáo Markdown: {args.out}")


if __name__ == "__main__":
    main()

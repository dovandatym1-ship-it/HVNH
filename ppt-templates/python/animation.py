"""Động cơ hoạt họa PPT - Thao tác hiệu ứng hoạt ảnh thông qua OOXML XML"""

from lxml import etree


def _build_animation_xml(shape_id, anim_type, delay=0, duration=500):
    """Xây dựng đoạn mã XML hoạt ảnh"""
    nsmap = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    }

    if anim_type == "fade_in":
        return _fade_animation(shape_id, delay, duration, "fade", "in")
    elif anim_type == "fade_out":
        return _fade_animation(shape_id, delay, duration, "fade", "out")
    elif anim_type == "fly_in_bottom":
        return _fly_in_animation(shape_id, delay, duration, "b")
    elif anim_type == "fly_in_left":
        return _fly_in_animation(shape_id, delay, duration, "l")
    elif anim_type == "fly_in_right":
        return _fly_in_animation(shape_id, delay, duration, "r")
    elif anim_type == "fly_in_top":
        return _fly_in_animation(shape_id, delay, duration, "t")
    elif anim_type == "wipe":
        return _wipe_animation(shape_id, delay, duration)
    elif anim_type == "grow":
        return _grow_shrink_animation(shape_id, delay, duration, 0, 100)
    elif anim_type == "shrink":
        return _grow_shrink_animation(shape_id, delay, duration, 100, 0)
    elif anim_type == "spin":
        return _spin_animation(shape_id, delay, duration)
    elif anim_type == "appear":
        return _appear_animation(shape_id, delay)
    else:
        return _fade_animation(shape_id, delay, duration, "fade", "in")


def _fade_animation(shape_id, delay, duration, effect, direction):
    """Hoạt ảnh làm mờ dần / hiện dần (fade in/out)"""
    return f'''<p:seq concurrent="1" nextAc="seek" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:childTnLst>
    <p:seq concurrent="1" nextAc="seek">
      <p:childTnLst>
        <p:set>
          <p:cBhvr>
            <p:stCondLst><p:cond delay="0"/></p:stCondLst>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
          <p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>
        </p:set>
        <p:anim effect="{effect}" filter="{direction}">
          <p:cBhvr>
            <p:stCondLst><p:cond delay="{delay}"/></p:stCondLst>
            <p:duration>{duration}</p:duration>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
        </p:anim>
      </p:childTnLst>
      <p:nodeType>clickEffect</p:nodeType>
    </p:seq>
  </p:childTnLst>
</p:seq>'''


def _fly_in_animation(shape_id, delay, duration, direction):
    """Hoạt ảnh bay vào (fly in)"""
    # Thiết lập tọa độ điểm đầu và điểm cuối theo hướng bay (tỷ lệ phần trăm so với slide)
    direction_map = {
        'b': {'from': '50,110', 'to': '50,50'},   # Bay vào từ dưới
        't': {'from': '50,-10', 'to': '50,50'},    # Bay vào từ trên
        'l': {'from': '-10,50', 'to': '50,50'},    # Bay vào từ trái
        'r': {'from': '110,50', 'to': '50,50'},    # Bay vào từ phải
    }
    pos = direction_map.get(direction, direction_map['b'])
    return f'''<p:seq concurrent="1" nextAc="seek" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:childTnLst>
    <p:seq concurrent="1" nextAc="seek">
      <p:childTnLst>
        <p:set>
          <p:cBhvr>
            <p:stCondLst><p:cond delay="0"/></p:stCondLst>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
          <p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>
        </p:set>
        <p:animMotion origin="layout" from="{pos['from']}" to="{pos['to']}" fill="hold">
          <p:cBhvr>
            <p:stCondLst><p:cond delay="{delay}"/></p:stCondLst>
            <p:duration>{duration}</p:duration>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
        </p:animMotion>
      </p:childTnLst>
      <p:nodeType>clickEffect</p:nodeType>
    </p:seq>
  </p:childTnLst>
</p:seq>'''


def _wipe_animation(shape_id, delay, duration):
    """Hoạt ảnh quét (wipe)"""
    return f'''<p:seq concurrent="1" nextAc="seek" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:childTnLst>
    <p:seq concurrent="1" nextAc="seek">
      <p:childTnLst>
        <p:set>
          <p:cBhvr>
            <p:stCondLst><p:cond delay="0"/></p:stCondLst>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
          <p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>
        </p:set>
        <p:anim effect="wipe" filter="in">
          <p:cBhvr>
            <p:stCondLst><p:cond delay="{delay}"/></p:stCondLst>
            <p:duration>{duration}</p:duration>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
        </p:anim>
      </p:childTnLst>
      <p:nodeType>clickEffect</p:nodeType>
    </p:seq>
  </p:childTnLst>
</p:seq>'''


def _grow_shrink_animation(shape_id, delay, duration, from_scale, to_scale):
    """Hoạt ảnh phóng to / thu nhỏ (grow/shrink)"""
    return f'''<p:seq concurrent="1" nextAc="seek" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:childTnLst>
    <p:seq concurrent="1" nextAc="seek">
      <p:childTnLst>
        <p:anim effect="grow" calcmode="lin" valueType="num">
          <p:cBhvr>
            <p:stCondLst><p:cond delay="{delay}"/></p:stCondLst>
            <p:duration>{duration}</p:duration>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
          <p:tavLst>
            <p:tav pos="0"><p:val><p:strVal val="{from_scale}%"/></p:val></p:tav>
            <p:tav pos="100000"><p:val><p:strVal val="{to_scale}%"/></p:val></p:tav>
          </p:tavLst>
        </p:anim>
      </p:childTnLst>
      <p:nodeType>clickEffect</p:nodeType>
    </p:seq>
  </p:childTnLst>
</p:seq>'''


def _spin_animation(shape_id, delay, duration):
    """Hoạt ảnh xoay tròn (spin)"""
    return f'''<p:seq concurrent="1" nextAc="seek" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:childTnLst>
    <p:seq concurrent="1" nextAc="seek">
      <p:childTnLst>
        <p:anim effect="spin" calcmode="lin" valueType="num">
          <p:cBhvr>
            <p:stCondLst><p:cond delay="{delay}"/></p:stCondLst>
            <p:duration>{duration}</p:duration>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
          <p:tavLst>
            <p:tav pos="0"><p:val><p:strVal val="0"/></p:val></p:tav>
            <p:tav pos="100000"><p:val><p:strVal val="3600000"/></p:val></p:tav>
          </p:tavLst>
        </p:anim>
      </p:childTnLst>
      <p:nodeType>clickEffect</p:nodeType>
    </p:seq>
  </p:childTnLst>
</p:seq>'''


def _appear_animation(shape_id, delay):
    """Hoạt ảnh xuất hiện (appear)"""
    return f'''<p:seq concurrent="1" nextAc="seek" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:childTnLst>
    <p:seq concurrent="1" nextAc="seek">
      <p:childTnLst>
        <p:set>
          <p:cBhvr>
            <p:stCondLst><p:cond delay="{delay}"/></p:stCondLst>
            <p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl>
          </p:cBhvr>
          <p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>
        </p:set>
      </p:childTnLst>
      <p:nodeType>clickEffect</p:nodeType>
    </p:seq>
  </p:childTnLst>
</p:seq>'''


def apply_animations_to_slide(slide, animations):
    """Áp dụng một tập hợp hoạt ảnh cho slide

    Args:
        slide: Đối tượng slide
        animations: Danh sách hoạt ảnh, mỗi phần tử là (shape_id, anim_type, delay, duration)
    """
    if not animations:
        return

    timing_xml = '<p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
    timing_xml += '<p:tnLst>'

    for shape_id, anim_type, delay, duration in animations:
        timing_xml += _build_animation_xml(shape_id, anim_type, delay, duration)

    timing_xml += '</p:tnLst></p:timing>'

    slide._element.append(etree.fromstring(timing_xml))


def add_slide_morph_transition(slide):
    """Thêm hiệu ứng chuyển slide biến đổi Morph"""
    xml_str = '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" advClick="1" advTm="1000"><p:morph advClick="1"/></p:transition>'
    slide._element.append(etree.fromstring(xml_str))

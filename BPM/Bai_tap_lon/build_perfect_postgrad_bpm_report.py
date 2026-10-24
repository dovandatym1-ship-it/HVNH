#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Academic Master Report Builder for HVNH Postgraduate Program
Báo cáo Bài tập nhóm: Quản lý Quy trình Nghiệp vụ (BPM)
Khoa Sau Đại học - Học viện Ngân hàng
Chuyển hóa trực tiếp từ Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.md
sang Bao_cao_BPM_Tin_dung_Giai_ngan_LPBank_HOAN_THIEN.docx chuẩn mực OpenXML.
"""

from build_clean_academic_bpm_report import compile_markdown_to_docx, INPUT_MD, OUTPUT_DOCX

if __name__ == '__main__':
    compile_markdown_to_docx(INPUT_MD, OUTPUT_DOCX)

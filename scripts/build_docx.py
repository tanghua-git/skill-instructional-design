#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
教学设计 Markdown → 规范排版 DOCX 转换器（公开课版）
====================================================
用法：python3 build_docx.py <输入.md> [输出.docx]

将 Agent 生成的「约定语法 Markdown」一键转换为版式规范的 Word 教案：
- A4 页面、标准页边距、页脚页码
- 标题黑体、正文仿宋、表格宋体的中文公文式排版
- 「思路主线」自动渲染为竖向流程框图（表格实现，任何 Word 版本不错位）
- 教学过程四列表自动设置列宽，表头底纹
- 附录自动另起一页

支持的 Markdown 子集（详见 references/docx-format-spec.md）：
  # 主标题（仅一个）          ## 一级章节标题      ### 二级小节标题
  @info 课时信息行（居中）    | 表格 |（首行为表头）
  > 引用块（设计意图，灰字）  - 无序列表 / 1. 有序列表
  **加粗**                    --- 分隔线（忽略）
"""
import sys
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import parse_xml

# ─────────────────────────────────────────────
# 版式常量（公开课教案打印标准）
# ─────────────────────────────────────────────
FONT_TITLE = "黑体"       # 主标题 / 章节标题
FONT_SUB = "楷体"         # 信息行 / 引用块
FONT_BODY = "仿宋_GB2312" # 正文（兼容名：仿宋）
FONT_TABLE = "宋体"       # 表格文字
FONT_HEAD = "黑体"        # 表头
FONT_WEST = "Times New Roman"

SZ_MAIN_TITLE = Pt(22)    # 二号  主标题
SZ_INFO = Pt(14)          # 四号  信息行
SZ_H1 = Pt(16)            # 三号  一级章节标题
SZ_H2 = Pt(14)            # 四号  二级小节标题
SZ_BODY = Pt(12)          # 小四  正文
SZ_TABLE = Pt(10.5)       # 五号  表格
SZ_QUOTE = Pt(11)         # 小四偏小 引用块

C_SHADE_HEAD = "D9E2F3"   # 表头底纹：浅蓝
C_SHADE_STEP = "DEEBF7"   # 流程环节标题底纹：更浅蓝
C_QUOTE = RGBColor(0x40, 0x40, 0x40)  # 引用块灰字

FOUR_COL_WIDTHS = [Cm(6.8), Cm(4.6), Cm(3.0), Cm(3.0)]  # 教学过程四列表列宽（合计≈17.4cm 版心）


def set_run_font(run, cn_font, size, bold=False, color=None):
    """同时设置中西文字体（python-docx 必须两处都设，否则中文不生效）。"""
    run.font.name = FONT_WEST
    run.font.size = size
    run.font.bold = bold
    if color is not None:
        run.font.color.rgb = color
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = parse_xml(r'<w:rFonts xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
        rPr.append(rFonts)
    rFonts.set(qn("w:eastAsia"), cn_font)


def shade_cell(cell, hex_color):
    """单元格底纹。"""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(
        r'<w:shd xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        r'w:val="clear" w:color="auto" w:fill="%s"/>' % hex_color
    )
    tcPr.append(shd)


def write_rich_text(paragraph, text, cn_font, size, base_bold=False, color=None):
    """解析 **加粗** 内联标记写入段落。"""
    for i, seg in enumerate(re.split(r"\*\*", text)):
        if not seg:
            continue
        run = paragraph.add_run(seg)
        set_run_font(run, cn_font, size, bold=base_bold or (i % 2 == 1), color=color)


def add_paragraph_md(doc, text, cn_font=FONT_BODY, size=SZ_BODY, align=None,
                     indent=True, space_after=Pt(4), line=1.4):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    if align is not None:
        pf.alignment = align
    if indent:
        pf.first_line_indent = size * 2  # 首行缩进2字符
    pf.space_after = space_after
    pf.line_spacing = line
    write_rich_text(p, text, cn_font, size)
    return p


# ─────────────────────────────────────────────
# 文档骨架：页面、页脚页码
# ─────────────────────────────────────────────
def setup_document():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)   # A4
    sec.top_margin = sec.bottom_margin = Cm(2.54)
    sec.left_margin = sec.right_margin = Cm(2.8)
    # 页脚页码：第 X 页
    footer_p = sec.footer.paragraphs[0]
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer_p.add_run("第 ")
    set_run_font(run, FONT_TABLE, Pt(9))
    fld = parse_xml(
        r'<w:fldSimple xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:instr=" PAGE ">'
        r'<w:r><w:rPr><w:rFonts w:eastAsia="宋体" w:ascii="Times New Roman"/><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r>'
        r"</w:fldSimple>"
    )
    footer_p._p.append(fld)
    run = footer_p.add_run(" 页")
    set_run_font(run, FONT_TABLE, Pt(9))
    return doc


# ─────────────────────────────────────────────
# 表格渲染
# ─────────────────────────────────────────────
def add_heading_row_style(cell, text):
    """表头单元格：黑体居中 + 底纹。"""
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    write_rich_text(p, text, FONT_HEAD, SZ_TABLE, base_bold=True)
    shade_cell(cell, C_SHADE_HEAD)


def add_body_row_style(cell, text, center=False):
    """表格正文单元格：宋体五号。"""
    cell.text = ""
    lines = [ln for ln in text.split("<br>")] if "<br>" in text else [text]
    first = True
    for ln in lines:
        p = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        if center:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        write_rich_text(p, ln, FONT_TABLE, SZ_TABLE)


def render_generic_table(doc, rows):
    """通用表格：首行表头底纹。"""
    n_cols = max(len(r) for r in rows)
    t = doc.add_table(rows=len(rows), cols=n_cols)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = True
    for r_idx, row in enumerate(rows):
        for c_idx in range(n_cols):
            text = row[c_idx] if c_idx < len(row) else ""
            cell = t.cell(r_idx, c_idx)
            if r_idx == 0:
                add_heading_row_style(cell, text)
            else:
                add_body_row_style(cell, text, center=(n_cols >= 3 and c_idx > 0 and len(text) <= 12))
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def render_four_col_table(doc, rows):
    """教学过程四列表（环节流程|为什么这样设计|教师行为|学生行为）：固定列宽。"""
    t = doc.add_table(rows=len(rows), cols=4)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for c_idx, w in enumerate(FOUR_COL_WIDTHS):
        for r_idx in range(len(rows)):
            t.cell(r_idx, c_idx).width = w
    for r_idx, row in enumerate(rows):
        for c_idx in range(4):
            text = row[c_idx] if c_idx < len(row) else ""
            cell = t.cell(r_idx, c_idx)
            if r_idx == 0:
                add_heading_row_style(cell, text)
            else:
                add_body_row_style(cell, text)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def render_flow_chart(doc, rows):
    """思路主线：竖向流程框图（环节框 + 箭头交替），任何 Word 版本渲染不错位。

    输入表格约定：| 环节 | 为什么这样安排 |
    """
    for idx, row in enumerate(rows[1:]):
        if len(row) < 2:
            continue
        step_name, why = row[0], row[1]
        # 环节框：1 列 2 行小表格
        t = doc.add_table(rows=2, cols=1)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        t.cell(0, 0).width = Cm(14)
        t.cell(1, 0).width = Cm(14)
        # 行1：环节名（底纹 + 黑体居中）
        c = t.cell(0, 0)
        c.text = ""
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        write_rich_text(p, step_name, FONT_HEAD, Pt(12), base_bold=True)
        shade_cell(c, C_SHADE_STEP)
        # 行2：设计理由（直接呈现，无前缀）
        c = t.cell(1, 0)
        c.text = ""
        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.3
        write_rich_text(p, why, FONT_TABLE, SZ_TABLE)
        # 箭头行（末环节之后不加）；固定段距保证所有箭头间距一致
        if idx < len(rows) - 2:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.0
            run = p.add_run("↓")
            set_run_font(run, FONT_HEAD, Pt(14), bold=True)
    tail = doc.add_paragraph()
    tail.paragraph_format.space_after = Pt(2)
    tail.paragraph_format.line_spacing = 1.0


# ─────────────────────────────────────────────
# Markdown 子集解析
# ─────────────────────────────────────────────
HEAD_FLOW = "思路主线"
HEAD_FOUR = ("环节流程", "为什么这样设计", "教师行为", "学生行为")


def parse_table_block(lines, i):
    """收集从 i 开始的连续表格行，返回 (rows, next_i)。自动剔除 |---| 分隔行。"""
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        raw = lines[i].strip().strip("|")
        cells = [c.strip() for c in raw.split("|")]
        if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
            rows.append(cells)
        i += 1
    return rows, i


def convert(md_path, docx_path):
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    doc = setup_document()
    in_flow_section = False
    title_done = False

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line.strip() or line.strip() == "---":
            i += 1
            continue

        # @info 信息行 → 居中楷体（超宽自动降字号防断行）
        if line.startswith("@info"):
            text = line[len("@info"):].strip()
            sz = SZ_INFO if len(text) <= 32 else Pt(12)
            add_paragraph_md(doc, text, FONT_SUB, sz,
                             align=WD_ALIGN_PARAGRAPH.CENTER, indent=False, space_after=Pt(2))
            i += 1
            continue

        # 主标题
        if line.startswith("# ") and not line.startswith("## "):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(10)
            write_rich_text(p, line[2:].strip(), FONT_TITLE, SZ_MAIN_TITLE, base_bold=True)
            title_done = True
            i += 1
            continue

        # 一级章节标题
        if line.startswith("## "):
            text = line[3:].strip()
            in_flow_section = HEAD_FLOW in text
            p = doc.add_paragraph()
            pf = p.paragraph_format
            pf.space_before = Pt(14)
            pf.space_after = Pt(8)
            if "附录" in text:  # 附录另起一页
                pf.page_break_before = True
            write_rich_text(p, text, FONT_TITLE, SZ_H1, base_bold=True)
            i += 1
            continue

        # 二级小节标题（环节）
        if line.startswith("### "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(6)
            write_rich_text(p, line[4:].strip(), FONT_TITLE, SZ_H2, base_bold=True)
            i += 1
            continue

        # 引用块（可多行合并）
        if line.startswith(">"):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip().lstrip(">").strip())
                i += 1
            text = " ".join(q for q in quote_lines if q)
            p = doc.add_paragraph()
            pf = p.paragraph_format
            pf.left_indent = Cm(0.74)
            pf.space_after = Pt(4)
            pf.line_spacing = 1.3
            run = p.add_run("◆ ")
            set_run_font(run, FONT_SUB, SZ_QUOTE, bold=True, color=C_QUOTE)
            write_rich_text(p, text, FONT_SUB, SZ_QUOTE, color=C_QUOTE)
            continue

        # 表格
        if line.strip().startswith("|"):
            rows, i = parse_table_block(lines, i)
            if not rows:
                continue
            header = rows[0]
            if in_flow_section:
                render_flow_chart(doc, rows)
                in_flow_section = False  # 流程表只渲染该章节第一个表格
            elif len(header) == 4 and header[0].strip() == HEAD_FOUR[0] and header[1].strip() == HEAD_FOUR[1]:
                render_four_col_table(doc, rows)
            else:
                render_generic_table(doc, rows)
            continue

        # 有序 / 无序列表
        m_ul = re.match(r"^[-*·]\s+(.*)", line.strip())
        m_ol = re.match(r"^(\d+)[.、)]\s+(.*)", line.strip())
        if m_ul or m_ol:
            text = m_ul.group(1) if m_ul else m_ol.group(2)
            marker = "· " if m_ul else m_ol.group(1) + ". "
            p = doc.add_paragraph()
            pf = p.paragraph_format
            pf.left_indent = Cm(0.74)
            pf.space_after = Pt(3)
            pf.line_spacing = 1.4
            run = p.add_run(marker)
            set_run_font(run, FONT_BODY, SZ_BODY, bold=True)
            write_rich_text(p, text, FONT_BODY, SZ_BODY)
            i += 1
            continue

        # 普通段落
        add_paragraph_md(doc, line.strip())
        i += 1

    if not title_done:
        sys.stderr.write("[warn] 未找到 '# 主标题'，文档将以无标题形式生成\n")

    doc.save(docx_path)
    print(f"[ok] 已生成：{docx_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else re.sub(r"\.md$", "", src) + ".docx"
    convert(src, dst)

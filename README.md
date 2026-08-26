# Skill: 教学设计师 (Instructional Design)

![GitHub Repo stars](https://img.shields.io/github/stars/tanghua-git/skill-instructional-design?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/tanghua-git/skill-instructional-design?style=flat-square)
![GitHub](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Topics](https://img.shields.io/badge/tags-instructional--design%20%7C%20ai--education%20%7C%20icap-brightgreen?style=flat-square)

> **中小学各学科公开课教学设计助手** — 统一公开课模式：完整设计流程 + 信息技术融合设计（逐环节标注）+ 教学亮点提炼 + 说课要点，内置理论参考库与规范 Word 排版引擎，输出可直接打印上课的教案文档。
>
> An AI-powered instructional design assistant for K-12 demo/open classes. Unified open-class workflow with IT-integration design, teaching highlights extraction, and lesson presentation (说课) notes. Built-in theory library and a standard Word formatting engine. Powered by ICAP, Bloom's Taxonomy, and Gradual Release of Responsibility frameworks.

---

## 🌟 Features

| Capability | Description |
|-----------|-------------|
| **Unified Open-Class Mode** 🎯 | Full design workflow + IT integration (per-step annotations) + highlights + 说课 notes — one mode for all demo/open/research classes |
| **5 Lesson Types** 📚 | New lesson / Review / Practice / Inquiry / Assessment review (each with a theory-matched decision tree) |
| **Multi-Agent Architecture** 🤖 | Student analyst, Content architect, Goal designer, Activity designer, Assessment designer, Motivation designer, Metacognition coach, QA reviewer, Open-class designer |
| **ICAP Framework** 🧠 | Interactive-Constructive-Active-Passive cognitive engagement optimization |
| **Bloom's Taxonomy** 📊 | 6×4 matrix for precise ABCD learning objectives (observable verbs only) |
| **IT Integration Design** 🖥 | Per-step tech annotations (希沃白板 etc.) with failure fallbacks — technology serves teaching, never for its own sake |
| **8-D Quality Check** 🔍 | Goals ↔ activities ↔ assessment alignment + readability audit (v4.0: jargon-free plain language guaranteed) |
| **Word Export** 📄 | Standard-formatted .docx lesson plans via built-in formatting engine (print-ready, 仿宋/黑体/楷体 typography) |

---

## 🆕 What's New

### v4.0 (2026-08) — Unified Open-Class Edition

- **Unified Open-Class Mode** — Replaces the Lite/Pro split with one full workflow: complete design process + IT integration design (per-step annotations) + teaching highlights (3-5 items, each traceable to a step) + 说课要点 (6-part presentation notes).
- **IT Integration Design** — Every step annotated with tool usage (希沃白板5, 实物展台, AI tools, etc.), each answering "what teaching problem does it solve", plus a full tech overview table with failure fallbacks. "Not using tech + reason" is also a professional judgment.
- **Standard Word Formatting Engine** — New: `scripts/build_docx.py` renders a spec-compliant Markdown to print-ready .docx (中文字体规范、流程框图、表格列宽、页码、附录分页). Format spec: `references/docx-format-spec.md`.
- **Open-Class Guide** — New: `references/open-class-guide.md` covering IT integration principles, highlights extraction methods, and the 说课 framework.
- **8-D Quality Check** — Readability and formatting compliance are now veto items; jargon must be collected into an appendix with plain-language explanations.

### v3.0 (2026-07)

- **Bilingual Expression Mechanism** — The skill thinks in professional theory internally, but outputs in plain, teacher-friendly language. Jargon is moved to an appendix with first-use explanations and "because…so…" rationale phrasing. New: `references/plain-language.md`.
- **Knowledge Base Now Optional** — KB integration is an enhancement layer, not a hard dependency. The skill works out of the box for anyone you share it with (all theory is distilled into `references/`).
- **Edge Cases Handbook** — New: `references/edge-cases.md` covering special class types, missing information, and fallback strategies.

---

## 📦 Installation

### As an OpenClaw Skill

```bash
# Clone the repo
git clone https://github.com/tanghua-git/skill-instructional-design.git \
  ~/.openclaw/skills/instructional-design

# Or install directly via OpenClaw:
openclaw skill install tanghua-git/skill-instructional-design
```

### As a standalone AI Agent Skill

Copy the `SKILL.md`, `references/`, and `scripts/` folders to your AI agent's skills directory:

```bash
cp -r skill-instructional-design ~/my-agent-skills/
```

---

## 🚀 Usage

> **Input:** "帮我做初中物理八年级下册《牛顿第一定律》的教案设计，我授课工具是希沃白板5"
> **Output:** Full open-class lesson plan with objectives, activities, assessment, board design, IT integration, highlights, and 说课 notes — delivered as a print-ready .docx

```
Unified Workflow (10 steps):
  Step 0    → Requirements Analysis
  Step 0.5  → Unit Positioning + Lesson Type Decision
  Step 1    → Student + Content + Motivation Analysis (parallel)
  Step 1.5  → Goal Design (Bloom's 6×4 matrix, ABCD format)
  Step 2    → Activity + Assessment + Metacognition (parallel, with per-step IT annotations)
  Step 2.5  → 5-D Consistency Review + Confidence Self-Assessment
  Step 3    → Open-Class Design (highlights + 说课 notes + IT overview with fallbacks)
  Step 4    → Lesson Plan Assembly → Word Export (build_docx.py)
  Step 5    → QA Feedback (8 dimensions)
  Step 6    → Implementation Issue Prediction
```

---

## 🧠 Theoretical Foundations

| Framework | Application | Source |
|-----------|-------------|--------|
| **ICAP** (Chi & Wylie) | Cognitive engagement optimization across lesson types | `references/icap-scaffold.md` |
| **Bloom's Taxonomy** (revised) | 6 cognitive processes × 4 knowledge types | `references/bloom-matrix.md` |
| **Gradual Release of Responsibility** | "I do → We do → You do" scaffolding | Embedded in activity design |
| **Self-Determination Theory** (Deci & Ryan) | Autonomy/Competence/Relatedness motivation design | `references/sdt-motivation.md` |
| **Backward Design** (UbD, Wiggins & McTighe) | Goals → Assessment → Activities | Embedded in workflow |
| **AI in Education Framework** | AI integration levels (No AI / AI-assisted / AI-integrated) | `references/ai-era-framework.md` |
| **Open-Class Design** | IT integration principles + highlights + 说课 framework | `references/open-class-guide.md` |

---

## 📁 Repository Structure

```
skill-instructional-design/
├── SKILL.md              # Main skill file (v4.0 — unified open-class edition)
├── README.md             # This file
├── references/
│   ├── plain-language.md           # v3.0: plain-language expression rules (jargon → appendix)
│   ├── open-class-guide.md         # v4.0: IT integration + highlights + 说课 framework
│   ├── docx-format-spec.md         # v4.0: Markdown→Word syntax & typography spec
│   ├── bloom-matrix.md             # Bloom's 6×4 matrix + ABCD objectives
│   ├── icap-scaffold.md            # ICAP framework + teaching strategy mapping
│   ├── assessment-design.md        # GRASPS + SOLO + tiered rubrics
│   ├── learner-analysis.md         # Misconception prediction + cognitive conflict design
│   ├── big-ideas.md                # Big ideas extraction methodology
│   ├── sdt-motivation.md           # Self-determination theory design patterns
│   ├── metacognition.md            # Reflection card templates + Think Aloud
│   ├── create-checklist.md         # CREATE 6-dimension QA checklist
│   ├── edge-cases.md               # v3.0: edge cases & fallback strategies
│   └── ai-era-framework.md         # AI in education: assessment taxonomy + teacher spectrum
└── scripts/
    ├── build_docx.py               # v4.0: Markdown → standard .docx formatting engine
    └── sample_test.md              # v4.0: format spec sample for engine testing
```

---

## 📊 Quality Score

| Dimension | Score | Note |
|-----------|-------|------|
| Frontmatter | ✅ 10/10 | Clear name, description, and trigger keywords |
| Workflow Clarity | ✅ 10/10 | Numbered steps with explicit inputs/outputs |
| Failure Mode Encoding | ✅ 10/10 | If-fail-then branches throughout |
| Checkpoint Design | ⏳ 6/10 | Logic exists, visual markers pending |
| Actionable Specificity | ✅ 10/10 | Concrete parameters, templates, and examples |
| Resource Integration | ✅ 10/10 | All reference paths correct and accessible |
| Architecture | ✅ 10/10 | Clean hierarchy, no redundancy |
| Empirical Testing | ✅ 10/10 | Test prompts validated (v4.0: 牛顿第一定律 open-class case) |

**Overall: 92+/100** — v2.1 Darwin baseline → v3.0 bilingual layer → v4.0 unified open-class edition.

---

## 🔗 Related Projects

- [OpenClaw](https://github.com/openclaw/openclaw) — AI agent platform
- [Darwin Skill](https://github.com/alchaincyf/darwin-skill) — Skill optimization framework
- [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills) — Academic workflow skills for OpenClaw

---

## 📄 License

MIT © 2026 Tanghua (唐华)

---

## 🤝 Contributing

Found an issue or have a suggestion? Feel free to [open an issue](https://github.com/tanghua-git/skill-instructional-design/issues) or submit a PR.

If this skill is useful to you, consider giving it a ⭐ — it helps others discover it!

---

*Built with ❤️ for K-12 educators. 教学法第一，工具第二。*

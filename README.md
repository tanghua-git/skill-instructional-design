# Skill: 教学设计师 (Instructional Design)

![GitHub Repo stars](https://img.shields.io/github/stars/tanghua-git/skill-instructional-design?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/tanghua-git/skill-instructional-design?style=flat-square)
![GitHub](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Topics](https://img.shields.io/badge/tags-instructional--design%20%7C%20ai--education%20%7C%20icap-brightgreen?style=flat-square)

> **中小学各学科公开课教学设计助手** — 以**导学问题驱动**为主轴（《问课》方法论）：完整设计流程 + 主问题与问题链设计 + 数智六要素融合（逐环节标注）+ 教学亮点提炼 + 说课要点，内置理论参考库与规范 Word 排版引擎，输出可直接打印上课的教案文档。
>
> An AI-powered instructional design assistant for K-12 demo/open classes, driven by the **Question-led Learning** methodology (《问课》). Unified open-class workflow with main-question & question-chain design, six-element IT integration, teaching highlights extraction, and lesson presentation (说课) notes. Built-in theory library and a standard Word formatting engine. Powered by 《问课》(Wenke), Bloom's Taxonomy (ABCD objectives), and Gradual Release of Responsibility frameworks.

---

## 🌟 Features

| Capability | Description |
|-----------|-------------|
| **Question-Driven Design** ❓ | v5.0 core: every lesson built around a main question + question chain (五何/良构劣构 typed, wait-time annotated) — 导学问题驱动，思维在问题中发生 |
| **Deep Understanding Anchor** ⚓ | Design philosophy from 《问课》: deep understanding as the invariant of good lessons + 3 anti-myth checks (热闹≠思维 etc.) + 5 types of thinking evidence |
| **Scenario Question Design** 🧭 | PBL (role+audience+task) / Big-unit (导语≠导学问题) / Cross-disciplinary (knowledge as卡点工具) — differentiated question design laws |
| **Six-Element IT Integration** 🖥 | Digital-classroom six elements (environment/activity/task/method/scaffold/process-value assessment) — technology serves thinking, never for its own sake |
| **Unified Open-Class Mode** 🎯 | Full design workflow + highlights + 说课 notes — one mode for all demo/open/research classes |
| **5 Lesson Types** 📚 | New lesson / Review / Practice / Inquiry / Assessment review (each with a theory-matched decision tree + question-chain type) |
| **Multi-Agent Architecture** 🤖 | 9 agents: student analyst, content architect, goal designer (main question & chain), activity designer, assessment designer (thinking evidence + process-value), motivation designer, metacognition coach, QA reviewer (question quality), open-class designer |
| **Bloom's Taxonomy** 📊 | 6×4 matrix for precise ABCD learning objectives (observable verbs only) |
| **8-D Quality Check** 🔍 | Dimension 3 rebuilt: question quality & thinking depth (six-feature check + chain progression + coverage map); readability veto retained |
| **Word Export** 📄 | Standard-formatted .docx lesson plans via built-in formatting engine (print-ready, 仿宋/黑体/楷体 typography) |

---

## 🆕 What's New

### v5.0 (2026-09) — Wenke Question-Driven Edition 问课重构版

- **Question-Driven Backbone** — 《问课》(胡小勇, 2026) becomes the first-principles methodology: deep understanding (深度理解) as the design anchor, question-led learning as the classroom engine. New Step 1.8 (Question Design) in the 11-step workflow.
- **4 New References** — `deep-understanding.md` (good-lesson invariant + 5 thinking evidences), `question-design.md` (6-dim question matrix + single-question six features + question set + question chain + shoufang method + human-AI co-design), `scenario-question-design.md` (PBL / big-unit / cross-disciplinary laws), `digital-classroom-six.md` (six elements + tech red lines + process-value assessment).
- **New Lesson-Plan Chapter** — "二、导学问题设计" (main question + question-chain table with type tags / cognitive level / wait time / step mapping); in-step questions carry chain IDs and type tags.
- **QA Dimension 3 Rebuilt** — "Cognitive engagement" → "Question quality & thinking depth" (single-question six-feature check + chain progression + coverage map + ≥2 thinking evidences).
- **Preserved Intact** — bilingual plain-language rules, one-glance flowchart, ABCD objectives, 9-agent architecture, open-class specials, Word engine, 5 lesson-type trees.

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
Unified Workflow (11 steps):
  Step 0    → Requirements Analysis (incl. scenario: single lesson / big-unit / PBL / cross-disciplinary)
  Step 0.5  → Unit Positioning + Lesson Type Decision
  Step 1    → Student + Content + Motivation Analysis (parallel, incl. "deep-understanding point")
  Step 1.5  → Goal Design (Bloom's 6×4 matrix, ABCD format) + Main Question
  Step 1.8  → Question Design (main question → matrix selection → question chain) ★v5.0
  Step 2    → Activity + Assessment + Metacognition (activities orbit the chain; typed questions)
  Step 2.5  → Consistency Review + Question Quality Review
  Step 3    → Open-Class Design (highlights + 说课 notes + six-element IT overview with fallbacks)
  Step 4    → Lesson Plan Assembly → Word Export (build_docx.py)
  Step 5    → QA Feedback (8 dimensions, D3 = question quality & thinking depth)
  Step 6    → Implementation Issue Prediction (incl. preset→generative shoufang plan)
```

---

## 🧠 Theoretical Foundations

| Framework | Application | Source |
|-----------|-------------|--------|
| **《问课》Wenke** (胡小勇, 2026) | v5.0 backbone: deep understanding anchor + question-led learning + WISE thinking evidence | `references/deep-understanding.md` |
| **Question Design System** | 6-dim matrix + six features + question set + chain + shoufang | `references/question-design.md` |
| **Scenario Question Laws** | PBL / big-unit / cross-disciplinary | `references/scenario-question-design.md` |
| **Digital-Classroom Six** | Six elements + human-AI division + process-value assessment | `references/digital-classroom-six.md` |
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
├── SKILL.md              # Main skill file (v5.0 — wenke question-driven edition)
├── README.md             # This file
├── references/
│   ├── deep-understanding.md       # v5.0: good-lesson invariant + 5 thinking evidences (《问课》ch.1)
│   ├── question-design.md          # v5.0: question matrix + six features + set + chain + shoufang (《问课》ch.4-5)
│   ├── scenario-question-design.md # v5.0: PBL / big-unit / cross-disciplinary question laws (《问课》ch.4)
│   ├── digital-classroom-six.md    # v5.0: six elements + tech red lines + process-value assessment (《问课》ch.6)
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
| Empirical Testing | ⏳ pending | v5.0 rebuild done; 牛顿第一定律 + PBL scenario tests to be re-validated |

**Overall: 92+/100** — v2.1 Darwin baseline → v3.0 bilingual layer → v4.0 unified open-class edition → v5.0 wenke question-driven rebuild.

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

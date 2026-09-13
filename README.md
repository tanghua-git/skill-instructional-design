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
| **Goal-Confirmation Gate** ✅ | v5.3: learning objectives must be sent to the user for confirmation before any further design — no large-scale rework after goals are locked (all subjects) |
| **Primary-Chinese Scaffold** 🧩 | v5.3: primary-Chinese-only "practice-block" backbone (two-period division / independent question chain for text comprehension / four integration methods) — other grades & subjects keep the question-chain backbone |

---

## 🆕 What's New

### v5.3 (2026-09-13) — 流程增强 · 小学语文骨架优化（Workflow & Primary-Chinese Scaffold）

本次更新分两类：**①通用流程增强（所有学科、所有学段适用）**；**②小学语文专属优化（仅限小学语文，不影响初高中语文与其他学科）**。

#### 一、通用流程增强（all subjects & grades）

- **目标确认关卡 Goal-Confirmation Gate（硬性）** — Step 1.5 产出教学目标卡后，**必须暂停并把目标发给用户核对**：用户确认，或按用户意见修改并再次确认后，才能进入 Step 1.8 及后续设计；用户未回复则停在该步等待。目的是避免"目标定型后整份教案大面积返工"。核对话术已内置（问三件事：基础字词/技能目标齐不齐、行为目标可不可测、要不要增删）。
- **目标完整性 Goal Completeness** — 教学目标必须"**三条腿齐全**"，缺一不可：**基础知识与基本技能**（语文的字词、朗读；数学的基本运算等，最容易被漏掉）＋ **素养目标** ＋ **应用与迁移目标**；并要求逐条对照本课知识点自检。

#### 二、小学语文专属优化（仅限小学语文 · primary Chinese only）

- **实践板块骨架 Practice-Block Backbone** — 小学语文的教学过程改按"**语言实践活动**"组织（不再是"问题链贯穿全课"）：**问题链只承载"精读品悟/精读深悟"板块**，导入、初读、写字、小结等板块用活动或任务推进。
- **两课时任务分工 Two-Period Division** —
  - **第一课时**＝导入激趣（任务导向）→ 初读课文·整体感知 → 认读字词·梳理脉络 → 写字巩固·小结；**任务重心＝生字词教学＋把握课文主要内容；不做深度理解**。
  - **第二课时**＝复习巩固（含听写）→ 精读深悟·深度理解课文 → 积累与表达运用 → 小结；**任务重心＝深度理解课文＋读写迁移**。
- **第一课时骨架三原则** —
  1. **导入必须指向本课任务**：只做"看图揭题、明确任务"，**不得越位去谈"怎样写清楚"**等深度理解话题（否则导入与后续板块格格不入）；
  2. **整体感知紧接初读**：遵循"从整体入手"——先读通、先知道"写了什么"，再进入字词与脉络，**整体感知不单独成环节排在字词之后**；
  3. **字词与脉络合并落实**：认读字词（随文正音）与梳理脉络（说清主要内容）放在同一板块。
- **课文理解独立成链** — 小学语文的"课文理解"**必须独立设计一条问题链**，沿"**整体把握 → 细部品读 → 深入体会 → 意义建构**"的梯度展开，自成体系、独立呈现（教案「二、导学问题设计」中单列"课文理解问题链"），不与其他板块（字词、写字、迁移运用）的问题混列。
- **融合四法 Four Integration Methods**（字词学习与教学主线融合的具体做法）：① **词串串主线**（把生字词按课文脉络编成几组词串，读词串即认角色、理内容）；② **关键词带全篇**（抓反复出现或关键的字词当读懂课文的抓手）；③ **分布落实**（认读在"初读"、书写在"写字"，不集中成块）；④ **书写相机穿插**（范写易错字＋同桌互评）。
- **适用范围严格限定** — 上述语文规则**仅适用于小学语文**；**初中语文、高中语文与数学、物理、化学、英语等其他学科，一律按"问题链骨架"组织教学环节，不套用"实践板块"与两课时分工**。

#### 三、本次同步还修复

- Step 4 文档结构中的第一课时骨架与 Step 2a **版本对齐**（此前两处不一致）；
- 全文"语文"规则统一加注"**仅限小学语文**"，消除对其他学段/学科的潜在影响。


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

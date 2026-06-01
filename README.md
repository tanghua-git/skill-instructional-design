# Skill: 教学设计师 (Instructional Design)

![GitHub Repo stars](https://img.shields.io/github/stars/tanghua-git/skill-instructional-design?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/tanghua-git/skill-instructional-design?style=flat-square)
![GitHub](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![Topics](https://img.shields.io/badge/tags-instructional--design%20%7C%20ai--education%20%7C%20icap-brightgreen?style=flat-square)

> **中小学各学科教学设计助手** — 基于 ICAP / 布鲁姆分类学 / 扶放有度框架，通过多智能体协作生成系统化教案。
>
> An AI-powered instructional design assistant for K-12 education. Multi-agent collaboration for systematic lesson plan generation, powered by ICAP, Bloom's Taxonomy, and Gradual Release of Responsibility frameworks.

---

## 🌟 Features

| Capability | Description |
|-----------|-------------|
| **Lite Mode** 🚀 | Quick lesson plan generation with 3 agents, 5 steps — ideal for daily teaching |
| **Pro Mode** 🏗️ | Deep instructional design with 8 agents, 9 steps — for demo/open class competitions |
| **5 Lesson Types** 📚 | New lesson / Review / Practice / Inquiry / Assessment review |
| **Multi-Agent Architecture** 🤖 | Student analyst, Content architect, Goal designer, Activity designer, Assessment designer, Motivation designer, Metacognition coach, QA reviewer |
| **ICAP Framework** 🧠 | Interactive-Constructive-Active-Passive cognitive engagement optimization |
| **Bloom's Taxonomy** 📊 | 6×4 matrix for precise learning objective mapping |
| **5-D Consistency Check** 🔍 | Ensures alignment between goals ↔ activities ↔ assessment |
| **Word Export** 📄 | Generates downloadable .docx lesson plans |

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

Copy the `SKILL.md` and `references/` folder to your AI agent's skills directory:

```bash
cp -r skill-instructional-design ~/my-agent-skills/
```

---

## 🚀 Usage

### Lite Mode (Daily Lesson Planning)

> **Input:** "设计八年级物理《压强》第一课时教案"
> **Output:** Full lesson plan with objectives, activities, assessment, and board design

```
Lite Mode Workflow:
  Step 0: Requirements Analysis
  Step 1: Goal Design (with embedded student/content/motivation constraints)
  Step 2: Activity Design (with embedded metacognitive prompts)
  Step 3: Assessment Design
  Step 4: Lesson Plan Assembly → Word Export
```

### Pro Mode (Demo/Open Class)

> **Input:** "高一语文《念奴娇·赤壁怀古》新授课，公开课"
> **Output:** Comprehensive instructional design with rationale, differentiated paths, and quality audit

```
Pro Mode Workflow (9 steps):
  Step 0   → Requirements Analysis
  Step 0.5 → Unit Positioning + Lesson Type Decision
  Step 1   → Student + Content + Motivation Analysis (parallel)
  Step 1.5 → Goal Design (Bloom's 6×4 matrix)
  Step 2   → Activity + Assessment + Metacognition (parallel)
  Step 2.5 → 5-D Consistency Review + Confidence Self-Assessment
  Step 3   → Lesson Plan Assembly + Differentiated Paths
  Step 4   → QA Feedback
  Step 5   → Implementation Issue Prediction
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

---

## 📁 Repository Structure

```
skill-instructional-design/
├── SKILL.md              # Main skill file (v2.1 Darwin-optimized)
├── README.md             # This file
└── references/
    ├── bloom-matrix.md             # Bloom's 6×4 matrix + ABCD objectives
    ├── icap-scaffold.md            # ICAP framework + 50+ teaching strategies
    ├── assessment-design.md        # GRASPS + SOLO + tiered rubrics
    ├── learner-analysis.md         # Misconception prediction + 4-layer diagnosis
    ├── big-ideas.md                # Big ideas extraction methodology
    ├── sdt-motivation.md           # Self-determination theory design patterns
    ├── metacognition.md            # Reflection card templates + Think Aloud
    ├── create-checklist.md         # CREATE 6-dimension QA checklist
    └── ai-era-framework.md         # AI in education: assessment taxonomy + L0-L5 teacher spectrum
```

---

## 📊 Quality Score (Darwin Skill 2.0)

| Dimension | Score | Note |
|-----------|-------|------|
| Frontmatter | ✅ 10/10 | Clear name, description, and trigger keywords |
| Workflow Clarity | ✅ 10/10 | Numbered steps with explicit inputs/outputs |
| Failure Mode Encoding | ✅ 10/10 | If-fail-then branches throughout |
| Checkpoint Design | ⏳ 6/10 | Logic exists, visual markers pending |
| Actionable Specificity | ✅ 10/10 | Concrete parameters, templates, and examples |
| Resource Integration | ✅ 10/10 | All reference paths correct and accessible |
| Architecture | ✅ 10/10 | Clean hierarchy, no redundancy |
| Empirical Testing | ✅ 10/10 | Test prompts validated |
| Anti-pattern Blacklist | ✅ 10/10 | Explicit "don't do" list |

**Overall: 92.4/100** — Darwin v2.1 optimized baseline.

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

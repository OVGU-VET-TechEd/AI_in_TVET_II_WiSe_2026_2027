<!--
author:    Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   1.0.0
language:  en
narrator:  UK English Female
mode:      Textbook

title:     S02 – AI vocabulary, models and workflows (Self-learning unit)
comment:   AI in TVET II – Self-learning unit for session 2 (10.12.2026): AI vocabulary for pedagogy, model types, agentic workflows, mapping an AI-enhanced pedagogical workflow; choice of the UNESCO learning objective and first draft of the competency matrix.
-->

# S02 – AI Vocabulary, Models and Workflows

> **Session 2 · 10.12.2026 · 🔵 Self-learning** – I am travelling; work through this unit with your group.
>
> **Time needed:** about 3 hours
>
> **Hand-in (Moodle, one per group): 16.12.2026, 23:59** – see the last chapter.

**After this unit you will be able to …**

1. use core AI terminology correctly when explaining AI-supported learning designs,
2. distinguish model types and choose a suitable one for a pedagogical task,
3. describe agentic AI and its opportunities and risks for professional development,
4. map an AI-enhanced pedagogical workflow for a TVET context,
5. choose your group's UNESCO learning objective and draft the competency matrix.

## 1. Vocabulary for AI Pedagogy

| Term | Definition | In a learning design |
| --- | --- | --- |
| **Data** | Examples used to train or ground a model | Your course texts, curriculum, case collection |
| **Algorithm** | Procedure that learns from data | Not visible to you, but determines behaviour |
| **Model** | Trained system with learned parameters | "GPT-…", "Claude …", a small local model |
| **Weights** | Learned numbers inside the model | Open-weight models can run locally (data protection) |
| **Prompt** | Instruction + context given to the model | Your template for nugget generation |
| **Context window** | What the model can consider at once | How much curriculum material you can include |
| **Grounding / RAG** | Answers based on retrieved documents | Quiz generated *only* from your verified text |
| **Fine-tuning** | Further training for a special purpose | Model adapted to a trade's terminology |
| **Agent** | LLM that plans, uses tools and acts in several steps | Assistant that researches, drafts and formats material |
| **Workflow** | Ordered sequence of steps with defined human checks | From learning objective to published nugget |
| **Hallucination** | Fluent but false output | Wrong safety rule in a quiz |

**Check:** You want the AI to answer *only* from the training regulation you upload. Which concept describes this?

- [( )] Fine-tuning
- [(X)] Grounding / retrieval-augmented generation
- [( )] Hallucination

## 2. Model Types and When to Use Them

| Model type | Typical use in learning design | Consider |
| --- | --- | --- |
| Large general LLM (cloud) | Drafting text, cases, quizzes, feedback | Data protection, cost, licence |
| Reasoning model | Complex planning, step-by-step solutions, checking logic | Slower; still needs checking |
| Small / local open-weight model | Working with sensitive material offline | Lower quality, technical set-up |
| Image / diagram models | Illustrations, infographics | Copyright, stereotypes, technical accuracy |
| Speech models | Text-to-speech, transcription, language practice | Voice data, accessibility benefits |
| Specialised educational tools | Adaptive practice, tutoring, assessment | Evidence of effectiveness, EU AI Act risk level |

## 3. Agentic AI

**Agentic AI** describes systems that pursue a goal with some autonomy: they **plan**, use **tools**, keep **memory** and **adapt** based on results.

``` ascii
        ┌──────────── Goal (set by human) ────────────┐
        ▼                                             │
     PLAN ──► ACT (tools: search, files, code) ──► OBSERVE ──► ADJUST
        ▲                                             │
        └──────────── memory / context ◄──────────────┘
                     │
               Human checkpoint
```

| Opportunities for TVET and professional development | Risks |
| --- | --- |
| Personalised learning paths and practice partners | Errors propagate across steps |
| Automating routine work (formatting, material search) | Lack of transparency: why did the agent do this? |
| Teacher assistants for planning and differentiation | Over-reliance, de-skilling of teachers |
| Support for continuous professional development | Data protection, security (prompt injection) |

**Principle:** keep a **human in the loop** at every step where pedagogical or high-stakes decisions are made.

**Check:** Which feature is typical for an AI agent but not for a single chat answer?

- [( )] It produces text.
- [(X)] It executes several steps and uses tools to reach a goal.
- [( )] It is always more accurate.

## 4. Mapping an AI-Enhanced Pedagogical Workflow

Describe each step with **who** does it (human / AI), **what tool**, and **which check**.

| Step | Who | Tool | Check |
| --- | --- | --- | --- |
| 1 Define learning objective (UNESCO) | Human | Framework | Is it measurable? Level? |
| 2 Collect and verify sources | Human + AI | Consensus, library | Sources exist and fit? |
| 3 Draft structure / content | AI | LLM + template | Matches objective? |
| 4 Fact check | Human | Primary sources | Errors removed? |
| 5 Didactic revision | Human | Bloom, AI-TPACK | Activating? Target group? |
| 6 Interactive elements | AI + human | LLM, LiaScript | Quiz quality, feedback |
| 7 Test & publish | Human | LiveEditor, GitHub | Renders? Licence? |
| 8 Evaluate | Human + learners | Feedback, quiz data | What to improve? |

**Group task (30 min):** Draw this workflow for **your** topic (ASCII, Mermaid, LucidChart or paper photo). Mark where AI is used and where you deliberately do *not* use AI.

## 5. Choosing Your Learning Objective

Open the **UNESCO AI Competency Framework for Teachers** (UNESCO, 2024) and look at competencies **3 (AI foundations and applications)**, **4 (AI pedagogy)** and **5 (AI for professional development)**.

**Criteria for a good choice**

- relevant for a concrete TVET target group,
- can be shown across Acquire – Deepen – Create,
- realistic to illustrate with sample material in 20 minutes,
- your group finds it interesting.

Use the **exact wording** of the framework and cite it. Do not let an AI invent competency numbers.

## 6. The Competency Matrix

The matrix shows how your learning objective develops over the three levels.

| Level | Content (what?) | Workflow (how do learners/teachers work?) | AI tool (with which support?) |
| --- | --- | --- | --- |
| **Acquire** | Basic concepts | Guided, step by step | e.g. explanation chatbot, quiz |
| **Deepen** | Application to cases | Problem-based, collaborative | e.g. case generator, feedback tool |
| **Create** | Own products / transfer | Project, design | e.g. agent or workflow the learners design |

**Check:** On which level do learners design their own AI-supported products or workflows?

- [( )] Acquire
- [( )] Deepen
- [(X)] Create

## 7. Hand-in for Session 2 (group)

**Deadline: 16.12.2026, 23:59 · Moodle · one upload per group**

1. **Learning objective:** UNESCO competency, exact wording and source; target group (3–5 sentences).
2. **First draft of the competency matrix** (table as in section 6).
3. **Workflow map** from section 4.
4. **Short AI tools log** of the group (tool, purpose, prompt, what you changed).

We discuss your drafts in the live session on **17.12.2026**.

## References

- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. In *Advances in Neural Information Processing Systems 33*. https://arxiv.org/abs/2005.11401
- Ning, Y., Zhang, C., Xu, B., Zhou, Y., & Wijaya, T. T. (2024). Teachers’ AI-TPACK: Exploring the relationship between knowledge elements. *Sustainability, 16*(3), 978. https://doi.org/10.3390/su16030978
- UNESCO. (2024). *AI competency framework for teachers*. https://doi.org/10.54675/ZJTE2084
- Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. In *International Conference on Learning Representations (ICLR 2023)*. https://arxiv.org/abs/2210.03629

<small>Licence: CC BY 4.0 · Hannes Tegelbeckers, OVGU Magdeburg · Created with AI support (Claude), checked and revised by the author.</small>

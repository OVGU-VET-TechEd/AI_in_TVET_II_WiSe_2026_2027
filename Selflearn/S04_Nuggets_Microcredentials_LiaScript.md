<!--
author:    Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   1.0.0
language:  en
narrator:  UK English Female
mode:      Textbook

title:     S04 – Designing self-learning nuggets and micro-credentials with LiaScript (Self-learning unit)
comment:   AI in TVET II – Self-learning unit for session 4 (live, 07.01.2027): learning nuggets and micro-credentials, Acquire–Deepen–Create progression, competency matrix workshop, LiaScript for sample material and the 20-minute group presentation.
-->

# S04 – Designing Self-Learning Nuggets and Micro-credentials with LiaScript

> **Session 4 · 07.01.2027 · 🟢 Live · Competency matrix workshop** – bring your matrix draft from S02/S03. This unit is also your reference for building the group presentation.
>
> **Time needed:** about 2 hours

**After this unit you will be able to …**

1. explain how learning nuggets stack into a micro-credential,
2. finalise a competency matrix across Acquire – Deepen – Create,
3. build sample learning material in LiaScript with AI support,
4. structure your 20-minute group presentation.

## 1. Nuggets and Micro-credentials

``` ascii
 Micro-credential  (EU approach: outcomes, workload, assessment, QA …)
 ├─ Acquire  ─ Nugget 1 · Nugget 2         understand concepts
 ├─ Deepen   ─ Nugget 3 · Nugget 4         apply in cases
 └─ Create   ─ Nugget 5                    design own product
```

| Learning nugget | Micro-credential |
| --- | --- |
| 5–15 minutes, one learning objective | Small volume of learning, several outcomes |
| Interactive element + short check | Assessment against transparent criteria |
| Can be reused in other contexts | Recorded and recognised (e.g. digital badge) |

The European approach (Council of the European Union, 2022) defines mandatory elements of a micro-credential, e.g. learning outcomes, notional workload, level, type of assessment and quality assurance. You already know this from AI in TVET I.

**For your group presentation:** you do not need to build all nuggets. Show the **design** (matrix, nugget plan) and **one piece of sample material**.

## 2. The Competency Matrix Workshop (live)

### Step 1 – Check your learning objective

- Exact UNESCO wording and source?
- Action verb that can be observed?
- Concrete TVET target group?

### Step 2 – Complete the matrix

| Level | Content | Workflow | AI tool | Assessment / feedback | Human decision |
| --- | --- | --- | --- | --- | --- |
| **Acquire** | | | | | |
| **Deepen** | | | | | |
| **Create** | | | | | |

### Step 3 – Peer check (10 min per group)

Another group checks your matrix with three questions:

1. Is the progression visible (does each level build on the previous one)?
2. Do content, workflow and AI tool fit together on each level?
3. Where is the human role clear – and where is AI used just because it is possible?

**Check:** Which sequence describes a coherent progression?

- [( )] Learners design an AI workflow → learn basic terms → apply them in a case
- [(X)] Learners learn basic terms → apply them in a case → design their own AI-supported product
- [( )] Learners only take quizzes on all three levels

## 3. Sample Material with AI and LiaScript

### Prompt template for a nugget section

```text
You are an instructional designer for vocational education.
Create a LiaScript section (mode: Textbook) for this learning objective:
"<UNESCO learning objective, exact wording>" – level: <Acquire | Deepen | Create>.
Target group: <…>. Language: English, B1–B2.
Include: workplace scenario (max. 120 words), explanation with a table or ASCII
diagram, 2 single-choice items (- [( )] / - [(X)]) with hints ([[?]]),
1 reflection task, summary in 3 bullets.
Do not invent sources or statistics; mark gaps with <!-- CHECK -->.
Never indent text by 4 or more spaces.
```

### LiaScript elements worth showing in your presentation

| Element | Syntax | Pedagogical purpose |
| --- | --- | --- |
| Step-by-step reveal | `{{1}}` before a block | Guide attention, reduce cognitive load |
| Speaker note / TTS | `--{{0}}--` | Accessibility, self-paced learning |
| Single / multiple choice | `- [(X)]`, `- [[X]]` | Retrieval practice with feedback |
| Text input | `[[answer]]` | Recall of key terms |
| Hint | `[[?]] hint` | Scaffolding |
| Survey | `- [(1)] option` | Activate prior knowledge, discussion |
| Video | `!?[title](url)` | Demonstration of workplace procedures |
| ASCII diagram | code block marked `ascii` | Processes and workflows |

### Quality checklist for AI-generated material

- [ ] Factually correct and sources checked
- [ ] Aligned with the learning objective and level
- [ ] Authentic for the vocational field
- [ ] Activating (learners have to think, not only read)
- [ ] Inclusive language and examples, no stereotypes
- [ ] Renders correctly in LiaScript
- [ ] Licence (e.g. CC BY 4.0), image credits and AI declaration

## 4. Structuring the 20-Minute Group Presentation

Use the presentation template from the course website. A possible timing:

| Part | Content | Time |
| --- | --- | --- |
| 1 | Introduction: group, topic, why this learning objective matters | 2 min |
| 2 | Learning objective and target group | 2 min |
| 3 | Competency matrix: Acquire – Deepen – Create | 5 min |
| 4 | Sample learning material, shown live (with interactive element for the audience) | 6 min |
| 5 | AI workflow: tools, prompts, what you checked and changed | 3 min |
| 6 | Lessons learned, references, licence | 2 min |
| | **Discussion** | 5 min |

**Tip:** Split the parts among group members, but rehearse once together with a timer.

## 5. Until Next Week

- Build your presentation in the shared repository.
- Prepare the sample material and test it in LiaScript.
- On **14.01.2027** (🔵 self-learning) you exchange drafts with another group for peer review – see unit S05.

## References

- Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's taxonomy of educational objectives*. Longman.
- Council of the European Union. (2022). *Council Recommendation of 16 June 2022 on a European approach to micro-credentials for lifelong learning and employability* (2022/C 243/02). https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022H0627(02)
- LiaScript. (n.d.). *LiaScript documentation*. https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md
- UNESCO. (2019). *Recommendation on Open Educational Resources (OER)*. https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer
- UNESCO. (2024). *AI competency framework for teachers*. https://doi.org/10.54675/ZJTE2084

<small>Licence: CC BY 4.0 · Hannes Tegelbeckers, OVGU Magdeburg · Created with AI support (Claude), checked and revised by the author.</small>

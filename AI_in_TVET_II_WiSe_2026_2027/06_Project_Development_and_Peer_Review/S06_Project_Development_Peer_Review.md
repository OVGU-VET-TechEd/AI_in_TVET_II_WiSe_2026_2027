<!--
author:    Dr. Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   2.1.0
language:  en
narrator:  UK English Female
mode:      Textbook

title:     S06 – Project development and peer review (Self-learning unit)
comment:   AI in TVET II – Self-learning unit for session 6 (14.01.2027, format to be confirmed: live or self-learning): finalising the group presentation, structured written peer review of another group's draft, final quality check, revision plan, reflection on the human role in AI-supported design. Obligatory SCORM unit with group hand-in.
-->

# S06 – Project Development and Peer Review

> **Session 6 · 14.01.2027 · ⚪ Format to be confirmed** – live in the room or self-learning (announced in Moodle). The tasks are the same in both cases; work in your group.
>
> **Time needed:** about 3 hours
>
> **📦 Obligatory:** completing this unit [in Moodle (SCORM)](https://elearning.ovgu.de/course/section.php?id=202215) is part of the pass requirement – all 7 units by **15.02.2027**.
>
> **📤 Group hand-in inside this unit: 18.01.2027, 23:59** – see chapter 5. Every group member submits the group result in their own unit.

**After this unit you will be able to …**

1. give structured, criteria-based feedback on another group's presentation draft – as a GitHub issue with concrete change suggestions,
2. use peer feedback to plan concrete revisions of your own presentation,
3. check sample material, references and licences systematically,
4. reflect on the balance between automation and human-centred pedagogy in your design.

## 1. Plan for Today

The peer review only works if every draft is online on time. The pairing of review partners is published in Moodle.

<!-- data-type="none" -->
| Time | Activity |
| --- | --- |
| 0:00–0:45 | Finish your presentation draft and push it to GitHub |
| 0:45–1:00 | Send the LiaScript link to your peer-review partner group (pairing in Moodle) |
| 1:00–2:00 | Review the partner group's draft with the rubric (chapter 3) |
| 2:00–2:10 | Break |
| 2:10–2:35 | Discuss the feedback you received and plan revisions |
| 2:35–3:00 | Reflection and hand-in in this unit |

## 2. How to Give Good Peer Feedback

Feedback is useful when the receiver knows what to keep and what to change. The three feedback questions of Hattie and Timperley (2007) give it a structure:

1. **Where are they going?** – Are the learning objective and the goal of the presentation clear?
2. **How are they going?** – What already works? What is missing or unclear?
3. **Where to next?** – Which 2–3 concrete changes would improve it most?

**Rules**

- Be specific: refer to slides or sections.
- Be constructive: "You could …" instead of "This is bad".
- Prioritise: the three most important points first.
- You may use AI to *structure* your feedback, but the judgement must be your own – and declared.

**Check:** useful or not useful feedback?

<!-- data-hint-button="1" data-solution-button="2" data-show-partial-solution -->
[(useful) (not useful)]
[  ( )        (X)      ] "Nice presentation, well done!"
[  (X)        ( )      ] "Slide 5: the Deepen level repeats the Acquire content. You could add a case where learners check a chatbot answer."
[  ( )        (X)      ] "The matrix is bad."
[  (X)        ( )      ] "Your workflow slide does not show where a human checks the AI draft – add the fact-check step."

## 3. Peer-Review Rubric

The rubric uses the same criteria as the assessment of your own presentation. Rate each criterion: **++** convincing · **+** mostly there · **–** needs work, and add one comment per criterion.

<!-- data-type="none" -->
| Criterion | Guiding question | Rating | Comment |
| --- | --- | --- | --- |
| **Learning objective** | Exact UNESCO wording, competency and target group clear? | | |
| **Competency matrix** | Progression Acquire → Deepen → Create visible and consistent? | | |
| **Sample material** | Fits the objective and level? Activating? Correct? | | |
| **AI workflow** | Tools, prompts and human revisions transparent? | | |
| **Human-centred design** | Clear where humans decide and where AI is deliberately not used? | | |
| **LiaScript use** | Slides, step-by-step reveal, at least one interactive element, renders correctly? | | |
| **Sources and licence** | References (APA 7) correct and verifiable? Licence, image credits, AI declaration? | | |
| **Timing** | Realistic for 20 minutes? | | |

**Overall:** the three most important recommendations, in order of priority.

### Review on GitHub

In AI in TVET I the panel gave oral feedback after the pitch. In AI in TVET II the review is **written and traceable, where the work lives**: in the partner group's repository.

- Open an **issue** in the partner group's repository with your complete review (template below) and the **pinned link** of the version you reviewed.
- For small concrete fixes (a broken quiz, a missing alt text) propose a **change via pull request** – the authors accept or reject it.
- The authors answer every point: *accepted · changed differently · not changed, because …* – this is your revision plan.

```markdown
## Peer review by <group>
**Pinned link reviewed:** <link with commit hash>

| Criterion | Rating (++ / + / –) | Comment (slide no.) |
| --- | --- | --- |
| Learning objective | | |
| Competency matrix | | |
| Sample material | | |
| AI workflow | | |
| Human-centred design | | |
| LiaScript use | | |
| Sources and licence | | |
| Timing | | |

### Top 3 recommendations
1. …
```

### Optional: an AI as additional reviewer

You may ask an AI tool for a critical review – read it as one more opinion, not as a verdict, and declare it.

```text
Act as a critical reviewer for a 20-minute teacher-training presentation.
Use only these criteria: <paste the rubric>. For each criterion, quote the slide
you refer to, name one strength and one concrete improvement. Do not rewrite
the presentation. Mark every statement you are unsure about.
Presentation: """<paste the .md file>"""
```

## 4. Final Quality Check

Check your **own** presentation as strictly as your partner's. These are the most frequent problems in the final presentations of earlier cohorts:

- [ ] **Renders:** opened via the LiaScript link, no `[[`, `{{` or `-->` visible, every quiz works
- [ ] **References:** every DOI opens at [doi.org](https://doi.org); claims checked with [Consensus](https://consensus.app) or the library
- [ ] **AI declaration** and **licence line** on the last slide; third-party material credited with TASL
- [ ] **Accessibility:** alt text for images, speaker notes, readable contrast
- [ ] **Facts:** no invented statistics, no unchecked safety rules
- [ ] **Timing:** rehearsed once with a timer – 20 minutes

### Reflection

Answer as a group (5–8 sentences) and connect your answer to one framework from the seminar – the human-centred AI lens (Schmager et al., 2025), the heutagogy paradigms (Ng & Lai, 2025) or the four key considerations of the European Commission (2022):

- Which part of your design would not work without human expertise?
- Where did AI save time – and where did it cost time (checking, correcting)?
- What would you change if learners used your material without a teacher?

## 5. Group Hand-in for Session 6

**Deadline: 18.01.2027, 23:59 · inside this unit** – every group member enters the **same group result** in their own unit and submits it.

### Part 1: written peer review

**Link to your review issue in the partner group's repository, and the three most important recommendations:**

[[___ ___ ___ ___ ___]]

### Part 2: revision plan

**Which feedback did you receive, and what will you change by 20.01.? (bullet points)**

[[___ ___ ___]]

### Part 3: reflection

**Your group's reflection (5–8 sentences, with a framework):**

[[___ ___ ___ ___]]

### Part 4: link

**LiaScript link to your current presentation draft:**

[[___]]

**Presentation file (link in Moodle): 20.01.2027, 23:59** · **Final presentations: 21.01.2027** (20 minutes + 5 minutes discussion per group).

## Summary and Self-Check

- Useful feedback names the place, the problem and a possible next step – structured by *where to, how, where next*.
- The peer-review rubric uses the same criteria as the final assessment.
- A final quality check covers rendering, references, licences, accessibility, facts and timing.
- Reflection connects your experience with a framework – and names what must stay human.

**Tick what you can do now:**

- [ ] I gave specific, prioritised feedback with the rubric.
- [ ] Our group has a revision plan based on the feedback we received.
- [ ] Our presentation passed the final quality check.
- [ ] Our reflection names what must stay human – and why.

**Next session:** Thursday, 21.01.2027, 🟢 live – final group presentations and reflection.

## References

- European Commission. (2022). *Ethical guidelines on the use of artificial intelligence (AI) and data in teaching and learning for educators*. Publications Office of the European Union. https://data.europa.eu/doi/10.2766/153756
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. https://doi.org/10.3102/003465430298487
- Ng, S. H. S., & Lai, J. W. (2025). AI-augmented heutagogy: A framework for fostering self-determined learning and agency in higher education. *Higher Education Research & Development*. https://doi.org/10.1080/07294360.2025.2564977
- Schmager, S., Pappas, I. O., & Vassilakopoulou, P. (2025). Understanding human-centred AI: A review of its defining elements and a research agenda. *Behaviour & Information Technology, 44*(15), 3771–3810. https://doi.org/10.1080/0144929X.2024.2448719
- UNESCO. (2024). *AI competency framework for teachers*. https://doi.org/10.54675/ZJTE2084

<small>Licence: CC BY 4.0 · Dr. Hannes Tegelbeckers, OVGU Magdeburg · Created with AI support (Claude), checked and revised by the author.</small>

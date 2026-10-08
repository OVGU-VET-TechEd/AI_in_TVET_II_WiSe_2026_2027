<!--
author:    Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   1.0.0
language:  en
narrator:  UK English Female
mode:      Textbook

title:     S01 – Introduction to AI & Prompting: refresher for AI pedagogy (Self-learning unit)
comment:   AI in TVET II – Self-learning unit for session 1 (live, 03.12.2026): LLMs, grounding and agents, prompt patterns for learning material, LiaScript generation workflow, group formation and assessment.
-->

# S01 – Introduction to AI & Prompting: Refresher for AI Pedagogy

> **Session 1 · 03.12.2026 · 🟢 Live** – this unit accompanies the kick-off. It refreshes AI in TVET I and goes one step further: from *using* AI to *designing learning material* with AI.
>
> **Time needed:** about 75 minutes

**After this unit you will be able to …**

1. explain how LLMs, retrieval (grounding) and agents differ,
2. use prompt patterns to generate learning material (quizzes, cases, diagrams, LiaScript),
3. describe a quality-assured workflow from prompt to published learning material,
4. organise your group and plan the 20-minute group presentation.

## 1. Refresher: How LLMs Work

| Concept | Short explanation | Why it matters for learning material |
| --- | --- | --- |
| **Tokens** | Text is processed in small units | Long documents may exceed the limit |
| **Weights** | Billions of learned numbers encode patterns from training data | Knowledge is statistical, not checked |
| **Probabilities** | The next token is chosen by likelihood | Plausible ≠ correct → verify |
| **Training data / cut-off** | Knowledge ends at a certain date | New standards or regulations may be missing |
| **Context window** | Everything the model "sees" in one conversation | Provide your curriculum text, learning outcomes, examples |

**Check:** Why should you give an LLM your own course text when generating a quiz?

- [( )] Because LLMs cannot write quizzes otherwise.
- [(X)] Because the output is then grounded in material you have checked, which reduces errors.
- [( )] Because it makes the answer shorter.

## 2. Beyond the Chat: Grounding and Agents

``` ascii
 Plain LLM            LLM + retrieval (RAG)              Agent
 ─────────            ─────────────────────              ─────
 Prompt ─► Answer     Prompt ─► search your docs ─►      Goal ─► plan ─► use tools
                      Answer with sources                 (search, files, code)
                                                          ─► check ─► next step
```

- **Retrieval-augmented generation (RAG):** the system first searches documents (your files, the web, a database) and uses the found passages to answer. Examples: NotebookLM, Perplexity, file upload in chat tools (Lewis et al., 2020).
- **Agents:** an LLM that plans several steps, calls tools and works towards a goal with limited supervision, e.g. "research three sources, draft a lesson plan, create the quiz file". More autonomy means more need for human checks.

## 3. Prompt Patterns for Learning Material

| Material | Pattern | Example prompt (short) |
| --- | --- | --- |
| Learning objectives | Template + Bloom | "Formulate 3 learning objectives with Bloom verbs (levels 2–4) for …" |
| Quiz | Persona + template + grounding | "As a trainer, create 5 single-choice items from the attached text. Format: LiaScript `- [( )]`. Add feedback." |
| Case / scenario | Audience persona + constraints | "Write a realistic workplace case for apprentices in logistics, 150 words, with one decision point." |
| Diagram | Output format | "Draw the process as an ASCII diagram / Mermaid code." |
| Differentiation | Variation | "Create the same task in three difficulty levels." |
| Quality check | Reflection / fact check | "List all factual claims and mark which ones need a source." |

**Practice (15 min):** Take a learning objective you might work on. Generate (1) a short case and (2) three quiz items with an AI tool. Then apply the *fact check* pattern. Keep the result – you can reuse it in your group presentation.

## 4. Workflow: From Prompt to OER

``` ascii
 1 Learning objective ─► 2 Collect sources ─► 3 Prompt with template ─►
 4 AI draft ─► 5 Fact check ─► 6 Didactic revision ─► 7 LiaScript test ─►
 8 Licence + AI declaration ─► 9 Publish on GitHub
```

**Human responsibility:** You are responsible for the factual and didactic quality of everything you present – not the AI.

**Limitations to watch for in learning material**

- fabricated references and statistics,
- didactically weak output (correct but not activating),
- bias and stereotypes in cases and images,
- missing national or sector-specific context,
- broken LiaScript syntax (test in the LiveEditor).

## 5. Ethics in Short

- **Data protection:** no personal data of learners or colleagues in AI tools.
- **Copyright:** purely AI-generated content is generally not protected by copyright; your selection and revision can be. Check tool terms, licence your work openly (e.g. CC BY 4.0), credit images.
- **Transparency:** declare AI use.
- **Human-centred pedagogy:** decide consciously where AI supports learning and where learners must think themselves.

## 6. Your Task in This Seminar

**Group work.** Each group prepares a **20-minute LiaScript presentation** (+ 5 minutes discussion) on 21.01.2027 for **one learning objective** from the UNESCO AI Competency Framework for Teachers:

- Competency 3 – AI foundations and applications
- Competency 4 – AI pedagogy
- Competency 5 – AI for professional development

The presentation contains:

1. the chosen learning objective and target group,
2. a **competency matrix** across *Acquire – Deepen – Create* (content, workflow, AI tool),
3. **sample learning material** created with AI (e.g. a short nugget section, case or quiz), shown live,
4. your **AI workflow** and what you changed as humans,
5. lessons learned, references, licence and AI declaration.

A complete, stand-alone self-learning course is **not** required.

**Today:**

- [ ] form your group and agree on a working mode,
- [ ] create a shared GitHub repository (e.g. `AI_in_TVET_II_<topic>`) and add all members,
- [ ] look at the presentation template (course website),
- [ ] shortlist 2–3 possible learning objectives.

## References

- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. In *Advances in Neural Information Processing Systems 33* (NeurIPS 2020). https://arxiv.org/abs/2005.11401
- Lo, L. S. (2023). The CLEAR path: A framework for enhancing information literacy through prompt engineering. *The Journal of Academic Librarianship, 49*(4), 102720. https://doi.org/10.1016/j.acalib.2023.102720
- UNESCO. (2023). *Guidance for generative AI in education and research*. https://doi.org/10.54675/EWZM9535
- UNESCO. (2024). *AI competency framework for teachers*. https://doi.org/10.54675/ZJTE2084
- White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., & Schmidt, D. C. (2023). *A prompt pattern catalog to enhance prompt engineering with ChatGPT* (arXiv:2302.11382). https://arxiv.org/abs/2302.11382

<small>Licence: CC BY 4.0 · Hannes Tegelbeckers, OVGU Magdeburg · Created with AI support (Claude), checked and revised by the author.</small>

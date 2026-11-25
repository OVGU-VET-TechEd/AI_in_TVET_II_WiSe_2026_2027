<!--
author:    Dr. Hannes Tegelbeckers
email:     hannes.tegelbeckers@ovgu.de
version:   2.1.0
language:  en
narrator:  UK English Female
mode:      Textbook

title:     S04 – Pedagogical trends, AI tools for assessment and feedback, ethics in AI pedagogy (Self-learning unit)
comment:   AI in TVET II – Self-learning unit for session 4 (live, 17.12.2026): labour-market trends, AI-TPACK, personalisation, AI-augmented heutagogy and self-regulated learning; AI for formative and summative assessment and feedback; evaluating AI assessment tools; cognitive offloading, bias, privacy, EU AI Act and the human-centred mindset. Obligatory SCORM unit.
-->

# S04 – Pedagogy, Assessment and Ethics in AI-Supported TVET

> **Session 4 · 17.12.2026 · 🟢 Live** – this unit accompanies the live session. Read chapters 1–3 before or after the session; chapter 5 applies everything to your group project.
>
> **Time needed:** about 2 hours
>
> **Builds on AI in TVET I** (session 4: AI-TPACK, heutagogy, tool evaluation · session 2: ethics, EU AI Act) – applies these to your own design instead of repeating them.
>
> **📦 Obligatory:** completing this unit [in Moodle (SCORM)](https://elearning.ovgu.de/course/section.php?id=202215) is part of the pass requirement – all 7 units by **15.02.2027**.

**After this unit you will be able to …**

1. apply pedagogical trends (AI-augmented heutagogy, self-regulated learning, evidence on learning vs. performance) to your competency matrix,
2. design AI-supported formative feedback for a TVET learning objective,
3. evaluate the reliability of AI grading with a mini-study and decide where AI may support assessment,
4. co-create ethical rules for AI use in your learning design and justify the human role.

## 1. Pedagogical Trends

AI changes vocational education on two sides: it changes the **work** that learners are prepared for, and it changes **how** they learn. Both matter for your design.

### Why AI pedagogy matters in TVET

The [Job-Futuromat](https://job-futuromat.iab.de) of the German Institute for Employment Research (IAB) estimates which share of the core tasks of an occupation could already be automated with current technology. Enter the occupation of your target group (German occupation names, e.g. *Mechatroniker/in*). If many routine tasks can be automated, apprentices need more of what machines do badly: diagnosing unusual faults, judging quality, communicating with customers – and working critically with AI.

**The occupation of our target group and the share of automatable core tasks – and what apprentices should learn *because of* that:**

[[___ ___]]

### AI-TPACK

TPACK describes the knowledge teachers need to combine **T**echnology, **P**edagogy and **C**ontent. **AI-TPACK** extends this to AI: knowing what AI can do, how it changes teaching methods and how it changes the subject content itself (Ning et al., 2024). Example: a welding trainer needs to know what an AI vision system can detect (technology), how to use its feedback in practice phases (pedagogy) and how quality standards change when such systems are used in companies (content).

### Personalisation and adaptive learning

AI adapts content, pace and feedback to learners. Reviews show benefits for engagement and performance when teachers orchestrate the use (du Plooy et al., 2024; Zhao & Ko, 2024).

The **OECD Digital Education Outlook 2026** adds an important warning: with general-purpose chatbots, students produce better work – but the advantage disappears, or even reverses, when access is removed in exams. Tools designed or used with a clear pedagogical purpose show more lasting learning gains (OECD, 2026). **Performance with AI is not the same as learning.**

### Heutagogy: self-determined learning

Heutagogy puts the learner in charge of *what* and *how* to learn – up to the design of curriculum and assessment. Ng and Lai (2025) propose **AI-augmented heutagogy** and map three AI paradigms to rising learner autonomy and the SOLO taxonomy:

<!-- data-type="none" -->
| AI paradigm | Role of AI | SOLO level | Learner autonomy | TVET example |
| --- | --- | --- | --- | --- |
| **AI-informed** | Information, identifying learning needs | Pre-/uni-structural | Low – teachers guide strongly | An apprentice asks a chatbot to explain Ohm's law; the trainer sets tasks |
| **AI-supported** | Adaptive feedback, tailored content, recommendations | Multi-structural, relational | Growing | Practising fault diagnosis with adaptive hints |
| **AI-empowered** | Partner for complex, open-ended problems | Extended abstract | Full autonomy and agency | A team designs an energy-saving concept with AI as sparring partner |

AI's computational strengths should complement the emotional and ethical dimensions of human cognition. The authors stress that this requires deliberate changes in pedagogy and assessment, staff development and infrastructure.

You met these paradigms in AI in TVET I. Now **apply** them: which paradigm fits each level of **your** competency matrix? Learner autonomy should rise from Acquire to Create.

**Acquire level – AI paradigm:** <script input="select" options="AI-informed|AI-supported|AI-empowered" value="AI-informed" output="h1">`@input`</script>

**Deepen level – AI paradigm:** <script input="select" options="AI-informed|AI-supported|AI-empowered" value="AI-supported" output="h2">`@input`</script>

**Create level – AI paradigm:** <script input="select" options="AI-informed|AI-supported|AI-empowered" value="AI-supported" output="h3">`@input`</script>

<script modify="false" style="display:block">
const rank = {"AI-informed":1,"AI-supported":2,"AI-empowered":3};
const solo = {1:"pre-/uni-structural",2:"multi-structural, relational",3:"extended abstract"};
const v = [`@input(`h1`)`,`@input(`h2`)`,`@input(`h3`)`].map(x => rank[`${x}`.trim()] || 1);
const lv = ["Acquire","Deepen","Create"];
const rows = v.map((x,i) => `<li><b>${lv[i]}</b>: ${Object.keys(rank)[x-1]} · SOLO ${solo[x]}</li>`).join("");
const tips = [];
if (v[0] > v[1] || v[1] > v[2]) tips.push("📉 Autonomy decreases somewhere – learners should gain agency from level to level.");
if (v[2] < 3) tips.push("🎯 At <b>Create</b>, learners should use AI as a partner for open problems (AI-empowered) – otherwise the top level stays teacher-led.");
if (v[0] === 3) tips.push("⚠️ AI-empowered already at <b>Acquire</b> overloads novices – they need guidance first.");
`HTML: <ul>${rows}</ul><p>${tips.length ? tips.join("<br>") : "✅ Learner autonomy rises from Acquire to Create – the heutagogy progression fits your matrix."}</p>`
</script>

**Your paradigms per level – and how learners move from one to the next:**

[[___ ___]]

### Self-regulated learning (SRL)

AI chatbots can support the SRL cycle – **goal setting, monitoring, feedback, reflection** – if they are designed to ask questions rather than give answers (Chang et al., 2023). A system prompt for such a coach could look like this:

```text
You are a learning coach for apprentices. Never give the full solution.
1) Ask the learner for their goal for this task.
2) Ask what they have tried so far.
3) Give one hint at a time, then ask them to try again.
4) At the end, ask: "What will you do differently next time?"
```

**Check:** Which design supports self-regulated learning best?

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] A chatbot that immediately provides complete solutions.
- [(X)] A chatbot that asks the learner for a goal, gives hints and prompts reflection.
- [( )] A chatbot that grades every answer without explanation.
[[?]] Who does the thinking in each design?
***
The coach keeps the thinking with the learner: goal, attempt, hint, retry, reflection – the SRL cycle.
***

## 2. AI for Assessment and Feedback

Assessment answers the question *how do we know learners reached the objective?* AI can help on the way – but the role it may play depends on the purpose.

### Formative vs. summative

<!-- data-type="none" -->
| | Formative | Summative |
| --- | --- | --- |
| Purpose | Support learning | Certify achievement |
| Timing | During learning | At the end |
| AI role | Generate tasks, give immediate feedback, adapt practice | Support only; humans decide |
| Risk | Over-reliance, generic feedback | Unfair or wrong decisions; high risk under the EU AI Act |

### Good feedback

Effective feedback answers three questions (Hattie & Timperley, 2007): **Where am I going?** (goal) · **How am I going?** (progress) · **Where to next?** (next steps). Use these as a template when you prompt AI for feedback.

```text
Give feedback to an apprentice on the following fault-diagnosis report.
Structure: (1) goal of the task, (2) what is already correct, (3) one or two
concrete next steps. Do not give the full solution. Max. 120 words.
Report: """<paste report>"""
```

### What does research say?

- In a randomised field experiment with blinded feedback sources (N = 90), students rated LLM and peer feedback as fairer and easier to accept than teacher feedback – but **teacher feedback produced the strongest improvement** in the quality of their work, and LLM feedback the smallest (Weidlich et al., 2025).
- LLM grading of exams can deviate considerably from human grading (Flodén, 2025); the acceptance of AI grading depends on perceived fairness (Jones-Jang et al., 2025).
- Teachers' own value judgements also change when they know work was AI-assisted (Luo & Dawson, 2025).

**Check:** What follows from Weidlich et al. (2025)?

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] Replace teacher feedback with AI feedback – students like it more.
- [(X)] Use AI feedback as an addition, but keep teacher feedback where improvement matters most.
- [( )] Never use AI feedback.
[[?]] Acceptance and effect are not the same.

### Feedback lab

Read this fictitious report of an apprentice:

> *"The machine stopped. I think the motor is broken because it made a noise. I changed the fuse but it did not help. Then I called the master."*

1. Write **your own** feedback (max. 80 words).
2. Let an AI tool write feedback with the prompt above.
3. Compare: which feedback is more specific, more motivating, more correct?

**Your feedback, and the biggest difference to the AI's feedback:**

[[___ ___ ___]]

### AI-supported assessment in practice

<!-- data-type="none" -->
| Task | AI support | Human check |
| --- | --- | --- |
| Item generation | Quiz items from your verified text | Correctness, difficulty, distractors |
| Rubric design | Draft criteria and levels | Alignment with learning objective |
| Formative feedback | First feedback draft | Tone, accuracy, next steps |
| Competency-based task | Workplace scenario variants | Authenticity, safety |
| Summative decision | none / analysis only | **Teacher decides** |

**Check:** Under the EU AI Act, AI systems used to evaluate learning outcomes are …

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] minimal risk
- [(X)] high risk
- [( )] always prohibited
[[?]] Annex III of the regulation lists education and vocational training.
***
AI systems intended to evaluate learning outcomes or steer the learning process are listed as high-risk in Annex III of the AI Act – with obligations for human oversight, transparency and data quality.
***

## 3. Can AI Grade Your Learners? A Mini-Study

In AI in TVET I you discussed whether you would let an AI grade your work and evaluated AI tools with a general grid. Here you go one step further and **test** an AI grader with your own material. Research shows that LLM grades can deviate considerably from human grades (Flodén, 2025) – but how large is the problem for *your* topic?

**Procedure (20 min):**

1. Write **three short learner answers** for a task of your topic – one good, one medium, one weak – and a **three-level rubric**.
2. Let an AI grade each answer **twice**, each time in a new chat with the same prompt (rubric + answer).
3. Grade the answers **yourself** before you look at the AI grades.

Enter your counts:

**Answers graded:** <script input="range" min="1" max="10" step="1" value="3" output="ga">@input</script>

**AI run 1 = AI run 2 (same grade):** <script input="range" min="0" max="10" step="1" value="2" output="gb">@input</script>

**AI = your grade (exactly):** <script input="range" min="0" max="10" step="1" value="1" output="gc">@input</script>

**AI = your grade (± one level):** <script input="range" min="0" max="10" step="1" value="2" output="gd">@input</script>

<script modify="false" style="display:block">
const n = +@input(`ga`), self = Math.min(+@input(`gb`), n), ex = Math.min(+@input(`gc`), n), adj = Math.max(Math.min(+@input(`gd`), n), ex);
const p = x => Math.round(100 * x / n);
const bar = (x, l) => `<div style="margin:3px 0"><span style="display:inline-block;width:190px">${l}</span><span style="display:inline-block;height:14px;width:${p(x)*2.4}px;background:${p(x) >= 80 ? "#2e7d32" : (p(x) >= 60 ? "#b7791f" : "#d03b3b")};border-radius:3px"></span> <b>${p(x)} %</b></div>`;
const verdict = p(self) < 80 ? "🔴 The AI does not even agree with itself – not usable for grading, at most for first feedback drafts." : (p(ex) < 70 ? "🟡 Consistent, but different from your judgement – use for formative feedback only, you decide on grades." : "🟢 Close to your judgement in this small sample – still: summative decisions stay with you (EU AI Act: high risk).");
`HTML: ${bar(self, "AI agrees with itself")}${bar(ex, "AI = you (exact)")}${bar(adj, "AI = you (± 1 level)")}<p>${verdict}</p><p><small>${n} answers – a mini-study, not a validation. Compare: Flodén (2025).</small></p>`
</script>

Two lessons: a grader that does not agree with itself cannot be valid; and even good agreement in three answers is no validation. Summative decisions stay with the teacher – AI systems that evaluate learning outcomes are high-risk under the EU AI Act.

**Your result and your rule – when may AI support assessment in your design, and when does the teacher decide?**

[[___ ___ ___]]

## 4. Ethics in AI Pedagogy

Ethics is not an extra chapter at the end of a design – it shapes the design. Three risks matter most for learning material.

### Cognitive offloading

If learners let AI do the thinking, learning can suffer:

- Higher AI tool use was associated with lower critical-thinking scores, mediated by cognitive offloading (Gerlich, 2025).
- In an essay-writing study, participants using an LLM showed lower brain connectivity and weaker recall of their own text than those writing without tools (Kosmyna et al., 2025, preprint).

**Design consequence:** plan phases *without* AI, ask learners to think first, and use AI as a sparring partner rather than a solution generator.

### Bias, privacy, accountability

- **Bias:** check cases, images and examples for stereotypes – the bias audit from S02 makes it measurable.
- **Privacy:** no personal learner data in external tools; prefer institutional licences or local models.
- **Accountability:** teachers remain responsible for grading and pedagogical decisions (UNESCO, 2024).
- **Transparency:** tell learners when and how AI is used.

### Ethical guidelines for educators

The European Commission (2022) names four key considerations for the ethical use of AI and data in teaching and learning:

<!-- data-type="none" -->
| Consideration | Question for your design |
| --- | --- |
| **Human agency** | Do learners and teachers stay in control of decisions about learning? |
| **Fairness** | Is everyone treated fairly – incl. language, disability, background? |
| **Humanity** | Are dignity, identity and well-being respected? |
| **Justified choice** | Can you justify *why* AI is used here – with evidence and transparency? |

### Co-creating ethical rules

In AI in TVET I you learned ethical **principles** – UNESCO CFT dimension 2 at the *Acquire* level. The *Create* level of the same dimension is **co-creating ethical rules**: teachers develop rules for AI use together with learners and colleagues. Draft an AI agreement for your learning design – then discuss and revise it with learners.

**Learners may use AI for:** <script input="select" options="explanations and hints only|drafts they revise and declare|everything except the assessed part" value="explanations and hints only" output="r1">`@input`</script>

**Phase without AI:** <script input="select" options="first attempt at every task|the practical skill check|none" value="first attempt at every task" output="r2">`@input`</script>

**Declaration:** <script input="select" options="one line: tool and purpose|AI log with prompts|no declaration" value="one line: tool and purpose" output="r3">`@input`</script>

**Data:** <script input="select" options="no personal or company data in AI tools|anonymised data only|any data" value="no personal or company data in AI tools" output="r4">`@input`</script>

**Feedback and grades:** <script input="select" options="AI drafts feedback - the trainer decides on grades|AI grades - the trainer checks samples" value="AI drafts feedback - the trainer decides on grades" output="r5">`@input`</script>

<script modify="false" style="display:block">
const g = k => `${k}`.trim();
const a = [g(`@input(`r1`)`), g(`@input(`r2`)`), g(`@input(`r3`)`), g(`@input(`r4`)`), g(`@input(`r5`)`)];
const w = [];
if (a[1] === "none") w.push("No phase without AI – risk of cognitive offloading (Gerlich, 2025).");
if (a[2] === "no declaration") w.push("No declaration – transparency and fairness suffer.");
if (a[3] === "any data") w.push("Any data – conflicts with data protection (GDPR) and the human-agency principle.");
if (a[4].startsWith("AI grades")) w.push("AI grades – high-risk use under the EU AI Act; requires human oversight of every decision.");
`HTML: <div style="border:2px solid #7a003f;border-radius:10px;padding:10px 14px;max-width:560px"><b>📜 Our AI agreement</b><ol><li>You may use AI for: ${a[0]}.</li><li>Without AI: ${a[1]}.</li><li>Declare AI use: ${a[2]}.</li><li>Data: ${a[3]}.</li><li>${a[4]}.</li></ol></div><p>${w.length ? "⚠️ " + w.join("<br>⚠️ ") : "✅ Consistent with the four key considerations – now discuss it with learners and revise it together."}</p>`
</script>

**Your AI agreement (final wording for your sample material):**

[[___ ___ ___]]

### The human-centred mindset

The UNESCO AI Competency Framework for Teachers places the **human-centred mindset** first: human agency, human accountability and social responsibility. Use it – together with the purpose–values–properties lens from session 2 – for every design decision in your project.

**Check:** A training company wants an AI tool to write the monthly progress reports on its apprentices automatically. Which safeguard matters most?

<!-- data-hint-button="1" data-solution-button="2" -->
- [( )] The reports are sent faster, so learners get more feedback.
- [(X)] The trainer reviews and signs every report; apprentices can see and comment on it.
- [( )] The AI is told to be positive, so no harm can occur.
[[?]] Human agency and accountability.
***
Reports influence an apprentice's future – a human must stay accountable, and learners must be able to see and contest what is written about them.
***

## 5. Apply to Your Group Project

Use your competency matrix from S03 and add two columns. Discuss them in your group.

<!-- data-type="none" -->
| Level | Assessment / feedback (how do we know learners reached it?) | Human decision / ethical safeguard (what without AI?) |
| --- | --- | --- |
| Acquire | | |
| Deepen | | |
| Create | | |

**Questions for your group**

1. Which pedagogical trend from chapter 1 fits your learning objective best – and why?
2. Where could AI make learners passive in your design? How do you prevent it?
3. Which piece of sample material will you show in your presentation?

**Your two new matrix columns (or the link to the file in your repository):**

[[___ ___ ___ ___]]

### Reflection

Write 5–8 sentences: *Where is the balance between automation and human-centred pedagogy in our design?* Use at least one of the frameworks of this unit (heutagogy paradigms, EC key considerations, UNESCO human-centred mindset).

[[___ ___ ___ ___]]

## Summary and Self-Check

- AI pedagogy combines AI-TPACK, personalisation, heutagogy and SRL – and performance with AI is not the same as learning.
- Formative AI feedback can help; summative decisions stay with teachers, and AI grading is high-risk under the EU AI Act.
- Test AI graders before trusting them: self-agreement and agreement with your own judgement.
- Co-create ethical rules with learners – the *Create* level of the ethics dimension.
- Cognitive offloading, bias and privacy are design questions – plan phases without AI and keep humans accountable.

**Tick what you can do now:**

- [ ] I can explain AI-augmented heutagogy with a TVET example.
- [ ] I can write an AI feedback prompt with the three feedback questions.
- [ ] I tested an AI grader with a mini-study.
- [ ] We drafted an AI agreement for our learning design.
- [ ] I can name the four key considerations of the EC guidelines.
- [ ] Our matrix has assessment and safeguard columns.

**Next session:** Thursday, 07.01.2027, 🟢 live – nuggets and micro-credentials, competency matrix workshop. Bring your extended matrix.

## References

- Chang, D. H., Lin, M. P.-C., Hajian, S., & Wang, Q. Q. (2023). Educational design principles of using AI chatbot that supports self-regulated learning in education: Goal setting, feedback, and personalization. *Sustainability, 15*(17), 12921. https://doi.org/10.3390/su151712921
- du Plooy, E., Casteleijn, D., & Franzsen, D. (2024). Personalized adaptive learning in higher education: A scoping review of key characteristics and impact on academic performance and engagement. *Heliyon, 10*(21), e39630. https://doi.org/10.1016/j.heliyon.2024.e39630
- European Commission. (2022). *Ethical guidelines on the use of artificial intelligence (AI) and data in teaching and learning for educators*. Publications Office of the European Union. https://data.europa.eu/doi/10.2766/153756
- European Union. (2024). *Regulation (EU) 2024/1689 (Artificial Intelligence Act)*. https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Flodén, J. (2025). Grading exams using large language models: A comparison between human and AI grading of exams in higher education using ChatGPT. *British Educational Research Journal, 51*(1), 201–224. https://doi.org/10.1002/berj.4069
- Gerlich, M. (2025). AI tools in society: Impacts on cognitive offloading and the future of critical thinking. *Societies, 15*(1), 6. https://doi.org/10.3390/soc15010006
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. https://doi.org/10.3102/003465430298487
- Institut für Arbeitsmarkt- und Berufsforschung. (n.d.). *Job-Futuromat* [Web application]. https://job-futuromat.iab.de
- Jones-Jang, S. M., Chung, M., Choi, J., Kim, N., & Lee, S. (2025). Fairness perceptions of AI in grading systems. *Computers and Education: Artificial Intelligence, 8*, 100419. https://doi.org/10.1016/j.caeai.2025.100419
- Kosmyna, N., Hauptmann, E., Yuan, Y. T., Situ, J., Liao, X.-H., Beresnitzky, A. V., Braunstein, I., & Maes, P. (2025). *Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant for essay writing task* (arXiv:2506.08872). https://arxiv.org/abs/2506.08872
- Luo, J., & Dawson, P. (2025). Exploring value judgements in grading: Will teachers mark down student work assisted by GenAI, and should they? *Studies in Higher Education*. https://doi.org/10.1080/03075079.2025.2552825
- Ng, S. H. S., & Lai, J. W. (2025). AI-augmented heutagogy: A framework for fostering self-determined learning and agency in higher education. *Higher Education Research & Development*. https://doi.org/10.1080/07294360.2025.2564977
- Ning, Y., Zhang, C., Xu, B., Zhou, Y., & Wijaya, T. T. (2024). Teachers’ AI-TPACK: Exploring the relationship between knowledge elements. *Sustainability, 16*(3), 978. https://doi.org/10.3390/su16030978
- OECD. (2026). *OECD digital education outlook 2026*. OECD Publishing. https://www.oecd.org/en/publications/oecd-digital-education-outlook-2026_062a7394-en.html
- UNESCO. (2024). *AI competency framework for teachers*. https://doi.org/10.54675/ZJTE2084
- Weidlich, J., Gotsch, F., Schudel, K., Marusic-Würscher, C., Mazzarella, J., Bolten, H., Bütler, D., Luger, S., Wohlfender, B., & Maag Merki, K. (2025). Teacher, peer, or AI? Comparing effects of feedback sources in higher education. *Computers and Education Open, 9*, 100300. https://doi.org/10.1016/j.caeo.2025.100300
- Zhao, Y., & Ko, J. (2024). Orchestrating vocational education classrooms for adaptive instruction and collaborative learning. *Cogent Education, 11*(1). https://doi.org/10.1080/2331186X.2024.2351238

<small>Licence: CC BY 4.0 · Dr. Hannes Tegelbeckers, OVGU Magdeburg · Created with AI support (Claude), checked and revised by the author.</small>

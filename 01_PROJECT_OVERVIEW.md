# 01 — Project Overview

## Product statement

**SkillBridge** bridges the gap between industry demand and university curriculum, and connects the resulting skills to real opportunities.

> SkillBridge doesn't just connect students to jobs. It connects industry demand to curriculum, curriculum to skills, and skills to opportunities.

## Core problem

Industry skill requirements change faster than university curricula.

| Stakeholder | Situation |
|---|---|
| Industry | Needs skills that keep changing |
| University | Teaches a curriculum that may lag behind demand |
| Student | May build skills that do not fully match current requirements |
| Company | Struggles to find candidates with the right skills |

## The chain SkillBridge makes measurable

```
Industry Demand
      ↓
University Curriculum
      ↓
Student Skills
      ↓
Skill Gaps
      ↓
Career Opportunities
```

It is **not** another job portal. Do not position it as a replacement for LinkedIn, Naukri or any professional network.

## Stakeholders

1. **Student** — "What skills do I have, what am I missing, and what opportunities fit me?"
2. **Industry / Company** — define requirements, find suitable candidates, understand why they match.
3. **University / Institution** — see industry demand, measure curriculum coverage, find gaps, benchmark alignment.

Plus a central, interactive **Skill Graph**: Student ↔ Skills ↔ Roles ↔ Internships ↔ Jobs.

## Reverse Matching (key feature)

- Normal platforms: Student → Opportunity.
- SkillBridge also supports: **Company Requirements → Suitable Candidates**.
- Result is a two-way matching model. Every match is explained, never just a number.

## Branding rules

- Name: **SkillBridge**.
- Header left: the supplied final logo + the text "SkillBridge". Use the logo file exactly as provided. Do not redraw, recolour or restyle it.
- Remove the old labels "Academia–Industry Platform" and "Skill Intelligence Ecosystem".
- Remove "Section 1" to "Section 5" labels.
- Remove decorative category labels: Career Hub, Credentials, Recruiting, Academic Insights, Skill Tracking Center.

## Content that must NOT appear anywhere in the UI (including tooltips, titles, alt text, comments shown in UI)

- SIH, Smart India Hackathon, problem statement IDs
- Gamma AI or Gamma-style wording
- Hackathon branding, team presentation labels, PPT/slide language
- Any mention that the UI was built with Claude or any AI tool
- LinkedIn comparison page, table, card, button, or text such as "Isn't this just LinkedIn Premium?"
- Presentation words as headings: "Our Solution", "Feature 1", "Innovation", "Impact", "Feasibility"

## Access model

| Visitor | Can see |
|---|---|
| Public (not logged in) | Home, Skill Graph, Student dashboard **preview** (headings visible, data blurred). Industry and University require login |
| Student | Own dashboard, profile, skills, applications, opportunities, improvement plan, skill passport |
| Industry | Own company dashboard only |
| University | Own university dashboard only |

### Privacy rule — Industry (system-level)

Company A must never see Company B's positions, requirements, matched candidates, shortlist, feedback or analytics. Structure state and data keyed by `companyId`, and filter every read by the logged-in company.

### Privacy rule — University

- A university sees full detail for **its own** curriculum, demand comparison, gaps, recommendations, score, rank and score explanation.
- For **other** universities show **rank and score only**. No curriculum, gaps, recommendations or explanation.
- Wording: "Industry Alignment Ranking", "Curriculum-to-Industry Alignment", "University Benchmark". **Never** "Best University".

## Honesty rules

- Current frontend = visual and workflow demonstration with sample data.
- Match scores, alignment scores, demand figures are **sample data**. Do not call them live, real-time, or produced by a trained model.
- Authentication in the demo is simulated in frontend state. Do not claim production security.
- Prefer words: explainability, evidence, transparent scoring, verified. Avoid "AI-powered" as decoration. No "100% accurate", "perfect matching", "guaranteed job".
- Where relevant, state: "Matching is based on available data and evidence."

## Technology

**Current file (keep):** HTML, CSS, JavaScript, React 18, ReactDOM, JSX, hooks, Tailwind via CDN, Recharts, browser-side state and demo data.

**Future implementation:**

| Layer | Choice |
|---|---|
| Frontend | HTML, CSS, JavaScript, Bootstrap where useful, Chart.js |
| Backend | Python, Flask, REST APIs |
| Database | SQLite first, SQL data model |
| Data / AI | Pandas, NumPy, scikit-learn, simple NLP skill extraction |

Do **not** introduce: React + TypeScript migration, Next.js, FastAPI, microservices, heavy AI frameworks, complex infrastructure.

## Conceptual architecture

```
USER LAYER        Student / Industry / University
                       ↓
DATA LAYER        Student data · Company requirements · Job/Internship data ·
                  University curriculum · Industry skill demand ·
                  Certificates · Projects · Applications
                       ↓
INTELLIGENCE      Skill extraction · Skill normalization · Skill matching ·
LAYER             Skill gap analysis · Curriculum alignment ·
                  Explainable matching · Recommendations
                       ↓
OUTPUT LAYER      Student opportunities · Improvement plan · Candidate ranking ·
                  Match explanation · Curriculum gaps · Alignment score ·
                  University benchmark · Skill Graph
```

In the current frontend, simulate these outputs with coherent demo data (see `04_DEMO_DATA_AND_ARCHITECTURE.md`).

## Design intent in one line

Education + Enterprise + Technology. A restrained, engineered product that looks built by an experienced team. Not an AI chatbot, not a futuristic startup, not a presentation turned into a website.

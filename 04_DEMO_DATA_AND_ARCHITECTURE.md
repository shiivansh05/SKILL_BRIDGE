# 04 — Demo Data and Architecture

All figures below are **sample data** for the current frontend demo. Every score is derived from the data by the formulas in section 1, so numbers never contradict visible evidence. Compute scores in code from the skill data. Do not hard-code them in JSX.

Company names, people and universities are fictional.

---

## 1. Formulas (single source of truth)

### Candidate / opportunity match score (0–100)

```
required_part   = 70 × (required skills matched ÷ required skills)
preferred_part  = 20 × (preferred skills matched ÷ preferred skills)
evidence_part   = 10 × (verified matched skills ÷ matched skills)
match           = round(required_part + preferred_part + evidence_part)   // round half up
```

- A skill is "matched" if the person has it. "Verified" means backed by a certificate, graded academic record, or reviewed project.
- Communication is shown as a **concern** when no verified evidence exists. It is not part of the score.
- **Confidence** (from evidence share): High ≥ 75% verified, Medium 50–74%, Low < 50%.

### University Industry Alignment Score (0–100)

```
alignment = Σ(demand_i × coverage_i) ÷ Σ(demand_i)       // demand-weighted curriculum coverage
```

- `demand_i` = industry demand index (0–100) for skill i.
- `coverage_i` = share of the university's curriculum covering skill i (0–100).
- Gap = `demand − coverage`. Status: gap < 10 → Aligned; 10–24 → Moderate gap; ≥ 25 → Critical gap.
- Coverage label: < 30 Very low · 30–54 Low · 55–74 Moderate · ≥ 75 High.
- Demand label: ≥ 75 High · 50–74 Medium.

---

## 2. Industry skill demand (shared by Student Market Intelligence and University dashboard)

| Skill | Category | Demand index | Trend |
|---|---|---|---|
| Python | Programming | 95 | → Stable |
| SQL | Data | 90 | → Stable |
| Machine Learning | AI / Data | 85 | ↑ Rising |
| Cloud (AWS / Azure / GCP) | Infrastructure | 88 | ↑ Rising |
| Docker | Infrastructure | 78 | ↑ Rising |
| Generative AI | AI / Data | 72 | ↑ Rising (emerging) |
| Data Visualization | Data | 70 | → Stable |
| Git / Version Control | Engineering | 65 | → Stable |

Skill normalization examples: AWS → Cloud; Pandas → Python data libraries (kept as its own skill for matching); "ML" → Machine Learning.

Role-wise (top skills, in order): Data Science Intern: Python, SQL, Machine Learning · Data Analyst Intern: SQL, Python, Data Visualization · Junior ML Engineer: Python, Machine Learning, Docker, Cloud · Backend Developer Intern: Python, SQL, REST APIs, Git.

Industry-wise (top skills): Retail analytics: SQL, Python, Data Visualization · Cloud and infrastructure: Cloud, Docker, Python · Healthcare data: Python, SQL, Git.

Label the table: "Sample demand data · Last updated {today's date}".

### Demo refresh (simulated update)

The **Refresh demo data** button applies this change to the demand index:

| Skill | Before | After |
|---|---|---|
| Cloud | 88 | 90 |
| Docker | 78 | 80 |
| Generative AI | 72 | 76 |

Then recompute gaps, recommendations and alignment: Your University goes **74 → 73**, still rank #3. Gaps: Cloud 28 → 30, Docker 33 → 35, Generative AI 27 → 31. This demonstrates "demand updates → comparison re-evaluated → gaps and recommendations change". Do not call it live.

---

## 3. University (Your University) curriculum coverage

| Skill | Demand | Coverage | Coverage label | Gap | Status |
|---|---|---|---|---|---|
| Python | 95 | 95 | High | 0 | Aligned |
| SQL | 90 | 90 | High | 0 | Aligned |
| Machine Learning | 85 | 80 | High | 5 | Aligned |
| Cloud | 88 | 60 | Moderate | 28 | Critical gap |
| Docker | 78 | 45 | Low | 33 | Critical gap |
| Generative AI | 72 | 45 | Low | 27 | Critical gap |
| Data Visualization | 70 | 85 | High | −15 | Aligned |
| Git / Version Control | 65 | 85 | High | −20 | Aligned |

Check: Σ demand = 643; Σ demand×coverage = 47,430; alignment = 73.76 → **74%**.

Recommendations (each tied to a gap):
1. **Docker (gap 33)** — add a practical containerisation module in the second-year software engineering course.
2. **Cloud (gap 28)** — add hands-on cloud deployment labs (compute, storage, basic deployment) to the existing systems course.
3. **Generative AI (gap 27)** — introduce an elective on prompt-based application development and evaluation.

### Benchmark (10 participating universities)

| Rank | University | Alignment score |
|---|---|---|
| 1 | University A | 86% |
| 2 | University B | 82% |
| 3 | **Your University** | **74%** |
| 4 | University C | 71% |
| 5 | University D | 69% |
| 6 | University E | 66% |
| 7 | University F | 63% |
| 8 | University G | 60% |
| 9 | University H | 57% |
| 10 | University I | 52% |

Other universities' rows expose only rank and score. Their coverage tables, gaps and recommendations do not exist in the logged-in university's state at all.

---

## 4. Student: Meera Iyer (demo student)

B.Tech Computer Science, Your University, graduating 2027.

| Skill | Level | Evidence | Verified |
|---|---|---|---|
| Python | Advanced | Course grade + certificate | Yes |
| SQL | Advanced | Course grade + certificate | Yes |
| Pandas | Intermediate | Reviewed project | Yes |
| Machine Learning | Intermediate | Course grade + certificate | Yes |
| Data Visualization | Intermediate | Certificate | Yes |
| Docker | Intermediate | Personal project, no certificate | No |
| Communication | — | No verified evidence | Concern only |

Missing relative to target roles: AWS / Cloud, REST APIs, Git.

Improvement Plan and Skill Passport: keep their current content and structure. If their data conflicts with the table above, adjust the data (not the structure) so the student's skills are the same everywhere.

---

## 5. Positions and opportunities

| ID | Company | Position | Type | Location | Mode | Terms | Required | Preferred |
|---|---|---|---|---|---|---|---|---|
| P1 | Orbis Analytics | Data Science Intern | Internship | Bengaluru | Hybrid | 6 months, ₹30,000 / month | Python, SQL, Pandas, Machine Learning | AWS, Docker |
| P2 | Kestrel Retail Tech | Data Analyst Intern | Internship | Pune | Remote | 3 months, ₹20,000 / month | SQL, Python, Data Visualization | Excel, Statistics |
| P3 | Northline Cloud Systems | Junior ML Engineer | Job | Hyderabad | On-site | ₹7–9 LPA | Python, Machine Learning, Docker, AWS | Kubernetes, SQL |
| P4 | Veridian Health Data | Backend Developer Intern | Internship | Remote | Remote | 4 months, ₹15,000 / month | Python, SQL, REST APIs, Git | Flask, Docker |

### Meera's match (by formula)

| Position | Required | Preferred | Evidence | Match |
|---|---|---|---|---|
| P1 Data Science Intern | 4/4 → 70 | 1/2 → 10 (Docker) | 4/5 verified → 8 | **88%** |
| P2 Data Analyst Intern | 3/3 → 70 | 0/2 → 0 | 3/3 → 10 | **80%** |
| P3 Junior ML Engineer | 3/4 → 52.5 | 1/2 → 10 (SQL) | 3/4 → 7.5 | **70%** |
| P4 Backend Developer Intern | 2/4 → 35 | 1/2 → 10 (Docker) | 2/3 → 6.7 | **52%** |

"Why you match" example (P1): "Matches 4 of 4 required skills, all verified. Missing preferred skill: AWS."

---

## 6. Industry: Orbis Analytics, position P1 candidates

| Candidate | Required | Preferred | Evidence | Match | Confidence |
|---|---|---|---|---|---|
| Meera Iyer | 4/4 | Docker (1/2) | 4/5 verified | **88%** | High (80%) |
| Kavya Nair | 3/4 (missing Machine Learning) | AWS, Docker (2/2) | 3/5 verified | **79%** | Medium (60%) |
| Rohan Das | 4/4 | none (0/2) | 3/4 verified | **78%** | High (75%) |
| Sahil Verma | 2/4 (Python, SQL) | none | 1/2 verified | **40%** | Medium (50%) |

Sorted by match: Meera 88, Kavya 79, Rohan 78, Sahil 40.

Match Explanation, Meera for P1:
- ✓ Matched: Python, SQL, Pandas, Machine Learning, Docker
- ⚠ Concern: Communication — no verified evidence
- ✕ Missing: AWS
- Confidence: High — 4 of 5 matched skills are verified (Docker is a personal project without certification).

Sample candidate detail fields: education, skills with level, verified flag, 1–2 projects, certificates, experience (if any). Do not include phone, address or ID numbers.

Kestrel Retail Tech has its own position (P2) and its own candidate list. Orbis never sees it, and vice versa.

---

## 7. Demo accounts (simulated auth only)

| Role | Email | Organisation |
|---|---|---|
| Student | `meera.iyer@student.example.edu` | Your University |
| Industry | `hiring@orbis-analytics.example.com` | Orbis Analytics (`c_orbis`) |
| Industry | `hiring@kestrel-retail.example.com` | Kestrel Retail Tech (`c_kestrel`) |
| University | `industry.cell@youruniversity.example.edu` | Your University (`u_you`) |

Password for all demo accounts: `Demo@1234`. State clearly in code comments that this is simulated.

---

## 8. Frontend state shape (organisation-level isolation)

```js
const db = {
  skills: { /* id → { name, category } */ },
  demand: { /* skillId → { index, trend } */ },
  students: { s_meera: { name, skills: [{ skillId, level, verified, evidence }], ... } },
  companies: { c_orbis: { name }, c_kestrel: { name } },
  positions: [
    { id: 'P1', companyId: 'c_orbis', role, type, required: [], preferred: [], ... },
    { id: 'P2', companyId: 'c_kestrel', ... },
  ],
  shortlists: [{ companyId, positionId, studentId, status, feedback }],
  universities: {
    u_you: { name: 'Your University', coverage: { skillId: 0 } },
    // other universities: only { rank, score } is ever exposed to a non-owner
  },
};

// All reads go through selectors that take the session.
const positionsFor = (session) =>
  db.positions.filter(p => p.companyId === session.orgId);

const shortlistFor = (session) =>
  db.shortlists.filter(s => s.companyId === session.orgId);

const benchmarkFor = (session, rows) =>
  rows.map(r => r.universityId === session.orgId
    ? { ...r, detail: universityDetail(r.universityId) }  // own: full detail
    : { rank: r.rank, name: r.name, score: r.score });    // others: rank + score only

const matchScore = (person, position) => { /* formula in section 1 */ };
const alignmentScore = (demand, coverage) => { /* formula in section 1 */ };
```

Components must receive data from these selectors. Never pass the whole `db` into a dashboard component.

---

## 9. Future backend (Flask + SQLite)

Not part of the current frontend task. This is the structure the frontend should map onto.

**Tables**: `users`, `students`, `student_skills`, `certificates`, `projects`, `companies`, `positions`, `position_skills`, `applications`, `shortlists`, `universities`, `curriculum_courses`, `curriculum_skills`, `skills`, `skill_aliases`, `industry_demand` (skill_id, demand_index, trend, updated_at), `alignment_scores`.

**Isolation**: every company query includes `WHERE company_id = :session_company_id`. University detail endpoints check `university_id == session.university_id`; the benchmark endpoint returns `rank, name, score` only for others.

**REST endpoints (examples)**

| Area | Endpoints |
|---|---|
| Auth | `POST /api/auth/signup`, `POST /api/auth/login`, `POST /api/auth/forgot-password`, `POST /api/auth/logout` |
| Student | `GET/PUT /api/student/profile`, `GET /api/student/skills`, `POST /api/student/resume/extract`, `GET /api/student/opportunities?q=&type=&location=&mode=`, `POST /api/student/applications`, `GET /api/student/improvement-plan` |
| Industry | `POST /api/company/positions`, `GET /api/company/positions`, `GET /api/company/positions/:id/candidates`, `GET /api/company/candidates/:id`, `GET /api/company/positions/:id/candidates/:sid/explanation`, `POST /api/company/shortlist`, `POST /api/company/feedback` |
| University | `GET /api/university/demand`, `GET /api/university/curriculum`, `GET /api/university/gaps`, `GET /api/university/alignment`, `GET /api/university/benchmark`, `GET /api/university/recommendations` |
| Graph | `GET /api/skill-graph` |

**Intelligence layer (simple and explainable)**: keyword/entity skill extraction → alias-based skill normalization → weighted skill matching (formula above) with Pandas/NumPy → coverage and gap analysis → rule-based recommendations. scikit-learn (e.g. TF-IDF similarity) can supplement skill extraction later. Demand data refreshed on a schedule from a dataset the team controls.

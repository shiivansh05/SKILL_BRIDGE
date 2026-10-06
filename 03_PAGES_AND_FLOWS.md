# 03 — Pages and Flows

Rule for every page: preserve existing working interactions in `PROTOTYPE_FINAL (2).html`. Refine structure, hierarchy, styling, wording and flow. Do not leave dead navigation, buttons pointing to deleted pages, or references to removed sections.

---

## 1. Global header

```
[Logo]  SkillBridge                                   [Profile photo] [≡]
```

- Left: supplied final logo (unchanged) + the text "SkillBridge".
- Right: profile photo, with the three-line hamburger immediately beside it.
- The **photo is not clickable**. The **hamburger is the only control**.
- Hamburger menu contains exactly: **My Profile**, **Why SkillBridge?**, **Logout**.
- Before login: show Login / Sign up in place of the photo, and keep the hamburger with Why SkillBridge? available.
- Logout returns to the public Home.
- Primary navigation stays minimal and role-aware. Do not expose every internal module as a tab.

---

## 2. Public Home

Compact. Communicates: **Problem → Solution → Three stakeholders → Interactive Skill Graph**.

1. **Hero** (compact, navy background, flat colour)
   - Title: SkillBridge
   - Line: "Bridging the gap between industry demand and university curriculum."
   - Supporting: "SkillBridge connects industry demand, university curriculum, student skills, and opportunities through skill intelligence."
2. **Stakeholder row**: University | Industry | Student. Three balanced blocks in one row (stack on mobile). Each: name, one-line purpose, one action.
   - University: "See how your curriculum aligns with industry demand." → requires login
   - Industry: "Define requirements and find suitable candidates." → requires login
   - Student: "See your skills, gaps and matching opportunities." → public preview
3. **Interactive Skill Graph**: large, the visual centrepiece. Keep the existing graph as is.

Nothing below the graph. No data tables, salary dashboards, statistics walls, feature sections, comparison content or long marketing copy.

---

## 3. Authentication (one shared experience)

Account types: **Student, University, Industry**. Simulated in frontend state; do not claim production security.

**Login**
- Fields: Email / Institutional Email, Password.
- Actions: Login, Forgot Password, Sign Up.
- Do not ask for account type on login when the account already has one. The role comes from the account.

**Sign up**: step 1 choose Student / University / Industry, step 2 role fields.

| Role | Fields |
|---|---|
| Student | Full Name, Email, Password, University / College, Course / Branch, Graduation Year |
| University | University Name, Official Institutional Email, Contact Person, Password, Website, Departments / basic details |
| Industry | Company Name, Official Company Email, Contact Person, Password, Industry / Company Type, Website |

Validation: required fields, email format, password minimum length with a strength hint, graduation year range, URL format. Inline messages under the field with an icon, e.g. "Enter a valid email address."

Forgot Password: simple email form with a confirmation message (simulated).

After login the UI shows **only** that role's experience.

---

## 4. Student (public preview + logged-in)

Core question: "What skills do I have, what am I missing, and what opportunities fit me?"

**Fixed section order**

1. Opportunities For Me
   - Search box: "Search roles, skills, companies"
   - Filters: **Job / Internship**, **Preferred Location**, **Work Mode**
   - Remove: Minimum Package, Desired Role filter, "Curated AI Recommendations", any "Matching candidate: …" sentence
2. Search results
3. Market Intelligence
4. Improvement Plan
5. Skill Passport

**Empty state** (initial): "Search for a role, skill, or company to discover matching opportunities." Do **not** list the demo opportunities until the student searches or changes a filter.

**Opportunity card (compact)**: role, company, location, work mode, match %, relevant skills, one-line "Why you match", stipend/package where applicable, duration, Save, Apply.

**Market Intelligence** (kept, compact): appears after search. Shows current demand, relevant skills, role trend, demand intensity as a small table or horizontal bars with a trend label (↑ Rising, → Stable). Not a big analytics dashboard. Marked "Sample data".

**Improvement Plan** and **Skill Passport**: keep the current content and structure essentially unchanged. Integrate them into the flow visually only.

### Public preview (before login)
- Whole student dashboard is visible.
- **All headings and section labels stay clear**: Opportunities For Me, Market Intelligence, Improvement Plan, Skill Passport, Applications.
- Only the data inside private sections is blurred.
- Clicking any blurred region opens a prompt: **"Login to access your personalized student data."** with Login and Sign up buttons.
- Do not hide the whole page behind one login wall.

Implementation hint: a `PrivateRegion` component. It renders `<section><h3>Title</h3><div class="relative"><div aria-hidden class="blur-[5px] select-none pointer-events-none">…</div><button class="absolute inset-0" aria-label="Login to view {Title}"></button></div></section>`. When logged in it renders children normally.

---

## 5. My Profile (hamburger → My Profile)

**Student**: move everything from the current Student Details section here. **Same information and same general arrangement.** Do not redesign.
- Personal Details
- Academic & Professional Details
- AI Resume Skill Extractor
- Verified Documents
- Student Portfolio
- Edit Information (edit → save → cancel workflow with validation)

**Industry**: Company profile (name, type, website, contact person, positions summary). Edit workflow.
**University**: University profile (name, website, departments, contact person). Edit workflow.

The AI Resume Skill Extractor stays as a demo of simple skill extraction. Label results "Extracted skills (review before saving)".

---

## 6. Why SkillBridge? (hamburger → Why SkillBridge?)

A clear explanation page, not a marketing page. No statistics, no tech stack, no comparison.

1. **The problem**: Industry skills change faster than university curricula. This can create a gap between curriculum, student skills, industry requirements and employment opportunities.
2. **What SkillBridge does** (simple vertical or horizontal flow):
   Industry Demand → Curriculum Analysis → Student Skill Gap → Career Opportunities
3. **For universities**: identify curriculum gaps; measure curriculum-to-industry alignment; benchmark alignment; receive curriculum recommendations.
4. **For industry**: define skill requirements; post jobs and internships; find suitable candidates; use explainable candidate matching.
5. **For students**: understand skill gaps; improve relevant skills; discover suitable opportunities; build a stronger skill profile.
6. **Closing line**: "SkillBridge doesn't just connect students to jobs. It connects industry demand to curriculum, curriculum to skills, and skills to opportunities."

---

## 7. Industry / Company dashboard

**Fixed order**

1. **Post New Position**: modal or panel. Fields: Job / Internship, Role, Description, Required skills, Preferred skills, Experience level, Location, Work mode, other requirements (duration, stipend/package). Keep the current workflow, refine visually.
2. **Requirements**: after creating, show Required Skills and Preferred Skills as clear lists. These drive matching.
3. **Search Suitable Candidates** ("Find Candidates"): candidates are evaluated against the selected position's requirements. Results table sorted by match %, with filters. Values are sample data.
4. **Candidate Inspection**: selecting a candidate opens a side panel (desktop) or full-width section (mobile). Shows profile, education, skills, verified skills, projects, certificates, experience where available. No unnecessary private data (no phone, address, ID numbers).
5. **Match Explanation** (explainable matching): never only a number.
   ```
   89% match
   ✓ Matched   Python · SQL · Pandas · Machine Learning · Docker
   ⚠ Concern   Communication — no verified evidence yet
   ✕ Missing   AWS
   ```
   Include the scoring factors in plain language (required skills coverage, preferred skills coverage, evidence). Use the heading "Match Explanation", not "AI-powered".
6. **Match Evidence / Confidence / Skill Details**: for each skill: level, verified or self-reported, evidence source (certificate, project, academic). Confidence label (High / Medium / Low) derived from the share of verified evidence.
7. **Shortlist / Give Feedback**: Shortlist toggle and a feedback form (outcome + short note). Shortlist and feedback belong to the company only.

**Privacy**: every list, count and chart filters by the logged-in `companyId`. Company A cannot see Company B's positions, requirements, candidates, shortlist, feedback or analytics. Show a small "Only visible to your organisation" note on the dashboard.

Note: "Reverse Matching" can be named once in the Find Candidates section: "Requirements → suitable candidates".

---

## 8. University dashboard

**Fixed order**

### 8.1 Current Industry Skill Demand (first, detailed, highlighted)
- Table of most demanded skills: skill, category, demand index (0–100) with bar, trend (↑ Rising / → Stable), emerging flag.
- Tabs: Most demanded · Emerging skills · By role · By industry.
- Header note: "Sample demand data · Last updated {date}". A **Refresh demo data** button applies a small change to the demand data, and 8.2 and 8.3 recompute. Do not call it live or real-time.
- Message: "Industry demand changes over time; curriculum comparison is re-evaluated when the demand data is updated."

### 8.2 Curriculum Gap Analysis
- Table: Skill · Industry demand (High/Medium) · University coverage (Very low/Low/Moderate/High) · Gap · Status (icon + label).
- Recommendations tied to specific gaps, e.g. "Add practical Cloud and Docker training."
- Detailed view of the user's **own** university only.

### 8.3 Industry Alignment Ranking (University Benchmark)
- Title wording: "Industry Alignment Ranking" with subtitle "Curriculum-to-Industry Alignment". Not "best university".
- Table of 10 participating universities: Rank · University · Alignment score.
- Own row highlighted. Own row expands to show score explanation (how coverage and demand produce the score), gaps and recommendations.
- Other rows: **rank and score only**. No expand, no detail link.

### 8.4 Supporting outcomes (secondary, compact, at the bottom)
- Existing placement/internship analytics kept as a small supporting section. Must not dominate the page.

### Remove
- Cards titled **Curriculum Health**, **Priority Action**, **Outcome Feedback**.

---

## 9. Skill Graph

- **Keep the current Skill Graph.** Do not redesign, do not make it static, do not remove interactivity.
- Concept: Student ↔ Skills ↔ Roles ↔ Internships ↔ Jobs. Represents skill progress, current vs required level, industry demand, related roles and opportunities.
- Only change: in the **selected-skill info panel**, remove these three bottom items and nothing else:
  - Curriculum link
  - Related Roles
  - Aligned Opportunities
- Home: placed under the stakeholder row, large. It is a frontend visualisation, not a graph database; do not describe it as one.
- Make sure it fits the viewport on mobile and stays touch-interactive.

---

## 10. Removed items (verify none remain)

- LinkedIn comparison page, nav entry, cards, buttons, table, "Isn't this just LinkedIn Premium?"
- Old branding labels and Section 1–5 labels
- Minimum Package, Desired Role filter, Curated AI Recommendations, "Matching candidate: …" text
- University cards: Curriculum Health, Priority Action, Outcome Feedback
- Skill Graph panel items: Curriculum link, Related Roles, Aligned Opportunities
- Any SIH / hackathon / Gamma / presentation wording

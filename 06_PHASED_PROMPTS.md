# 06 — Phased Prompts

Run in order. Attach `PROTOTYPE_FINAL (2).html`, the logo, and the relevant reference files each time (the platform may forget earlier files). Check the result of each phase before starting the next.

Every phase begins with this preamble. Paste it first, every time.

````text
PREAMBLE
You are editing the existing file "PROTOTYPE_FINAL (2).html" for a product called SkillBridge. Keep React 18, Tailwind CDN and Recharts. Do not rewrite the app from scratch and do not break working interactions. Read the relevant code before changing it. Design: restrained enterprise education-tech. Navy #0F2747, blue #1E5AA8, teal #187C7A (accent only), background #F7F8FA, white surfaces, text #172033, secondary #5F6B7A, border #DCE2E8. IBM Plex Sans. Radius 6/8/12px, subtle shadows, no gradients, no purple, no neon, no glassmorphism, no emoji, no giant cards. Never mention SIH, hackathon, Gamma, LinkedIn or the tools used to build this. Scores and demand figures are sample data; never call them live or model-generated. Work only on the scope below, and tell me briefly what you changed.
````

---

## Phase 1 — Audit and design tokens

````text
SCOPE: Audit, then design tokens only.
1. Read the whole file. List: components, state, navigation tabs, modals, charts, skill graph code, student/company/university sections, demo data, and every occurrence of: SIH, Smart India Hackathon, Gamma, "Academia", "Skill Intelligence", "Section 1-5", Career Hub, Credentials, Recruiting, Academic Insights, Skill Tracking Center, LinkedIn. Show me the list. Do not edit yet.
2. Then add design tokens: Tailwind config (colours navy/brand/teal/canvas/ink/line/ok/warn/bad, IBM Plex Sans, radii 6/8/12), CSS variables, focus ring (0 0 0 3px rgba(30,90,168,.35)), and base styles (body background #F7F8FA, text #172033, 14px body). Add reusable components if missing: Button (primary/secondary/tertiary), Field (label + input + error), Badge (icon + label), Table wrapper (overflow-x auto), Tabs, Modal (focus trap, Esc), StatusTag (Matched / Partial / Missing / Verified).
Do not restyle pages yet.
````

## Phase 2 — Header, branding cleanup, navigation

````text
SCOPE: global header, branding cleanup, navigation.
- Header left: the supplied final logo, used exactly as provided, plus the text "SkillBridge". Right: profile photo (not clickable) with a three-line hamburger button immediately beside it. Hamburger dropdown contains exactly: My Profile, Why SkillBridge?, Logout. Close on outside click and Esc. Keyboard accessible.
- Before login show Login and Sign up in place of the photo.
- Remove old branding labels, Section 1-5 labels, decorative category labels (Career Hub, Credentials, Recruiting, Academic Insights, Skill Tracking Center), all SIH/hackathon/Gamma wording, and the entire LinkedIn comparison page with every nav item, card and button leading to it.
- Keep navigation minimal and role-aware; do not expose every module as a tab. Ensure no dead links remain.
````

## Phase 3 — Public Home

````text
SCOPE: public Home page only.
Compact hero (flat navy, no gradient): "SkillBridge" / "Bridging the gap between industry demand and university curriculum." / "SkillBridge connects industry demand, university curriculum, student skills, and opportunities through skill intelligence." Below: one row of three equal stakeholder blocks, UNIVERSITY | INDUSTRY | STUDENT, each with a one-line purpose and one action. University and Industry actions open login; Student opens the public preview. Below that: the existing interactive Skill Graph, large, as the centrepiece. Nothing after the graph. No tables, salary data, statistics, feature sections or comparison content. Stack on mobile; graph must fit the viewport.
````

## Phase 4 — Authentication and role-based access

````text
SCOPE: login, signup, forgot password, role-based dashboards.
Simulated in frontend state (state it in a code comment; do not claim production security).
- One shared auth modal/page. Login: Email / Institutional Email, Password, Login, Forgot Password, Sign Up. Role comes from the account, do not ask for it at login.
- Signup: first choose Student / University / Industry, then role fields. Student: Full Name, Email, Password, University/College, Course/Branch, Graduation Year. University: University Name, Official Institutional Email, Contact Person, Password, Website, Departments/basic details. Industry: Company Name, Official Company Email, Contact Person, Password, Industry/Company Type, Website.
- Inline validation with clear messages (required, email format, password length, URL, graduation year).
- Session = { role, orgId, name }. After login show only that role's dashboard. Logout returns to public Home.
- Seed demo accounts: meera.iyer@student.example.edu (student), hiring@orbis-analytics.example.com (company c_orbis), hiring@kestrel-retail.example.com (company c_kestrel), industry.cell@youruniversity.example.edu (university u_you). Password Demo@1234.
- Public rules: Home and Student preview are public; Industry and University require login.
````

## Phase 5 — Student dashboard and public preview

````text
SCOPE: Student dashboard only.
Fixed order: Opportunities For Me -> Search results -> Market Intelligence -> Improvement Plan -> Skill Passport.
- Search input "Search roles, skills, companies" plus filters Job/Internship, Preferred Location, Work Mode. Remove Minimum Package, Desired Role filter, "Curated AI Recommendations" and any "Matching candidate: ..." sentence.
- Initial empty state: "Search for a role, skill, or company to discover matching opportunities." Show opportunities only after search or filter change; filters actually update the list.
- Compact opportunity cards: role, company, location, work mode, match %, relevant skills, one-line why you match, stipend/package, duration, Save, Apply.
- Keep Market Intelligence, compact, shown after search (demand, relevant skills, trend, intensity), labelled sample data.
- Keep Improvement Plan and Skill Passport content and structure unchanged; only integrate visually.
- Public preview: create a PrivateRegion component. Headings always visible; only the data inside private sections is blurred (blur 5px, aria-hidden, not selectable). Clicking a blurred region opens a prompt "Login to access your personalized student data." with Login and Sign up. When logged in, render normally.
- Use the demo data in 04_DEMO_DATA_AND_ARCHITECTURE.md; compute match scores with the formula, do not hard-code them. Meera should get P1 88, P2 80, P3 70, P4 52.
````

## Phase 6 — My Profile

````text
SCOPE: My Profile.
Move everything from the current Student Details section into Hamburger -> My Profile. Keep the SAME information and SAME general arrangement: Personal Details, Academic & Professional Details, AI Resume Skill Extractor, Verified Documents, Student Portfolio, Edit Information (edit -> save / cancel, with validation). Remove the old Student Details entry from other navigation. Apply the new styling tokens only. For Industry, My Profile shows the company profile (name, type, website, contact person, positions summary, edit). For University, the university profile (name, website, departments, contact person, edit). Label extracted resume skills "Extracted skills (review before saving)".
````

## Phase 7 — Industry dashboard

````text
SCOPE: Industry dashboard.
Fixed order: Post New Position -> Requirements -> Search Suitable Candidates -> Candidate Inspection -> Match Explanation -> Evidence / Confidence / Skill details -> Shortlist / Give Feedback.
- Keep the existing Post New Position modal; refine the visuals. Fields: Job/Internship, Role, Description, Required skills, Preferred skills, Experience level, Location, Work mode, other requirements.
- Show Required and Preferred skills as clear lists after creating a position.
- "Find Candidates": candidates evaluated against the selected position, sorted by match %, with filters. Sample data, computed by the formula; Orbis P1 expected: Meera 88, Kavya 79, Rohan 78, Sahil 40.
- Candidate Inspection panel: profile, education, skills, verified skills, projects, certificates, experience. No phone, address or ID data.
- Match Explanation: Matched / Concern / Missing, each with icon + label + colour, plus the scoring factors in plain language. Evidence, confidence (High/Medium/Low from verified share), skill level and evidence source. Never show only a number. Do not claim a trained model.
- Shortlist toggle and feedback form.
- PRIVACY: store data keyed by companyId and read it only through selectors using the session. Company A must never see Company B's positions, requirements, candidates, shortlist, feedback or analytics. Test by logging in as both demo companies.
````

## Phase 8 — University dashboard

````text
SCOPE: University dashboard.
Fixed order: 1 Current Industry Skill Demand -> 2 Curriculum Gap Analysis -> 3 Industry Alignment Ranking (University Benchmark). Supporting placement/internship analytics move to a small section at the bottom.
- Section 1 (first, detailed): demand table with skill, category, demand index bar, trend (Rising / Stable), emerging flag; tabs Most demanded / Emerging / By role / By industry. Note "Sample demand data - Last updated {date}". Add a "Refresh demo data" button (Cloud 88->90, Docker 78->80, Generative AI 72->76) that recomputes sections 2 and 3. Do not call it live.
- Section 2: demand vs coverage table with gap and status (icon + label), and recommendations tied to the gaps (Docker, Cloud, Generative AI).
- Section 3: benchmark of 10 universities (A 86, B 82, Your University 74, C 71, D 69, E 66, F 63, G 60, H 57, I 52). Title "Industry Alignment Ranking", subtitle "Curriculum-to-Industry Alignment". Own row highlighted and expandable with score explanation, gaps, recommendations. Other rows: rank and score only. Never use "Best University".
- Alignment = sum(demand x coverage) / sum(demand), computed in code (74 before refresh, 73 after, rank stays #3).
- REMOVE the cards Curriculum Health, Priority Action, Outcome Feedback.
- Privacy: other universities' coverage, gaps and recommendations must not exist in the logged-in university's state.
````

## Phase 9 — Why SkillBridge? and Skill Graph edit

````text
SCOPE: two small changes.
1. Why SkillBridge? page (opened from the hamburger): problem statement; flow Industry Demand -> Curriculum Analysis -> Student Skill Gap -> Career Opportunities; sections For Universities, For Industry, For Students (four points each, as listed in 03_PAGES_AND_FLOWS.md); closing line "SkillBridge doesn't just connect students to jobs. It connects industry demand to curriculum, curriculum to skills, and skills to opportunities." No LinkedIn comparison, no tech stack, no statistics.
2. Skill Graph: do NOT redesign it, do NOT make it static, keep every interaction. Only remove from the selected-skill info panel: "Curriculum link", "Related Roles", "Aligned Opportunities". Confirm nothing else changed and that the graph fits the viewport on mobile.
````

## Phase 10 — Consistency, responsive, accessibility pass

````text
SCOPE: whole app review and fixes.
- Make colours, spacing, radii, type sizes and button styles consistent across all dashboards.
- Responsive check at 1440, 1024, 768, 390 px: no overflow, no overlapping controls, tables scroll inside wrappers, graph fits.
- Accessibility: labels on all fields, visible focus on all controls, Esc closes menu/modals, focus trapped in modals, contrast >= 4.5:1, status always icon + label + colour.
- Remove dead code, dead nav, unused buttons, old branding in tooltips/titles/alt text. Search the file for: SIH, Hackathon, Gamma, LinkedIn, Academia, "Skill Intelligence", "Section", "Curated AI", "Minimum Package", "Curriculum Health", "Priority Action", "Outcome Feedback". None should remain.
- Check data consistency: every score is computed from visible skills and requirements.
- Report what you changed and anything you could not fix.
````

## Phase 11 (optional, later) — Flask backend scaffold

````text
SCOPE: new backend, separate from the frontend file.
Create a Flask + SQLite backend following 04_DEMO_DATA_AND_ARCHITECTURE.md section 9. Use Python, Flask, sqlite3 (or SQLAlchemy only if needed), Pandas, NumPy. Implement: auth (hashed passwords, session), student profile/skills/opportunities, company positions and candidate matching using the documented formula, university demand/gaps/alignment/benchmark. Enforce isolation in SQL: company queries filter by the session company_id; university detail endpoints allow only the owner; the benchmark returns rank/name/score only for others. Seed the database with the demo dataset. Keep it simple: no microservices, no heavy AI frameworks. Skill extraction = keyword/alias matching with normalization. Provide README run steps.
````

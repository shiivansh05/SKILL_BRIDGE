# 05 — Master Prompt (paste into the vibe-coding platform)

Attach: `PROTOTYPE_FINAL (2).html`, the final SkillBridge logo file, and ideally `02_DESIGN_SYSTEM.md`, `03_PAGES_AND_FLOWS.md`, `04_DEMO_DATA_AND_ARCHITECTURE.md`.

---

````text
You are a senior product engineer, frontend architect and UI/UX designer.

TASK
Refine my existing frontend, "PROTOTYPE_FINAL (2).html", into a polished, enterprise-grade product called SkillBridge. Edit the existing file. Do NOT rewrite the app from scratch and do NOT break working interactions. First read the whole file and understand its components, state, navigation, demo data, charts, skill graph and modals. Then change only what is needed.

KEEP THE CURRENT STACK in this file: HTML, CSS, JavaScript, React 18, ReactDOM, JSX, hooks, Tailwind via CDN, Recharts, browser-side state and demo data. Do not add TypeScript, Next.js, FastAPI or new heavy dependencies. (The future real implementation will be Flask + SQLite + Pandas/NumPy/scikit-learn with Bootstrap and Chart.js, but that is NOT part of this task.)

PRODUCT
SkillBridge connects industry demand -> university curriculum -> student skills -> skill gaps -> career opportunities. Industry skills change faster than curricula; SkillBridge makes that gap measurable. It is NOT a job portal and must not be compared to LinkedIn or Naukri. Three stakeholders: Student, Industry/Company, University. Central interactive Skill Graph. Reverse Matching: company requirements -> suitable candidates.

BRANDING
- Name: SkillBridge. Header left: the supplied final logo (use exactly as provided, do not redraw) + text "SkillBridge". Header right: profile photo (NOT clickable) with a three-line hamburger immediately beside it. Hamburger menu has exactly: My Profile, Why SkillBridge?, Logout.
- Remove: "Academia-Industry Platform", "Skill Intelligence Ecosystem", "Section 1..5" labels, and the labels Career Hub, Credentials, Recruiting, Academic Insights, Skill Tracking Center.
- Remove EVERYWHERE (including tooltips, titles, alt text): SIH, Smart India Hackathon, problem statement IDs, Gamma, hackathon/team/PPT wording, any mention of AI tools used to build it, and ALL LinkedIn comparison content (page, nav, cards, buttons, tables, "Isn't this just LinkedIn Premium?"). Leave no dead links.

DESIGN (restrained enterprise education-tech; must NOT look AI-generated)
- Colours: navy #0F2747 (primary), blue #1E5AA8 (secondary), muted teal #187C7A (small accent only), background #F7F8FA, surface #FFFFFF, text #172033, secondary text #5F6B7A, border #DCE2E8, success #2F7D4F on #E8F3EC, warning #9A6A12 on #FBF3E0, error #B3433F on #FAEAE9.
- Font: IBM Plex Sans (fallback Inter/system). Body 14px, card heading 16px, section 20px, page title 28px, hero max 36px, metadata 12px. Weights 400/500/600.
- Radius 6px (buttons/inputs/badges), 8px (cards), 12px (modals/menus). 1px borders. Shadow only very subtle; stronger only on menus/modals. 4px spacing scale.
- FORBIDDEN: gradients, purple, neon, glow, glassmorphism, giant rounded cards, heavy shadows, decorative blobs, emoji, "AI" badges everywhere, many pills, giant type, decorative animation, a card for every item, repeated stat tiles, slide-style sections.
- Use varied structures: tables, lists, metric rows, tabs, panels, forms, compact cards. Realistic density.
- Interactions: clear hover/focus/active/disabled states, visible focus ring, 120-180ms ease-out transitions, respect prefers-reduced-motion.
- Status is always icon + label + colour (Matched / Partial / Missing / Verified).
- Responsive for desktop, laptop, tablet, mobile: no text overflow, no horizontal page scroll, tables scroll inside wrappers, skill graph fits viewport.
- Accessibility: semantic buttons, labels on all fields, contrast >= 4.5:1, focus-trapped modals, Esc closes menus/modals.

PUBLIC HOME (compact)
Hero: "SkillBridge" / "Bridging the gap between industry demand and university curriculum." / "SkillBridge connects industry demand, university curriculum, student skills, and opportunities through skill intelligence." Then one row: UNIVERSITY | INDUSTRY | STUDENT. Then the large interactive Skill Graph. Nothing below it. No tables, salary dashboards, statistics, feature sections or long copy.
Access: Home and Student preview are public. Industry and University require login.

AUTH (simulated in frontend state; do not claim production security)
One shared flow for Student / University / Industry. Login: Email/Institutional Email + Password, Login, Forgot Password, Sign Up. Do not ask for account type at login; role comes from the account. Sign up: pick role first, then role fields:
- Student: Full Name, Email, Password, University/College, Course/Branch, Graduation Year
- University: University Name, Official Institutional Email, Contact Person, Password, Website, Departments/basic details
- Industry: Company Name, Official Company Email, Contact Person, Password, Industry/Company Type, Website
Inline validation with clear messages. After login show ONLY that role's dashboard. Logout returns to public Home.

STUDENT (fixed order)
1 Opportunities For Me: search "roles, skills, companies" + filters Job/Internship, Preferred Location, Work Mode. REMOVE Minimum Package, Desired Role filter, "Curated AI Recommendations", and any "Matching candidate: ..." sentence. Initial empty state: "Search for a role, skill, or company to discover matching opportunities." Show results only after search/filter. Compact opportunity cards: role, company, location, work mode, match %, relevant skills, why you match, stipend/package, duration, Save, Apply.
2 Search results. 3 Market Intelligence (KEEP, compact, after search: demand, relevant skills, trend, intensity; marked sample data). 4 Improvement Plan (keep content/structure). 5 Skill Passport (keep content/structure).
Public preview before login: whole dashboard visible, ALL headings visible, only data inside private sections blurred. Clicking blurred data opens: "Login to access your personalized student data." Build a reusable PrivateRegion component. No giant login wall.

MY PROFILE (hamburger)
Move all current Student Details here with the SAME information and SAME arrangement: Personal Details, Academic & Professional Details, AI Resume Skill Extractor, Verified Documents, Student Portfolio, Edit Information (edit/save/cancel). Industry -> company profile; University -> university profile.

WHY SKILLBRIDGE? (hamburger)
Problem (industry skills change faster than curricula) -> flow Industry Demand -> Curriculum Analysis -> Student Skill Gap -> Career Opportunities -> For Universities (identify gaps, measure alignment, benchmark, recommendations) -> For Industry (define requirements, post jobs/internships, find candidates, explainable matching) -> For Students (understand gaps, improve skills, discover opportunities, build stronger profile). Closing: "SkillBridge doesn't just connect students to jobs. It connects industry demand to curriculum, curriculum to skills, and skills to opportunities." No LinkedIn comparison, no tech stack, no statistics.

INDUSTRY (fixed order)
1 Post New Position (Job/Internship, Role, Description, Required skills, Preferred skills, Experience level, Location, Work mode, other requirements; keep current modal, refine) -> 2 Requirements (Required / Preferred lists) -> 3 Search Suitable Candidates ("Find Candidates", Requirements -> suitable candidates, sorted by match %) -> 4 Candidate Inspection (profile, education, skills, verified skills, projects, certificates, experience; no unnecessary private data) -> 5 Match Explanation (matched / concern / missing with icon+label+colour; factor-based, never just a number; do not claim a trained model) -> 6 Evidence, Confidence, Skill details -> 7 Shortlist / Give Feedback.
PRIVACY: structure state by companyId; every list/count/chart filters by the logged-in company. Company A never sees Company B's positions, requirements, candidates, shortlist, feedback or analytics.

UNIVERSITY (fixed order)
1 Current Industry Skill Demand (first, detailed): most demanded, emerging, role-wise, industry-wise, trend, "Sample demand data - Last updated {date}", a "Refresh demo data" button that changes demand and recomputes everything below. Never say live/real-time.
2 Curriculum Gap Analysis: demand vs coverage per skill, gap status, recommendations tied to gaps.
3 Industry Alignment Ranking (University Benchmark): 10 universities, rank + score. Own row highlighted and expandable (score explanation, gaps, recommendations). Other universities: rank and score ONLY. Never "Best University".
Placement/internship analytics: keep only as a small secondary section at the bottom. REMOVE cards "Curriculum Health", "Priority Action", "Outcome Feedback".

SKILL GRAPH
KEEP the current interactive Skill Graph exactly (design and interactions). The ONLY change: in the selected-skill info panel remove the bottom items "Curriculum link", "Related Roles", "Aligned Opportunities". Nothing else.

DEMO DATA (coherent; compute all scores in code from the data, never hard-code)
Match = round(70 x required matched/required + 20 x preferred matched/preferred + 10 x verified matched/matched).
Alignment = sum(demand x coverage) / sum(demand).
Use this dataset (fictional):
- Demand index: Python 95, SQL 90, Machine Learning 85, Cloud 88, Docker 78, Generative AI 72, Data Visualization 70, Git 65.
- Your University coverage: Python 95, SQL 90, ML 80, Cloud 60, Docker 45, GenAI 45, Data Viz 85, Git 85 -> alignment 74%, rank #3. After "Refresh demo data" (Cloud 90, Docker 80, GenAI 76) -> 73%, still #3.
- Benchmark: A 86, B 82, Your University 74, C 71, D 69, E 66, F 63, G 60, H 57, I 52.
- Student Meera Iyer: Python (Adv, verified), SQL (Adv, verified), Pandas (Int, verified), ML (Int, verified), Data Viz (Int, verified), Docker (Int, unverified project); no AWS; Communication has no verified evidence (concern only).
- Positions: P1 Orbis Analytics, Data Science Intern, Bengaluru, Hybrid, 6 months, Rs 30,000/month; req Python, SQL, Pandas, ML; pref AWS, Docker. P2 Kestrel Retail Tech, Data Analyst Intern, Pune, Remote; req SQL, Python, Data Viz; pref Excel, Statistics. P3 Northline Cloud Systems, Junior ML Engineer, Hyderabad, On-site, Rs 7-9 LPA; req Python, ML, Docker, AWS; pref Kubernetes, SQL. P4 Veridian Health Data, Backend Developer Intern, Remote; req Python, SQL, REST APIs, Git; pref Flask, Docker.
- Expected Meera matches: P1 88, P2 80, P3 70, P4 52.
- Orbis candidates for P1: Meera 88 (High confidence), Kavya Nair 79 (Medium), Rohan Das 78 (High), Sahil Verma 40 (Medium).
- Demo accounts (simulated): student meera.iyer@student.example.edu; industry hiring@orbis-analytics.example.com and hiring@kestrel-retail.example.com; university industry.cell@youruniversity.example.edu; password Demo@1234.

HONESTY
All scores, demand figures and matches are sample data. Do not claim a trained ML model, live market data, perfect/accurate AI, guaranteed jobs, or production authentication. Prefer wording: Match Explanation, evidence, verified, transparent scoring. Where relevant: "Matching is based on available data and evidence."

CODE QUALITY
Reusable components, consistent naming, no duplicated JSX blocks, no dead code or dead navigation, no unused buttons. Keep readable. Preserve existing interactions.

FINISH
When done, audit every screen for: branding/removals, section order, role isolation, blurred preview, responsive layout, focus states, and consistent data (scores must match the visible skills). Fix anything inconsistent. Then summarise what changed, in a short list.
````

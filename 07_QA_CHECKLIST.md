# 07 — QA Checklist

Inspect every visible screen before calling the work complete. Tick each item only after checking it in the running page.

## Branding
- [ ] SkillBridge branding everywhere
- [ ] Final supplied logo used, unchanged
- [ ] No SIH / Smart India Hackathon / problem statement IDs
- [ ] No Gamma or Gamma-style wording
- [ ] No "Academia–Industry Platform" or "Skill Intelligence Ecosystem"
- [ ] No Section 1–5 labels
- [ ] No Career Hub / Credentials / Recruiting / Academic Insights / Skill Tracking Center labels
- [ ] No mention of the tools used to build the UI
- [ ] Tooltips, page titles, alt text and aria-labels are also clean

## Header and navigation
- [ ] Logo + "SkillBridge" on the left
- [ ] Profile photo (not clickable) + hamburger on the right
- [ ] Hamburger contains exactly My Profile, Why SkillBridge?, Logout
- [ ] Menu closes on outside click and Esc
- [ ] Logout returns to public Home
- [ ] No dead nav items or buttons pointing to deleted pages

## Home
- [ ] Compact hero with the required wording
- [ ] University | Industry | Student in one row
- [ ] Large interactive Skill Graph below
- [ ] Nothing below the graph
- [ ] No tables, salary data, statistics or comparison content

## Student
- [ ] Order: Opportunities For Me → results → Market Intelligence → Improvement Plan → Skill Passport
- [ ] Search by roles, skills, companies
- [ ] Job/Internship, Preferred Location, Work Mode filters work
- [ ] Empty state shown first; results appear only after search or filter change
- [ ] Minimum Package removed
- [ ] Desired Role filter removed
- [ ] "Curated AI Recommendations" removed
- [ ] "Matching candidate: …" sentence removed
- [ ] Market Intelligence retained and compact
- [ ] Improvement Plan retained, unchanged in content
- [ ] Skill Passport retained, unchanged in content
- [ ] Public preview: headings visible, only data blurred
- [ ] Clicking blurred data shows "Login to access your personalized student data."

## Industry
- [ ] Order: Post New Position → Requirements → Find Candidates → Candidate Inspection → Match Explanation → Evidence/Confidence → Shortlist/Feedback
- [ ] Required and Preferred skills shown clearly
- [ ] Candidates sorted by match %, scores computed from data
- [ ] Match Explanation shows matched, concern and missing with icon + label + colour
- [ ] Confidence and evidence shown per skill
- [ ] No unnecessary private candidate data
- [ ] Logged in as Orbis: no Kestrel positions, candidates, shortlist, feedback or analytics
- [ ] Logged in as Kestrel: no Orbis data

## University
- [ ] Order: Industry Skill Demand → Curriculum Gap Analysis → Alignment Ranking
- [ ] Demand labelled "Sample demand data" with a last-updated date
- [ ] Refresh demo data recomputes gaps, recommendations and score (74 → 73, rank stays #3)
- [ ] Recommendations tied to specific gaps
- [ ] 10 universities in the benchmark; own row highlighted and expandable
- [ ] Other universities: rank and score only
- [ ] Never labelled "Best University"
- [ ] Placement/internship analytics secondary, at the bottom
- [ ] Curriculum Health removed
- [ ] Priority Action removed
- [ ] Outcome Feedback removed

## Profile
- [ ] My Profile reachable from the hamburger
- [ ] Same information and arrangement as the old Student Details
- [ ] Personal Details
- [ ] Academic & Professional Details
- [ ] AI Resume Skill Extractor
- [ ] Verified Documents
- [ ] Student Portfolio
- [ ] Edit Information with save and cancel
- [ ] Company and University profile versions work

## Why SkillBridge?
- [ ] Problem explanation
- [ ] Industry Demand → Curriculum Analysis → Student Skill Gap → Career Opportunities
- [ ] For Universities / For Industry / For Students
- [ ] Closing statement present
- [ ] No LinkedIn comparison, no tech stack, no statistics

## Skill Graph
- [ ] Still interactive, design preserved
- [ ] "Curriculum link" removed
- [ ] "Related Roles" removed
- [ ] "Aligned Opportunities" removed
- [ ] Nothing else changed
- [ ] Fits the viewport on mobile

## Authentication
- [ ] Login with email/password, Forgot Password, Sign Up
- [ ] Signup for Student, University and Industry, each with the right fields
- [ ] Validation messages are clear
- [ ] Role-aware dashboard after login
- [ ] No claim of production security

## Data consistency
- [ ] Match scores computed from skills and requirements (Meera: P1 88, P2 80, P3 70, P4 52)
- [ ] Orbis candidates: Meera 88, Kavya 79, Rohan 78, Sahil 40
- [ ] Alignment 74% matches the coverage table
- [ ] Opportunity cards match position requirements
- [ ] Everything labelled as sample data; nothing called live or model-generated

## Visual design
- [ ] No gradients, glow, neon, purple or glassmorphism
- [ ] Palette: navy, blue, muted teal on neutral backgrounds
- [ ] Radius 6/8/12px only, shadows subtle
- [ ] Consistent spacing and typography
- [ ] Tables, lists and panels used instead of cards everywhere
- [ ] Hover, focus, active, disabled states present
- [ ] Animations short and functional; reduced-motion respected

## Responsive and accessibility
- [ ] Checked at 1440, 1024, 768 and 390 px: no overflow or overlap
- [ ] Tables scroll inside wrappers
- [ ] Labels on all form fields
- [ ] Visible focus ring everywhere
- [ ] Modals trap focus and close on Esc
- [ ] Contrast at least 4.5:1 for text
- [ ] Status never relies on colour alone

## Final impression
- [ ] It looks like a real software product built by an experienced team, not an AI-generated site or a presentation

# SkillBridge — Vibe-Coding Pack

This pack turns the SkillBridge brief into files you can feed to a vibe-coding platform (Lovable, Bolt, v0, Replit, Cursor, Claude Code, etc.).

| File | Purpose |
|---|---|
| `01_PROJECT_OVERVIEW.md` | What SkillBridge is, stakeholders, branding rules, privacy rules, tech direction, honesty rules |
| `02_DESIGN_SYSTEM.md` | Colour combination, typography, spacing, components, accessibility, "avoid" list. Includes CSS variables and Tailwind config |
| `03_PAGES_AND_FLOWS.md` | Page-by-page specification: header, home, auth, student, industry, university, profile, Why SkillBridge, skill graph |
| `04_DEMO_DATA_AND_ARCHITECTURE.md` | One coherent demo dataset with the formulas behind every number, state shape for data isolation, future Flask/SQLite design |
| `05_MASTER_PROMPT.md` | One self-contained prompt to paste into the platform |
| `06_PHASED_PROMPTS.md` | The same work split into 11 smaller prompts, to run in order |
| `07_QA_CHECKLIST.md` | Final inspection checklist |

## How to use

**Option A — single shot**
1. Upload or paste the current `PROTOTYPE_FINAL (2).html`.
2. Upload the final SkillBridge logo file (the platform must use it as-is).
3. Paste `05_MASTER_PROMPT.md`.
4. Attach `02_DESIGN_SYSTEM.md`, `03_PAGES_AND_FLOWS.md` and `04_DEMO_DATA_AND_ARCHITECTURE.md` as reference files.

**Option B — phased (recommended if the platform loses detail on long prompts)**
1. Do the same uploads as above.
2. Run the prompts in `06_PHASED_PROMPTS.md` one at a time, in order. Check the result before moving on.
3. Finish with `07_QA_CHECKLIST.md`.

## Ground rules that apply to every prompt

- Edit the existing file. Do not rewrite the app from scratch.
- Keep React 18 + Tailwind CDN + Recharts in the current frontend.
- Demo data is demo data. Never present it as a trained model or live market data.
- No SIH, hackathon, Gamma, LinkedIn-comparison or old-branding text anywhere in the UI.

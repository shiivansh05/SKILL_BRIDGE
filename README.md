# SkillBridge - Dynamic Curriculum & Opportunity Alignment Platform

SkillBridge is an enterprise-grade platform that aligns student skills, university curricula, and industry hiring requirements using quantitative matching formulas and transparent, auditable algorithms.

---

## 📁 Project Architecture & Folder Separation

As requested, this project is cleanly separated into three modular directories, keeping `PROTOTYPE_FINAL (2).html` untouched and independent:

```
├── dataset/                    # Data Layer (Taxonomy, Benchmarks, SQLite DB)
│   ├── skills.json             # Canonical skill taxonomy (11 skills, aliases, categories)
│   ├── industry_demand.json    # Market demand weights (baseline & refreshed states)
│   ├── curriculum.json         # University course coverage & 10-institution benchmark
│   ├── positions.json          # Industry opportunities (P1 Orbis, P2 Kestrel, P3, P4)
│   ├── students.json           # Profiles for Meera Iyer & reverse-matching candidates
│   ├── init_db.py              # SQLite schema builder & database seeder
│   └── skillbridge.sqlite      # Active relational SQLite database
│
├── backend/                    # Backend Layer (Python / Flask REST API)
│   ├── config.py               # Path configurations & environment settings
│   ├── database.py             # SQLite query execution helpers & connection manager
│   ├── intelligence.py         # Core mathematical calculation engines (exact formulas)
│   ├── models.py               # Data access layer with strict company & university isolation
│   ├── app.py                  # Flask REST API endpoints (Port 5000)
│   └── requirements.txt        # Backend dependencies (Flask, Flask-CORS)
│
├── frontend/                   # Frontend Layer (Modern Enterprise SPA)
│   ├── index.html              # React 18 + Tailwind CDN + Recharts SPA
│   ├── css/
│   │   └── style.css           # Design tokens, IBM Plex Sans typography, semantic badges
│   ├── js/
│   │   └── api.js              # Unified API client with automatic graceful fallback
│   └── logo.png                # Official SkillBridge branding logo
│
├── PROTOTYPE_FINAL (2).html    # Original reference prototype (UNTOUCHED)
├── run_backend.bat             # One-click script to start Flask backend
├── run_frontend.bat            # One-click script to serve frontend on http://localhost:8000
└── run_all.bat                 # One-click script to launch both backend & frontend
```

---

## 🚀 How to Run

### Quick Start (Windows)
Double-click `run_all.bat` to launch both the backend API and frontend web server in separate windows.

### Manual Launch

#### 1. Backend (Flask REST API on Port 5000)
```powershell
# Optional: install dependencies if needed
python -m pip install -r backend/requirements.txt

# Run backend
python backend/app.py
```
Backend API will be running at `http://localhost:5000`. Test health: `http://localhost:5000/api/health`.

#### 2. Frontend (Port 8000)
```powershell
# Serve frontend folder
cd frontend
python -m http.server 8000
```
Open `http://localhost:8000` in any web browser. You can also open `frontend/index.html` directly.

---

## 🔑 Demo Login Credentials

All demo accounts share the password: `Demo@1234`

| Role | Email | Organization / User | Scope / Access Rules |
| :--- | :--- | :--- | :--- |
| **Student** | `student@university.edu` | Meera Iyer (B.Tech CS, Sem 6) | Student Dashboard, Applications, Passport, Market Trends |
| **Industry (P1)** | `recruiter@orbis.com` | Orbis Analytics | **Strict Isolation**: Sees P1 position, candidate rankings, shortlist |
| **Industry (P2)** | `recruiter@kestrel.com` | Kestrel Retail Tech | **Strict Isolation**: Sees P2 position only; cannot access Orbis candidates |
| **University** | `dean@university.edu` | Your University | Alignment Score (74% baseline $\to$ 73% refreshed), Curriculum Gaps, 10-School Benchmark |

---

## 📐 Quantitative Engines & Formulas Implemented

### 1. Candidate Match Formula
$$\text{Candidate Match} = \text{round}\left(70 \times \frac{\text{Required Matched}}{\text{Required Total}} + 20 \times \frac{\text{Preferred Matched}}{\text{Preferred Total}} + 10 \times \frac{\text{Verified Matched}}{\text{Total Matched}}\right)$$
- Implemented in `backend/intelligence.py` (`calculate_match_score`).
- Factors: Required Skills (70%), Preferred Skills (20%), Verification / Evidence (10%).

### 2. University Institutional Alignment Score
$$\text{Alignment Score} = \text{round}\left(\frac{\sum (\text{Demand Index} \times \text{Coverage Score})}{\sum \text{Demand Index}}\right)$$
- Baseline: **74%**
- Refreshed: **73%** (when Cloud shifts to 90, Docker to 80, GenAI to 76)
- Implemented in `backend/intelligence.py` (`calculate_alignment_score`).

---

## 🔒 Security & Data Isolation Enforced

1. **Company Isolation**:
   - Orbis Analytics can only query position `P1` and its candidates (`Meera Iyer`, `Kavya Nair`, `Rohan Das`, `Sahil Verma`).
   - Kestrel Retail Tech can only query position `P2` and its candidates (`Ananya Roy`, `Tarun Joshi`).
   - Cross-company candidate inspection returns zero candidates.
2. **University Benchmark Privacy**:
   - The user's own university row shows rank, full name, score, and gap breakdown.
   - Other 9 universities show rank and score only, preserving institutional confidentiality.
3. **No Unauthenticated Leaks**:
   - Student dashboard, Opportunity match scores, and Improvement plan are protected behind login with blurred previews and login CTA modals.

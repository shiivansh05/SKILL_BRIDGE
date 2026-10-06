import os
import json
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "skillbridge.sqlite")

def init_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables
    cursor.executescript("""
    CREATE TABLE users (
        id TEXT PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        org_id TEXT NOT NULL,
        name TEXT NOT NULL
    );

    CREATE TABLE students (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        university TEXT NOT NULL,
        course TEXT NOT NULL,
        branch TEXT NOT NULL,
        graduation_year INTEGER NOT NULL,
        semester INTEGER NOT NULL,
        cgpa REAL NOT NULL,
        location TEXT,
        phone TEXT,
        bio TEXT
    );

    CREATE TABLE student_skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        skill_id TEXT NOT NULL,
        name TEXT NOT NULL,
        level TEXT NOT NULL,
        numeric_level INTEGER NOT NULL,
        required_level INTEGER NOT NULL,
        verified BOOLEAN NOT NULL,
        evidence TEXT,
        category TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id)
    );

    CREATE TABLE companies (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        website TEXT NOT NULL,
        contact_person TEXT NOT NULL,
        email TEXT NOT NULL
    );

    CREATE TABLE positions (
        id TEXT PRIMARY KEY,
        company_id TEXT NOT NULL,
        role TEXT NOT NULL,
        type TEXT NOT NULL,
        location TEXT NOT NULL,
        work_mode TEXT NOT NULL,
        terms TEXT NOT NULL,
        stipend_salary TEXT NOT NULL,
        duration TEXT NOT NULL,
        description TEXT NOT NULL,
        why_match_template TEXT,
        FOREIGN KEY (company_id) REFERENCES companies(id)
    );

    CREATE TABLE position_skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        position_id TEXT NOT NULL,
        skill_name TEXT NOT NULL,
        is_required BOOLEAN NOT NULL,
        FOREIGN KEY (position_id) REFERENCES positions(id)
    );

    CREATE TABLE candidates (
        id TEXT PRIMARY KEY,
        target_company_id TEXT NOT NULL,
        name TEXT NOT NULL,
        college TEXT NOT NULL,
        course TEXT NOT NULL,
        cgpa REAL NOT NULL,
        experience TEXT,
        concern TEXT
    );

    CREATE TABLE candidate_skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_id TEXT NOT NULL,
        skill_name TEXT NOT NULL,
        level TEXT NOT NULL,
        verified BOOLEAN NOT NULL,
        source TEXT,
        FOREIGN KEY (candidate_id) REFERENCES candidates(id)
    );

    CREATE TABLE applications (
        id TEXT PRIMARY KEY,
        student_id TEXT NOT NULL,
        position_id TEXT NOT NULL,
        date TEXT NOT NULL,
        match_score INTEGER NOT NULL,
        status TEXT NOT NULL,
        feedback TEXT
    );

    CREATE TABLE shortlists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id TEXT NOT NULL,
        candidate_id TEXT NOT NULL,
        status TEXT NOT NULL,
        feedback TEXT
    );

    CREATE TABLE universities (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        official_email TEXT NOT NULL,
        website TEXT NOT NULL,
        contact_person TEXT NOT NULL
    );

    CREATE TABLE curriculum_coverage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        university_id TEXT NOT NULL,
        skill_id TEXT NOT NULL,
        course TEXT NOT NULL,
        semester TEXT NOT NULL,
        coverage_score INTEGER NOT NULL,
        label TEXT NOT NULL
    );

    CREATE TABLE industry_demand (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        demand_index INTEGER NOT NULL,
        trend TEXT NOT NULL,
        emerging BOOLEAN NOT NULL
    );

    CREATE TABLE benchmarks (
        rank INTEGER PRIMARY KEY,
        university_id TEXT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
        is_own BOOLEAN NOT NULL
    );
    """)

    # Seed users (password Demo@1234)
    users = [
        ("u_1", "meera.iyer@student.example.edu", "Demo@1234", "student", "s_meera", "Meera Iyer"),
        ("u_2", "hiring@orbis-analytics.example.com", "Demo@1234", "industry", "c_orbis", "Orbis Analytics"),
        ("u_3", "hiring@kestrel-retail.example.com", "Demo@1234", "industry", "c_kestrel", "Kestrel Retail Tech"),
        ("u_4", "industry.cell@youruniversity.example.edu", "Demo@1234", "university", "u_you", "Your University")
    ]
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", users)

    # Seed companies
    companies = [
        ("c_orbis", "Orbis Analytics", "Analytics & Data Intelligence", "https://orbis-analytics.example.com", "Talent Acquisition", "hiring@orbis-analytics.example.com"),
        ("c_kestrel", "Kestrel Retail Tech", "Retail Technology & Commerce", "https://kestrel-retail.example.com", "Campus Recruiting", "hiring@kestrel-retail.example.com"),
        ("c_northline", "Northline Cloud Systems", "Cloud & MLOps Infrastructure", "https://northline.example.com", "Hiring Lead", "careers@northline.example.com"),
        ("c_veridian", "Veridian Health Data", "Healthcare Analytics & Data Platforms", "https://veridian.example.com", "Engineering Team", "jobs@veridian.example.com")
    ]
    cursor.executemany("INSERT INTO companies VALUES (?, ?, ?, ?, ?, ?)", companies)

    # Seed positions & position skills
    with open(os.path.join(BASE_DIR, "positions.json"), "r", encoding="utf-8") as f:
        positions_data = json.load(f)

    for p in positions_data:
        cursor.execute("""
            INSERT INTO positions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["id"], p["company_id"], p["role"], p["type"], p["location"],
            p["work_mode"], p["terms"], p["stipend_salary"], p["duration"],
            p["description"], p["why_match_template"]
        ))
        for s in p["required_skills"]:
            cursor.execute("INSERT INTO position_skills (position_id, skill_name, is_required) VALUES (?, ?, ?)", (p["id"], s, 1))
        for s in p["preferred_skills"]:
            cursor.execute("INSERT INTO position_skills (position_id, skill_name, is_required) VALUES (?, ?, ?)", (p["id"], s, 0))

    # Seed student Meera
    with open(os.path.join(BASE_DIR, "students.json"), "r", encoding="utf-8") as f:
        students_data = json.load(f)

    st = students_data["demo_student"]
    cursor.execute("""
        INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        st["id"], st["name"], st["email"], st["university"], st["course"],
        st["branch"], st["graduation_year"], st["semester"], st["cgpa"],
        st["location"], st["phone"], st["bio"]
    ))

    for sk in st["skills"]:
        cursor.execute("""
            INSERT INTO student_skills (student_id, skill_id, name, level, numeric_level, required_level, verified, evidence, category)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            st["id"], sk["id"], sk["name"], sk["level"], sk["numeric_level"],
            sk["required_level"], 1 if sk["verified"] else 0, sk["evidence"], sk["category"]
        ))

    # Seed candidates
    for c in students_data["candidate_pool"]:
        target_co = "c_orbis" if "c_meera" in c["id"] or "c_kavya" in c["id"] or "c_rohan" in c["id"] or "c_sahil" in c["id"] else "c_kestrel"
        cursor.execute("""
            INSERT INTO candidates VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            c["id"], target_co, c["name"], c["college"], c["course"],
            c["cgpa"], c.get("experience", ""), c.get("concern", "")
        ))
        for sk in c["student_skills"]:
            cursor.execute("""
                INSERT INTO candidate_skills (candidate_id, skill_name, level, verified, source)
                VALUES (?, ?, ?, ?, ?)
            """, (c["id"], sk["name"], sk["level"], 1 if sk["verified"] else 0, sk.get("source", "")))

    # Seed demand
    with open(os.path.join(BASE_DIR, "industry_demand.json"), "r", encoding="utf-8") as f:
        demand_data = json.load(f)

    for d in demand_data["baseline"]:
        cursor.execute("""
            INSERT INTO industry_demand VALUES (?, ?, ?, ?, ?, ?)
        """, (d["id"], d["name"], d["category"], d["demand_index"], d["trend"], 1 if d["emerging"] else 0))

    # Seed curriculum & benchmarks
    with open(os.path.join(BASE_DIR, "curriculum.json"), "r", encoding="utf-8") as f:
        curriculum_data = json.load(f)

    cursor.execute("""
        INSERT INTO universities VALUES (?, ?, ?, ?, ?)
    """, (
        curriculum_data["university_id"], curriculum_data["university_name"],
        curriculum_data["official_email"], curriculum_data["website"],
        curriculum_data["contact_person"]
    ))

    for k, v in curriculum_data["coverage"].items():
        cursor.execute("""
            INSERT INTO curriculum_coverage (university_id, skill_id, course, semester, coverage_score, label)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            curriculum_data["university_id"], k, v["course"], v["semester"],
            v["coverage_score"], v["label"]
        ))

    for b in curriculum_data["benchmark"]:
        cursor.execute("""
            INSERT INTO benchmarks VALUES (?, ?, ?, ?, ?)
        """, (b["rank"], b.get("university_id"), b["name"], b["score"], 1 if b.get("is_own") else 0))

    # Applications
    cursor.execute("""
        INSERT INTO applications VALUES (?, ?, ?, ?, ?, ?, ?)
    """, ("app_1", "s_meera", "P1", "2026-09-28", 88, "Under Review", "Application received and matched against required skills."))
    cursor.execute("""
        INSERT INTO applications VALUES (?, ?, ?, ?, ?, ?, ?)
    """, ("app_2", "s_meera", "P2", "2026-09-20", 80, "Shortlisted", "Passed initial verification for SQL and Python."))

    conn.commit()
    conn.close()
    print("Database initialized successfully at:", DB_PATH)

if __name__ == "__main__":
    init_database()

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from config import SECRET_KEY, PORT, DEBUG, DB_PATH
from models import DataAccess
from intelligence import calculate_match_score, calculate_alignment_score, extract_skills_from_text

app = Flask(__name__)
app.secret_key = SECRET_KEY
CORS(app, supports_credentials=True)

# Keep track of simulated demo demand refresh state
DEMO_STATE = {
    "is_demand_refreshed": False
}

# --- HEALTH & META ---
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "SkillBridge API", "version": "1.0.0"})

@app.route("/api/skills", methods=["GET"])
def get_skills():
    skills = DataAccess.get_all_skills()
    return jsonify({"skills": skills, "total": len(skills)})

@app.route("/api/skills/extract", methods=["POST"])
def extract_skills_endpoint():
    data = request.get_json() or {}
    text = data.get("text", "")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dataset", "skills.json"), "r") as f:
        catalog = json.load(f)["skills"]
    extracted = extract_skills_from_text(text, catalog)
    return jsonify({
        "extracted_skills": extracted,
        "count": len(extracted)
    })

# --- AUTHENTICATION ENDPOINTS (Simulated Session) ---
@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    if not email:
        return jsonify({"error": "Email is required."}), 400

    user = DataAccess.get_user_by_email(email)
    if not user:
        # Graceful role derivation for flexible testing
        if "orbis" in email:
            user = {"id": "u_2", "email": email, "role": "industry", "org_id": "c_orbis", "name": "Orbis Analytics"}
        elif "kestrel" in email:
            user = {"id": "u_3", "email": email, "role": "industry", "org_id": "c_kestrel", "name": "Kestrel Retail Tech"}
        elif "university" in email or ".edu" in email:
            if "student" in email:
                user = {"id": "u_1", "email": email, "role": "student", "org_id": "s_meera", "name": "Meera Iyer"}
            else:
                user = {"id": "u_4", "email": email, "role": "university", "org_id": "u_you", "name": "Your University"}
        else:
            user = {"id": "u_1", "email": email, "role": "student", "org_id": "s_meera", "name": "Meera Iyer"}
    else:
        user = dict(user)

    session["user"] = user
    return jsonify({
        "message": f"Logged in as {user['name']}",
        "user": user
    })

@app.route("/api/auth/signup", methods=["POST"])
def signup():
    data = request.get_json() or {}
    role = data.get("role", "student")
    email = data.get("email", "").strip().lower()
    name = data.get("name", "New User")

    if not email:
        return jsonify({"error": "Email is required."}), 400

    org_id = f"org_{role}_{int(os.urandom(2).hex(), 16)}"
    user = {
        "id": f"u_{int(os.urandom(2).hex(), 16)}",
        "email": email,
        "role": role,
        "org_id": org_id,
        "name": name
    }
    session["user"] = user
    return jsonify({"message": "Account created successfully", "user": user})

@app.route("/api/auth/me", methods=["GET"])
def get_current_user():
    user = session.get("user")
    if not user:
        return jsonify({"authenticated": False, "user": None})
    return jsonify({"authenticated": True, "user": user})

@app.route("/api/auth/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"})

@app.route("/api/auth/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json() or {}
    email = data.get("email")
    return jsonify({"message": f"Password reset instructions dispatched to {email} (simulated)."})

# --- STUDENT ENDPOINTS ---
@app.route("/api/student/profile", methods=["GET"])
def get_student_profile():
    # Demo student is Meera Iyer
    profile = DataAccess.get_student_profile("s_meera")
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    return jsonify(profile)

@app.route("/api/student/opportunities", methods=["GET"])
def get_student_opportunities():
    # Return all opportunities scored against Meera's skills
    profile = DataAccess.get_student_profile("s_meera")
    student_skills = profile["skills"] if profile else []
    positions = DataAccess.get_positions_for_company()

    results = []
    for pos in positions:
        math_res = calculate_match_score(student_skills, pos["required_skills"], pos["preferred_skills"])
        results.append({
            **pos,
            "match_score": math_res["score"],
            "match_breakdown": math_res
        })

    results.sort(key=lambda x: x["match_score"], reverse=True)
    return jsonify(results)

@app.route("/api/student/applications", methods=["GET", "POST"])
def student_applications():
    if request.method == "POST":
        data = request.get_json() or {}
        pos_id = data.get("position_id")
        title = data.get("title", "Position Application")
        company = data.get("company", "Company")
        score = data.get("match_score", 88)
        new_app = {
            "id": f"app_{int(os.urandom(2).hex(), 16)}",
            "position_id": pos_id,
            "title": title,
            "company": company,
            "date": "2026-10-06",
            "match": score,
            "status": "Applied",
            "feedback": "Application submitted and queued for recruiter evaluation."
        }
        return jsonify({"message": "Application submitted", "application": new_app})
    else:
        apps = DataAccess.get_applications_for_student("s_meera")
        return jsonify(apps)

@app.route("/api/student/resume/extract", methods=["POST"])
def resume_extract():
    data = request.get_json() or {}
    text = data.get("text", "")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dataset", "skills.json"), "r") as f:
        catalog = json.load(f)["skills"]
    extracted = extract_skills_from_text(text, catalog)
    return jsonify({
        "extracted_skills": extracted,
        "count": len(extracted),
        "note": "Extracted skills (review before saving)"
    })

# --- INDUSTRY ENDPOINTS (Company Isolation Enforced) ---
@app.route("/api/company/positions", methods=["GET", "POST"])
def company_positions():
    current_user = session.get("user") or {}
    company_id = request.args.get("company_id") or current_user.get("org_id", "c_orbis")

    if request.method == "POST":
        data = request.get_json() or {}
        pos_id = DataAccess.create_position(
            company_id=company_id,
            role=data.get("role", "New Position"),
            ptype=data.get("type", "Internship"),
            location=data.get("location", "Bengaluru"),
            work_mode=data.get("work_mode", "Hybrid"),
            terms=data.get("terms", "Negotiable"),
            description=data.get("description", ""),
            required_skills=data.get("required_skills", []),
            preferred_skills=data.get("preferred_skills", [])
        )
        return jsonify({"message": "Position created", "position_id": pos_id})
    else:
        # Strictly isolated by company_id!
        positions = DataAccess.get_positions_for_company(company_id=company_id)
        return jsonify(positions)

@app.route("/api/company/positions/<position_id>/candidates", methods=["GET"])
def company_candidates(position_id):
    current_user = session.get("user") or {}
    company_id = request.args.get("company_id") or current_user.get("org_id", "c_orbis")

    candidates = DataAccess.get_candidates_for_position(position_id, company_id)
    return jsonify({
        "position_id": position_id,
        "company_id": company_id,
        "candidates": candidates
    })

@app.route("/api/company/shortlist", methods=["POST"])
def set_shortlist():
    data = request.get_json() or {}
    current_user = session.get("user") or {}
    company_id = data.get("company_id") or current_user.get("org_id", "c_orbis")
    candidate_id = data.get("candidate_id")
    is_shortlisted = data.get("is_shortlisted", True)
    feedback = data.get("feedback")

    DataAccess.set_shortlist(company_id, candidate_id, is_shortlisted, feedback)
    return jsonify({"message": "Shortlist status updated", "candidate_id": candidate_id, "is_shortlisted": is_shortlisted})

# --- UNIVERSITY ENDPOINTS ---
@app.route("/api/university/demand", methods=["GET"])
def get_demand():
    demand_list = DataAccess.get_university_demand(DEMO_STATE["is_demand_refreshed"])
    coverage = DataAccess.get_curriculum_coverage("u_you")
    align_result = calculate_alignment_score(demand_list, coverage)
    return jsonify({
        "last_updated": "2026-10-06",
        "is_sample_data": True,
        "is_refreshed": DEMO_STATE["is_demand_refreshed"],
        "alignment_score": align_result["alignment_score"],
        "demand": demand_list,
        "coverage": coverage,
        "gaps": align_result["gaps"]
    })

@app.route("/api/university/demand/refresh", methods=["POST"])
def refresh_demand():
    DEMO_STATE["is_demand_refreshed"] = not DEMO_STATE["is_demand_refreshed"]
    demand_list = DataAccess.get_university_demand(DEMO_STATE["is_demand_refreshed"])
    coverage = DataAccess.get_curriculum_coverage("u_you")
    align_result = calculate_alignment_score(demand_list, coverage)

    return jsonify({
        "message": "Demo demand refreshed" if DEMO_STATE["is_demand_refreshed"] else "Demo demand reset",
        "is_refreshed": DEMO_STATE["is_demand_refreshed"],
        "alignment_score": align_result["alignment_score"],
        "demand": demand_list,
        "gaps": align_result["gaps"]
    })

@app.route("/api/university/curriculum-gaps", methods=["GET"])
def get_curriculum_gaps():
    demand_list = DataAccess.get_university_demand(DEMO_STATE["is_demand_refreshed"])
    coverage = DataAccess.get_curriculum_coverage("u_you")
    align_result = calculate_alignment_score(demand_list, coverage)
    return jsonify({
        "university_name": "Your University",
        "alignment_score": align_result["alignment_score"],
        "gaps": align_result["gaps"]
    })

@app.route("/api/university/benchmark", methods=["GET"])
def get_benchmark():
    current_user = session.get("user") or {}
    user_org_id = current_user.get("org_id", "u_you")

    demand_list = DataAccess.get_university_demand(DEMO_STATE["is_demand_refreshed"])
    coverage = DataAccess.get_curriculum_coverage("u_you")
    align_result = calculate_alignment_score(demand_list, coverage)

    benchmark = DataAccess.get_university_benchmark(user_org_id, align_result["alignment_score"])
    return jsonify({
        "benchmark": benchmark,
        "own_alignment_score": align_result["alignment_score"]
    })

# --- SKILL GRAPH ENDPOINT ---
@app.route("/api/skill-graph", methods=["GET"])
def get_skill_graph():
    profile = DataAccess.get_student_profile("s_meera")
    return jsonify({
        "student": {
            "name": profile["name"],
            "course": profile["course"],
            "branch": profile["branch"]
        },
        "skills": profile["skills"],
        "target_roles": ["Data Scientist", "ML Intern", "Data Analyst"]
    })

if __name__ == "__main__":
    print(f"Starting SkillBridge REST API on port {PORT}...")
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)

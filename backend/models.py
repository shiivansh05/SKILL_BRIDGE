import os
import json
from database import query_db, execute_db
from intelligence import calculate_match_score, calculate_alignment_score

class DataAccess:
    @staticmethod
    def get_user_by_email(email):
        return query_db("SELECT * FROM users WHERE email = ?", (email,), one=True)

    @staticmethod
    def get_all_skills():
        json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dataset", "skills.json")
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f).get("skills", [])
        except Exception:
            return []

    @staticmethod
    def get_student_profile(student_id):
        student = query_db("SELECT * FROM students WHERE id = ?", (student_id,), one=True)
        if not student:
            return None
        skills = query_db("SELECT * FROM student_skills WHERE student_id = ?", (student_id,))
        return {
            **dict(student),
            "skills": [dict(s) for s in skills]
        }

    @staticmethod
    def get_positions_for_company(company_id=None):
        """
        Enforce Company Isolation:
        If company_id is provided, only return positions belonging to that company.
        """
        if company_id:
            rows = query_db("SELECT p.*, c.name as company_name FROM positions p JOIN companies c ON p.company_id = c.id WHERE p.company_id = ?", (company_id,))
        else:
            rows = query_db("SELECT p.*, c.name as company_name FROM positions p JOIN companies c ON p.company_id = c.id")

        positions = []
        for r in rows:
            pos_id = r["id"]
            req_skills = query_db("SELECT skill_name FROM position_skills WHERE position_id = ? AND is_required = 1", (pos_id,))
            pref_skills = query_db("SELECT skill_name FROM position_skills WHERE position_id = ? AND is_required = 0", (pos_id,))
            positions.append({
                **dict(r),
                "required_skills": [s["skill_name"] for s in req_skills],
                "preferred_skills": [s["skill_name"] for s in pref_skills]
            })
        return positions

    @staticmethod
    def create_position(company_id, role, ptype, location, work_mode, terms, description, required_skills, preferred_skills):
        pos_id = f"P_{company_id}_{role.replace(' ', '_')}"
        execute_db("""
            INSERT INTO positions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (pos_id, company_id, role, ptype, location, work_mode, terms, terms, "Flexible", description, "Position requirements recorded."))

        for sk in required_skills:
            execute_db("INSERT INTO position_skills (position_id, skill_name, is_required) VALUES (?, ?, ?)", (pos_id, sk, 1))
        for sk in preferred_skills:
            execute_db("INSERT INTO position_skills (position_id, skill_name, is_required) VALUES (?, ?, ?)", (pos_id, sk, 0))

        return pos_id

    @staticmethod
    def get_candidates_for_position(position_id, company_id):
        """
        Enforce Company Isolation:
        Only evaluate candidates for positions owned by company_id.
        """
        pos = query_db("SELECT * FROM positions WHERE id = ? AND company_id = ?", (position_id, company_id), one=True)
        if not pos:
            return []

        req_skills = [s["skill_name"] for s in query_db("SELECT skill_name FROM position_skills WHERE position_id = ? AND is_required = 1", (position_id,))]
        pref_skills = [s["skill_name"] for s in query_db("SELECT skill_name FROM position_skills WHERE position_id = ? AND is_required = 0", (position_id,))]

        candidates_rows = query_db("SELECT * FROM candidates WHERE target_company_id = ?", (company_id,))
        results = []

        for cand in candidates_rows:
            cand_id = cand["id"]
            cand_skills_rows = query_db("SELECT * FROM candidate_skills WHERE candidate_id = ?", (cand_id,))
            cand_skills = [dict(s) for s in cand_skills_rows]

            math_res = calculate_match_score(cand_skills, req_skills, pref_skills)

            # Check if shortlisted by this company
            shortlist_row = query_db("SELECT * FROM shortlists WHERE company_id = ? AND candidate_id = ?", (company_id, cand_id), one=True)
            feedback = shortlist_row["feedback"] if shortlist_row else None
            is_shortlisted = bool(shortlist_row and shortlist_row["status"] == "Shortlisted")

            results.append({
                **dict(cand),
                "skills": cand_skills,
                "match_score": math_res["score"],
                "math_result": math_res,
                "is_shortlisted": is_shortlisted,
                "feedback": feedback
            })

        results.sort(key=lambda x: x["match_score"], reverse=True)
        return results

    @staticmethod
    def set_shortlist(company_id, candidate_id, is_shortlisted, feedback=None):
        status = "Shortlisted" if is_shortlisted else "Reviewed"
        existing = query_db("SELECT * FROM shortlists WHERE company_id = ? AND candidate_id = ?", (company_id, candidate_id), one=True)
        if existing:
            execute_db("UPDATE shortlists SET status = ?, feedback = COALESCE(?, feedback) WHERE company_id = ? AND candidate_id = ?",
                       (status, feedback, company_id, candidate_id))
        else:
            execute_db("INSERT INTO shortlists (company_id, candidate_id, status, feedback) VALUES (?, ?, ?, ?)",
                       (company_id, candidate_id, status, feedback or ""))
        return True

    @staticmethod
    def get_university_demand(is_refreshed=False):
        rows = query_db("SELECT * FROM industry_demand")
        demand_list = []
        for r in rows:
            d = dict(r)
            if is_refreshed:
                if d["id"] == "cloud":
                    d["demand_index"] = 90
                elif d["id"] == "docker":
                    d["demand_index"] = 80
                elif d["id"] == "genai":
                    d["demand_index"] = 76
            demand_list.append(d)
        return demand_list

    @staticmethod
    def get_curriculum_coverage(university_id="u_you"):
        rows = query_db("SELECT * FROM curriculum_coverage WHERE university_id = ?", (university_id,))
        return {r["skill_id"]: r["coverage_score"] for r in rows}

    @staticmethod
    def get_university_benchmark(current_user_org_id="u_you", alignment_score=74):
        """
        Enforce University Isolation:
        Own university row is highlighted with score explanation.
        Other universities expose rank and score ONLY.
        """
        rows = query_db("SELECT * FROM benchmarks ORDER BY rank ASC")
        result = []
        for r in rows:
            row_dict = dict(r)
            if row_dict["university_id"] == current_user_org_id:
                row_dict["score"] = alignment_score
                row_dict["is_own"] = True
                row_dict["has_detail"] = True
            else:
                row_dict["is_own"] = False
                row_dict["has_detail"] = False
            result.append(row_dict)
        return result

    @staticmethod
    def get_applications_for_student(student_id):
        rows = query_db("""
            SELECT a.*, p.role as position_role, p.company_id, c.name as company_name
            FROM applications a
            JOIN positions p ON a.position_id = p.id
            JOIN companies c ON p.company_id = c.id
            WHERE a.student_id = ?
        """, (student_id,))
        return [dict(r) for r in rows]

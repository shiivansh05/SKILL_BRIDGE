import math
import re

def calculate_match_score(candidate_skills, required_skills, preferred_skills):
    """
    Exact Match Formula from 04_DEMO_DATA_AND_ARCHITECTURE.md:
    required_part   = 70 * (required skills matched / required skills)
    preferred_part  = 20 * (preferred skills matched / preferred skills)
    evidence_part   = 10 * (verified matched skills / matched skills)
    match           = round(required_part + preferred_part + evidence_part)
    """
    # candidate_skills can be list of dicts: [{'name': 'Python', 'verified': True}] or [{'skill_name': 'Python', 'verified': True}]
    skills_map = {((s.get('name') or s.get('skill_name', ''))).lower(): s for s in candidate_skills}

    def has_skill(name):
        return name.lower() in skills_map

    def is_verified(name):
        sk = skills_map.get(name.lower())
        return bool(sk and sk.get('verified'))

    req_matched = [s for s in required_skills if has_skill(s)]
    pref_matched = [s for s in preferred_skills if has_skill(s)]
    matched_skills = req_matched + pref_matched
    verified_matched = [s for s in matched_skills if is_verified(s)]
    missing_required = [s for s in required_skills if not has_skill(s)]

    req_total = len(required_skills)
    pref_total = len(preferred_skills)
    total_matched = len(matched_skills)
    total_verified = len(verified_matched)

    req_part = 70.0 * (len(req_matched) / req_total) if req_total > 0 else 0.0
    pref_part = 20.0 * (len(pref_matched) / pref_total) if pref_total > 0 else 0.0
    ev_part = 10.0 * (total_verified / total_matched) if total_matched > 0 else 0.0

    score = int(round(req_part + pref_part + ev_part))

    verified_share = (total_verified / total_matched) if total_matched > 0 else 0.0
    if verified_share >= 0.75:
        confidence = "High"
    elif verified_share >= 0.50:
        confidence = "Medium"
    else:
        confidence = "Low"

    return {
        "score": score,
        "req_matched": len(req_matched),
        "req_total": req_total,
        "pref_matched": len(pref_matched),
        "pref_total": pref_total,
        "matched_skills": matched_skills,
        "missing_required": missing_required,
        "verified_matched": total_verified,
        "total_matched": total_matched,
        "confidence": confidence,
        "verified_share_pct": int(round(verified_share * 100))
    }

def calculate_alignment_score(demand_list, coverage_map):
    """
    Exact Alignment Formula:
    alignment = sum(demand_i * coverage_i) / sum(demand_i)
    """
    sum_demand = 0.0
    sum_weighted = 0.0
    gaps = []

    for item in demand_list:
        skill_id = item['id']
        demand_val = float(item['demand_index'])
        cov_val = float(coverage_map.get(skill_id, 0))

        sum_demand += demand_val
        sum_weighted += (demand_val * cov_val)

        gap = demand_val - cov_val
        if gap < 10:
            status = "Aligned"
            status_type = "aligned"
        elif gap < 25:
            status = "Moderate Gap"
            status_type = "partial"
        else:
            status = "Critical Gap"
            status_type = "critical"

        # Actionable recommendations tied to specific gaps
        rec = "Coverage fulfills current industry threshold."
        if skill_id == "docker":
            rec = "Add a practical containerisation module in the second-year software engineering course."
        elif skill_id == "cloud":
            rec = "Add hands-on cloud deployment labs (compute, storage, basic deployment) to systems course."
        elif skill_id == "genai":
            rec = "Introduce an elective on prompt-based application development and evaluation."

        gaps.append({
            "skill_id": skill_id,
            "skill_name": item['name'],
            "category": item['category'],
            "demand": int(demand_val),
            "coverage": int(cov_val),
            "gap": int(gap),
            "status": status,
            "status_type": status_type,
            "recommendation": rec
        })

    alignment = int(round(sum_weighted / sum_demand)) if sum_demand > 0 else 0
    return {
        "alignment_score": alignment,
        "sum_demand": int(sum_demand),
        "sum_weighted": int(sum_weighted),
        "gaps": gaps
    }

def extract_skills_from_text(text, skill_catalog):
    """
    NLP skill normalization from resume or description text.
    """
    text_lower = text.lower()
    matched = []
    for skill in skill_catalog:
        name = skill['name']
        aliases = skill.get('aliases', [name.lower()])
        for alias in aliases:
            pattern = r'\b' + re.escape(alias.lower()) + r'\b'
            if re.search(pattern, text_lower):
                matched.append(name)
                break
    return list(dict.fromkeys(matched))

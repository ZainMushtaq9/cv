def normalize_score(llm_result):
    """Normalize the match_score and enforce decision thresholds."""
    if not llm_result:
        return None

    # Normalize match_score
    score = llm_result.get("match_score", 0)
    try:
        score = float(score)
        if score > 100:
            score = 100
        if score < 0:
            score = 0
    except (ValueError, TypeError):
        score = 0

    # Determine decision based on match_score
    if score >= 90:
        decision = "Strong Candidate"
    elif score >= 70:
        decision = "Moderate Fit"
    elif score >= 50:
        decision = "Weak Match"
    else:
        decision = "Reject"

    llm_result["match_score"] = round(score, 1)
    llm_result["decision"] = decision

    # Ensure arrays exist and are properly formatted
    llm_result.setdefault("matched_keywords", [])
    llm_result.setdefault("missing_keywords", [])
    llm_result.setdefault("extra_keywords", [])
    llm_result.setdefault("strengths", [])
    llm_result.setdefault("weaknesses", [])
    llm_result.setdefault("cv_improvement_suggestions", [])
    llm_result.setdefault("missing_keyword_suggestions", [])
    llm_result.setdefault("extra_keyword_advice", [])
    llm_result.setdefault("total_jd_keywords", 0)
    llm_result.setdefault("total_resume_keywords", 0)

    return llm_result

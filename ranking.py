def rank_candidates(candidates_results):
    """Rank candidates by their union-based match_score."""
    if not candidates_results:
        return []
    valid = [c for c in candidates_results if c is not None and "match_score" in c]
    sorted_candidates = sorted(
        valid, key=lambda x: float(x.get("match_score", 0)), reverse=True
    )
    for idx, candidate in enumerate(sorted_candidates):
        candidate["rank"] = idx + 1
    return sorted_candidates

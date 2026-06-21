def calculate_score(role, recommended_roles):

    score = 50

    role_lower = role.lower()

    for rec_role in recommended_roles:

        if any(
            word in role_lower
            for word in rec_role.lower().split()
        ):
            score += 10

    return min(score, 100)

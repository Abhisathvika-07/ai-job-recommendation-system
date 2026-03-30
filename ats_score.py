def calculate_ats_score(resume_text, job_skills):
    resume_text = resume_text.lower()

    skills = [s.strip().lower() for s in job_skills.split()]

    matched = 0

    for skill in skills:
        if skill in resume_text:
            matched += 1

    if len(skills) == 0:
        return 0

    skill_score = (matched / len(skills)) * 100

    # Bonus checks
    bonus = 0

    if "project" in resume_text:
        bonus += 5
    if "experience" in resume_text:
        bonus += 5
    if "education" in resume_text:
        bonus += 5

    final_score = min(skill_score + bonus, 100)

    return round(final_score, 2)
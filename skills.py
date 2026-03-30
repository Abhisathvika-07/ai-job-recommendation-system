def get_skill_gap(resume, job):
    resume_words = set(resume.split())
    job_words = set(job.split())

    missing = job_words - resume_words
    return list(missing)
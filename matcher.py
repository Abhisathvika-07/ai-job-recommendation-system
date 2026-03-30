from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_jobs(resume_text, jobs):
    job_texts = [job["Skills"] for job in jobs]

    job_embeddings = model.encode(job_texts, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    scores = util.cos_sim(resume_embedding, job_embeddings)[0]

    for i, job in enumerate(jobs):
        job["score"] = float(scores[i])

    jobs = sorted(jobs, key=lambda x: x["score"], reverse=True)
    return jobs
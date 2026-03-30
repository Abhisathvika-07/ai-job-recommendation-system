import pandas as pd
import random

job_titles = [
    "Data Scientist", "Backend Developer", "Frontend Developer",
    "Full Stack Developer", "ML Engineer", "Data Analyst","Data Architect"
    "DevOps Engineer", "Cloud Engineer", "AI Engineer",
    "Cyber Security Analyst", "Software Engineer", "Data Engineer","Cyber Security Analyst",
"Security Engineer","Ethical Hacker","SOC Analyst","Penetration Tester"
]

locations = ["Hyderabad", "Bangalore", "Pune", "Chennai", "Mumbai", "Remote"]

domains = {
    "Data Scientist": "Data",
    "Data Engineer": "Data",
    "ML Engineer": "AI",
    "AI Engineer": "AI",
    "Data Analyst": "Analytics",
    "Backend Developer": "Software",
    "Frontend Developer": "Software",
    "Full Stack Developer": "Software",
    "Software Engineer": "Software",
    "DevOps Engineer": "Cloud",
    "Cloud Engineer": "Cloud",
    "Cyber Security Analyst": "Cybersecurity"
}

skills_map = {
    "Data Scientist": "python machine learning pandas numpy statistics",
    "Data Engineer": "python spark sql kafka",
    "ML Engineer": "python tensorflow pytorch deep learning",
    "AI Engineer": "python nlp transformers deep learning",
    "Data Analyst": "sql excel powerbi visualization",
    "Backend Developer": "python django fastapi api",
    "Frontend Developer": "react javascript html css",
    "Full Stack Developer": "javascript node react mongodb",
    "Software Engineer": "java c++ data structures algorithms",
    "DevOps Engineer": "docker kubernetes aws linux",
    "Cloud Engineer": "aws azure terraform devops",
    "Cyber Security Analyst": "network security penetration testing"
}

data = []

# 🔥 KEY CHANGE: balanced generation
for location in locations:
    for job in job_titles:
        for _ in range(10):  # ensures distribution
            data.append({
                "Job Title": job,
                "Skills": skills_map[job],
                "Location": location,
                "Salary": random.randint(300000, 2000000),
                "Domain": domains[job]
            })

df = pd.DataFrame(data)
df.to_csv("jobs.csv", index=False)

print("✅ Balanced dataset generated!")

for location in locations:
    for job in job_titles:
        for _ in range(10):
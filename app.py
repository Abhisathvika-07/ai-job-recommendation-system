import streamlit as st
import pandas as pd
from matcher import match_jobs
from resume_parser import extract_text_from_pdf
from skills import get_skill_gap
from suggestions import get_skill_suggestions
from ats_score import calculate_ats_score

st.set_page_config(page_title="AI Job Recommender", layout="wide")

# ---------------------------
# 🎨 CUSTOM UI
# ---------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e293b, #0f172a);
}
.job-card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0 0 15px rgba(0,0,0,0.3);
}
.tag {
    display: inline-block;
    background: #2563eb;
    color: white;
    padding: 5px 10px;
    border-radius: 10px;
    margin: 5px;
    font-size: 12px;
}
.ats-box {
    background: #1d4ed8;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.suggestion {
    background: #0ea5e9;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# TITLE
# ---------------------------
st.title("🚀 AI Job Recommendation System")

# ---------------------------
# FILTERS
# ---------------------------
st.sidebar.header("🔍 Filters")

location = st.sidebar.selectbox(
    "Location",
    ["All", "Hyderabad", "Bangalore", "Pune", "Chennai", "Mumbai", "Remote"]
)

domain = st.sidebar.selectbox(
    "Domain",
    ["All", "AI", "Software", "Data", "Cloud", "Analytics", "Cybersecurity"]
)


salary = st.sidebar.number_input("Minimum Salary (₹)", min_value=0, value=500000)


uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])


if uploaded_file is None:
    st.info("📄 Please upload your resume to continue.")
    st.stop()

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv("jobs.csv")
df.columns = df.columns.str.strip()

if location != "All":
    df = df[df["Location"] == location]

if domain != "All":
    df = df[df["Domain"] == domain]

df = df[df["Salary"] >= salary]

jobs = df.to_dict(orient="records")

st.write(f"Jobs after filtering: {len(jobs)}")

# ---------------------------
# RESUME PARSE
# ---------------------------
resume_text = extract_text_from_pdf(uploaded_file)

# ---------------------------
# MATCHING
# ---------------------------
if resume_text and jobs:
    jobs = match_jobs(resume_text, jobs)

jobs = sorted(jobs, key=lambda x: x.get("score", 0), reverse=True)[:10]

if not jobs:
    st.warning("No jobs found.")
    st.stop()

# ---------------------------
# JOB SELECT
# ---------------------------
job_titles = list(set(job["Job Title"] for job in jobs))

selected_job_title = st.selectbox(
    "🎯 Select a job to analyze skill gap",
    job_titles
)

selected_job = next(
    (job for job in jobs if job["Job Title"] == selected_job_title),
    None
)

# ---------------------------
# ATS + SKILL GAP
# ---------------------------
if selected_job:

    ats_score = calculate_ats_score(resume_text, selected_job["Skills"])

    ats_html = f"""
    <div class="ats-box">
        <h3>📊 ATS Resume Score: {ats_score}%</h3>
    </div>
    """
    st.markdown(ats_html, unsafe_allow_html=True)

    st.progress(int(ats_score))

    if ats_score > 75:
        st.success("🔥 Excellent Resume!")
    elif ats_score > 50:
        st.info("👍 Good, but improve more.")
    else:
        st.warning("⚠️ Needs improvement.")

    # Skill Gap
    missing_skills = get_skill_gap(resume_text, selected_job["Skills"])

    if missing_skills:
        st.subheader("🧠 Skill Gap Analysis")

        for skill in missing_skills[:10]:
            st.markdown(f'<span class="tag">{skill}</span>', unsafe_allow_html=True)

        # Suggestions
        suggestions = get_skill_suggestions(missing_skills)

        st.subheader("📈 Skill Improvement Suggestions")

        for s in suggestions[:5]:
            st.markdown(f'<div class="suggestion">{s}</div>', unsafe_allow_html=True)

    else:
        st.success("✅ You match all skills!")

# ---------------------------
# RESET RENDERING (IMPORTANT)
# ---------------------------
st.write("")

# ---------------------------
# JOB DISPLAY
# ---------------------------
st.subheader("🎯 Top Job Recommendations")

for job in jobs:
    with st.container():

        # Clean skills
        skills_list = job["Skills"].replace(",", " ").split()

        # Title
        st.markdown(f"### 💼 {job['Job Title']}")

        # Info
        st.write(f"📍 Location: {job['Location']}")
        st.write(f"💰 Salary: ₹{job['Salary']}")
        st.write(f"🌐 Domain: {job['Domain']}")

        # Skills as colored tags
        st.write("**Skills:**")
        cols = st.columns(6)

        for i, skill in enumerate(skills_list[:12]):
            cols[i % 6].markdown(
                f"<div style='background:#2563eb;padding:6px;border-radius:8px;text-align:center;margin:2px'>{skill}</div>",
                unsafe_allow_html=True
            )

        # Match score
        score = job.get("score", 0)
        st.progress(int(score * 100))

        if score > 0.7:
            st.success("🔥 Strong Match!")

        st.markdown("---")
import streamlit as st
import pdfplumber
from fuzzywuzzy import fuzz

# --- Extract text from uploaded resume PDF ---
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# --- Extract keywords from text ---
def extract_keywords(text):
    words = text.lower().split()
    return list(set([word.strip(",.():;") for word in words if len(word) > 2]))

# --- Compare resume and JD keywords ---
def compare_skills(resume_skills, jd_skills):
    matched, missing = [], []
    for skill in jd_skills:
        score = max([fuzz.partial_ratio(skill, r) for r in resume_skills] + [0])
        if score >= 80:
            matched.append(skill)
        else:
            missing.append(skill)
    return matched, missing

# --- Streamlit App UI ---
st.set_page_config(page_title="Resume Skill Gap Analyzer", layout="centered")

st.markdown("<h1 style='text-align: center; font-size: 40px; color: #004d99;'>📊 Resume & Skill Gap Analyzer</h1>", unsafe_allow_html=True)
st.markdown("#### Paste your Resume Text below 👇 (or upload as PDF)")

# --- Resume Text Box (always shown) ---
resume_text_input = st.text_area("✍️ Resume Text", height=200)

# --- Optional PDF Upload ---
resume_file = st.file_uploader("📄 Upload Resume PDF (optional)", type=["pdf"])

# --- JD Text Box (always shown) ---
st.markdown("#### Paste the Job Description (JD) 👇")
jd_text_input = st.text_area("💼 Job Description", height=200)

# --- Logic to prioritize PDF if uploaded ---
resume_text = ""
if resume_file is not None:
    resume_text = extract_text_from_pdf(resume_file)
elif resume_text_input.strip():
    resume_text = resume_text_input

jd_text = jd_text_input.strip()

# --- Analyze Button ---
if st.button("🔍 Analyze Skill Match"):
    if not resume_text or not jd_text:
        st.warning("⚠️ Please provide both Resume and Job Description.")
    else:
        resume_keywords = extract_keywords(resume_text)
        jd_keywords = extract_keywords(jd_text)

        matched, missing = compare_skills(resume_keywords, jd_keywords)

        match_percent = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0

        st.success(f"✅ Matched Skills: {len(matched)}")
        st.info(f"❌ Missing Skills: {len(missing)}")

        st.markdown(f"### 📈 Skill Match Percentage: `{match_percent:.2f}%`")

        st.markdown("### ✔️ Matched Skills")
        st.write(", ".join(matched) if matched else "No matching skills found.")

        st.markdown("### ❗ Missing Skills")
        st.write(", ".join(missing) if missing else "None! Your resume matches all JD skills 🎉")

        st.markdown("---")
        st.caption("📌 Pro Tip: Add the missing skills to your resume or upskill through free courses!")

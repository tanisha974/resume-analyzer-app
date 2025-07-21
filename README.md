# 🧠 Resume Screening and Skill Gap Analyzer

A **Streamlit web application** that automatically compares a candidate's **resume** with a **job description** (JD) and highlights:
- ✔️ Matching skills
- ❌ Missing skills
- 📊 Overall match percentage

---

## 💡 Features

- Upload resume (PDF or plain text)
- Paste or upload job description
- Automatically extract text using NLP
- Detect skill gaps using fuzzy string matching
- Show results in a clean, interactive UI

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web app development |
| **PDFPlumber** | Extract text from PDF resumes |
| **FuzzyWuzzy** | Match skills between resume & JD |
| **Python-Levenshtein** | Speed up fuzzy matching |

---

## 🚀 How to Run the App Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/resume-analyzer-app.git
cd resume-analyzer-app

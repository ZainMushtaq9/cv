# Resume Keyword Optimizer

AI-powered Resume Keyword Optimizer that compares your resume against any job description using Groq LLaMA-3 models. Built with Python Flask, Tailwind CSS, and Chart.js.

## Features

- **Keyword Match Report** — Matched ✅, Missing ❌, Extra ➕ keywords
- **Match Score** — Percentage of JD keywords found in resume
- **Resume Highlighting** — See your resume text with keywords color-coded
- **Contextual Suggestions** — How to naturally add each missing keyword
- **ATS Readability Tips** — Formatting advice for ATS compatibility
- **Multi-Job Comparison** — Compare resume against multiple JDs at once
- **Industry Benchmarks** — 12 industries with tailored keyword lists
- **Export** — Download PDF or Word report, email results
- **HR Bulk Mode** — Evaluate up to 50 resumes against one JD

## How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5001`

## Environment Variables

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Tech Stack

- **Backend:** Python Flask, Groq API (LLaMA 3.3 70B)
- **Frontend:** Tailwind CSS, Chart.js, Font Awesome
- **Export:** ReportLab (PDF), python-docx (Word)

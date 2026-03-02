# cv
AI-powered Resume Analysis and Bulk ATS Evaluation Platform. Built with Python Flask, Groq LLaMA models, Tailwind CSS, and Chart.js.

## Features
- Individual Resume vs Job Description Semantic Analysis
- HR Bulk Analyzer (Rank up to 50 resumes)
- 0-100 ATS Scoring System
- Fully AdSense compliant with Legal pages
- Supports PDF, DOCX, TXT, and Images (OCR)

## How to run locally
1. Create a `.env` file and add your GROQ_API_KEY.
2. Run `python -m venv venv`
3. Activate the virtual environment (`.\venv\Scripts\activate` on Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `python app.py`
6. Open `http://localhost:5001`

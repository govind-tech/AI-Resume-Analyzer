# AI Resume Analyzer & Job Matcher

A Python-based web application that analyzes a resume in PDF format and compares its technical skills with a job description.

## Features

- Upload a resume in PDF format.
- Extract text from the uploaded resume.
- Identify technical skills using keyword matching.
- Compare resume skills with job requirements.
- Display matching and missing skills.
- Calculate a skill match percentage.
- Recommend skills to practice.
- Download a text-based match report.

## Technologies Used

- Python
- Streamlit
- PyMuPDF

## How It Works

1. The user uploads a PDF resume.
2. The application extracts text from the PDF.
3. The program searches for predefined technical skills.
4. It identifies skills mentioned in the job description.
5. It compares the two skill lists.
6. It calculates the percentage of required skills found in the resume.
7. It displays the results and generates a downloadable report.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/govind-tech/AI-Resume-Analyzer
cd AI-Resume-Analyzer
```

Replace `https://github.com/govind-tech/AI-Resume-Analyzer` with your actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## Matching Algorithm

The current version uses rule-based keyword matching rather than a trained AI model.

The match percentage is calculated as:

Match Percentage = (Matching Required Skills / Total Detected Required Skills) × 100

This score measures skill overlap only. It does not predict hiring outcomes.

## Limitations

- Skill detection depends on a predefined list of keywords.
- Synonyms and related skills may not be recognized.
- Scanned PDFs without extractable text are not processed using OCR.
- Recommendations are rule-based.

## Future Improvements

- Expand skill coverage and handle skill-name variations.
- Add more useful skill-learning recommendations.
- Improve report design and export options.
- Explore semantic matching using NLP or embedding models.

## Author

**Govind Prajapat**

- GitHub: https://github.com/govind-tech
- LinkedIn: https://www.linkedin.com/in/govind-prajapat-4a35a836a

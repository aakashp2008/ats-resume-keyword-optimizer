# 🤖 ATS Resume Keyword Optimizer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/NLP-Text%20Processing-green">
  <img src="https://img.shields.io/badge/ATS-Keyword%20Analysis-orange">
  <img src="https://img.shields.io/badge/Testing-Pytest-yellow">
  <img src="https://img.shields.io/badge/Status-Completed-success">
</p>

<p align="center">
  <b>A Python-based ATS-style resume analyzer that compares a resume with a job description, identifies matched and missing keywords, calculates a keyword alignment score, and generates an improvement report.</b>
</p>

---

## 📌 Overview

The **ATS Resume Keyword Optimizer** is a Python-based text analysis tool designed to help students and job seekers understand how well their resume matches a specific job description.

The application extracts meaningful keywords from both documents and compares them to identify:

* ✅ Matching keywords
* ❌ Missing keywords
* 📊 Keyword match percentage
* 📄 Resume statistics
* 💡 Resume improvement recommendations
* 📝 Automatically generated analysis report

> **Note:** This project provides heuristic ATS-style keyword analysis. It does not reproduce the proprietary scoring algorithm of any specific Applicant Tracking System.

---

## 🎥 Project Demo

![Project Demo](https://raw.githubusercontent.com/aakashp2008/ats-resume-keyword-optimizer/main/assets/demo.gif)

---

## ✨ Features

### 📄 Resume Analysis

* Reads resume text files.
* Normalizes resume content.
* Extracts meaningful keywords.
* Identifies technical skills.

### 💼 Job Description Analysis

* Reads job descriptions from text files.
* Extracts relevant keywords.
* Detects technical requirements.

### 🔍 Keyword Matching

* Compares resume keywords with job requirements.
* Identifies matched keywords.
* Identifies missing keywords.

### 📊 ATS Match Score

Calculates a keyword alignment score based on:

```text
Matched Keywords
----------------------------- × 100
Total Job Keywords
```

### 💡 Recommendations

The system provides suggestions based on the calculated score and missing keywords.

### 📝 Report Generation

Automatically generates:

```text
ats_report.txt
```

containing the complete analysis.

### 🧪 Unit Testing

The project includes automated tests for:

* Perfect keyword matching
* Partial matching
* No matching keywords
* Empty job descriptions

---

## 🛠️ Technologies Used

| Technology          | Purpose                    |
| ------------------- | -------------------------- |
| Python              | Core programming language  |
| Regular Expressions | Text normalization         |
| Collections         | Keyword frequency analysis |
| File Handling       | Resume/JD processing       |
| Pytest              | Unit testing               |
| Git                 | Version control            |
| GitHub              | Project hosting            |

---

## 📂 Project Structure

```text
ats-resume-keyword-optimizer/
│
├── app.py
│
├── resume_parser.py
├── keyword_analyzer.py
├── matcher.py
├── report_generator.py
│
├── sample_data/
│   ├── resume.txt
│   └── job_description.txt
│
├── assets/
│   └── demo.gif
│
├── tests/
│   └── test_matcher.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3.x is installed.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

No external Python packages are required to run the main application.

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/aakashp2008/ats-resume-keyword-optimizer.git
```

Navigate into the project:

```bash
cd ats-resume-keyword-optimizer
```

---

## ▶️ Run the Application

Start the application:

```bash
python app.py
```

You will see:

```text
=================================================================
              ATS RESUME KEYWORD OPTIMIZER
=================================================================
Analyze your resume against a job description
and identify missing ATS-relevant keywords.
=================================================================

MAIN MENU
-----------------------------------------------------------------
1. Analyze sample resume
2. Analyze custom files
3. View sample data
4. Exit
-----------------------------------------------------------------
Enter your choice:
```

---

## 🔐 Login

This project does **not require login or authentication**.

It is designed as a lightweight local resume-analysis application.

---

## 🏠 Main Menu

The application provides four options:

### 1️⃣ Analyze Sample Resume

Uses:

```text
sample_data/resume.txt
```

and:

```text
sample_data/job_description.txt
```

to perform an analysis.

### 2️⃣ Analyze Custom Files

Allows the user to provide their own resume and job-description text files.

Example:

```text
Enter resume text file path:
resume.txt

Enter job description text file path:
job_description.txt
```

### 3️⃣ View Sample Data

Displays the sample resume and job description.

### 4️⃣ Exit

Closes the application.

---

## 📊 Example Input

### Resume

```text
Python
Java
SQL
Git
GitHub
Data Structures
Machine Learning
```

### Job Description

```text
Python
Java
SQL
Git
REST API
Docker
Machine Learning
```

---

## 📈 Example Output

```text
======================================================================
                 ATS RESUME ANALYSIS REPORT
======================================================================

MATCH SCORE
----------------------------------------------------------------------
ATS Keyword Match Score: 71.43%
Alignment Level: GOOD

KEYWORD SUMMARY
----------------------------------------------------------------------
Job Keywords: 7
Matched Keywords: 5
Missing Keywords: 2

MATCHED KEYWORDS
----------------------------------------------------------------------
✓ git
✓ java
✓ machine
✓ python
✓ sql

MISSING KEYWORDS
----------------------------------------------------------------------
• docker
• rest

RECOMMENDATIONS
----------------------------------------------------------------------
1. Your resume has good keyword alignment, but some relevant
   skills are missing.

2. Add missing keywords only when you genuinely have the
   corresponding skill or experience.

3. Use specific technical terms instead of vague descriptions.

4. Mention technologies in relevant project or work-experience
   descriptions.
```

---

## 🔎 Analysis

The application performs the following workflow:

```text
Resume
   │
   ▼
Text Normalization
   │
   ▼
Keyword Extraction
   │
   ▼
Job Description
   │
   ▼
Keyword Extraction
   │
   ▼
Keyword Matching
   │
   ▼
Match Score
   │
   ├── Matched Keywords
   │
   ├── Missing Keywords
   │
   └── Recommendations
   │
   ▼
ATS Analysis Report
```

---

## 🧠 Keyword Matching Logic

The system calculates the keyword alignment using:

```text
Match Score =
(Matched Job Keywords / Total Job Keywords) × 100
```

For example:

```text
Total Job Keywords = 10
Matched Keywords = 7

Score = (7 / 10) × 100

Score = 70%
```

---

## 📊 Score Interpretation

|     Score | Alignment |
| --------: | --------- |
|   80–100% | Excellent |
|    60–79% | Good      |
|    40–59% | Moderate  |
| Below 40% | Low       |

These categories are project-defined indicators and are **not official ATS thresholds**.

---

## 💡 Recommendations

The system can recommend:

* Adding relevant missing technical skills
* Using specific technical terminology
* Mentioning technologies inside project descriptions
* Improving alignment with job requirements
* Prioritizing important technical skills

### ⚠️ Important

Never add a keyword to a resume simply to increase the score.

Only include skills that genuinely represent your knowledge or experience.

---

## 🧪 Testing

The project includes unit tests using Pytest.

Install Pytest if needed:

```bash
pip install pytest
```

Run:

```bash
pytest
```

Expected result:

```text
4 passed
```

---

## 🔬 Test Cases

### Test 1 — Perfect Match

```text
Resume:
Python, Java, SQL, Git

Job:
Python, Java, SQL, Git

Expected:
100%
```

### Test 2 — Partial Match

```text
Resume:
Python, Java

Job:
Python, Java, SQL, Git

Expected:
50%
```

### Test 3 — No Match

```text
Resume:
HTML, CSS

Job:
Python, Java

Expected:
0%
```

### Test 4 — Empty Job Description

```text
Resume:
Python, Java

Job:
Empty

Expected:
0%
```

---

## 📄 Generated Report

After analysis, the application creates:

```text
ats_report.txt
```

The report contains:

* Match score
* Alignment level
* Matched keywords
* Missing keywords
* Document statistics
* Recommendations
* Analysis notes

---

## 🧩 Concepts Demonstrated

This project demonstrates practical knowledge of:

* Python programming
* Functions
* Sets
* Dictionaries
* File handling
* Regular expressions
* Text normalization
* String processing
* Keyword extraction
* Set operations
* Data analysis
* Automated testing
* Modular programming
* Report generation
* Error handling

---

## 🎯 Project Objectives

The main objectives are:

1. Analyze resume content programmatically.
2. Extract relevant job-description keywords.
3. Compare resume and job requirements.
4. Identify missing keywords.
5. Calculate a measurable alignment score.
6. Generate useful recommendations.
7. Produce an automated analysis report.
8. Practice software modularization and testing.

---

## 🎓 Learning Outcomes

After completing this project, you can understand how to:

* Process unstructured text using Python.
* Build a basic NLP-style keyword analyzer.
* Compare two text documents.
* Use sets for efficient matching.
* Build modular Python applications.
* Create automated tests.
* Generate structured reports.
* Design a practical developer-focused tool.

---

## 🔒 Security & Privacy

This project runs locally and does not require uploading resumes to an external server.

For public GitHub repositories:

> ⚠️ Do not upload your real resume if it contains private information such as your phone number, personal email, home address, or other sensitive details.

Use a sample or sanitized resume instead.

---

## ⚠️ Limitations

This project currently uses rule-based keyword analysis.

It does not:

* Reproduce proprietary ATS algorithms
* Understand every semantic relationship between skills
* Evaluate resume formatting
* Parse PDF/DOCX files directly
* Understand candidate experience depth
* Determine whether a candidate actually possesses a skill
* Guarantee ATS screening success

The match score should therefore be treated as a **guideline**, not a hiring prediction.

---

## 🚀 Future Enhancements

Possible improvements include:

### 📄 PDF Resume Support

Add PDF parsing using libraries such as:

```text
PyMuPDF
pdfplumber
```

### 📝 DOCX Support

Add Microsoft Word resume parsing.

### 🤖 NLP-Based Similarity

Use:

```text
TF-IDF
Cosine Similarity
Sentence Transformers
```

to measure semantic similarity.

### 🌐 Web Interface

Build a frontend using:

```text
HTML
CSS
JavaScript
```

or:

```text
Streamlit
```

### ⚡ FastAPI Backend

Convert the application into a REST API.

Possible endpoints:

```text
POST /analyze
GET /health
GET /report
```

### 📊 Dashboard

Display:

* Match score
* Skill coverage
* Missing skills
* Keyword frequency
* Recommendations

### ☁️ Deployment

Deploy the application using a cloud platform.

### 🔐 Authentication

Add user accounts and secure resume storage.

---

## 💼 Why This Project?

This project is more than a basic Python CRUD application.

It demonstrates a combination of:

```text
Python
   +
Text Processing
   +
NLP Concepts
   +
Data Analysis
   +
Software Testing
   +
Real-World Problem Solving
```

It is especially useful for demonstrating practical development skills during:

* Software Engineering internships
* Python internships
* Data/AI internships
* Placement preparation
* Resume projects
* Technical interviews

---

## 📌 Resume Project Description

You can describe the project on your resume as:

> **ATS Resume Keyword Optimizer** — Developed a Python-based ATS-style resume analysis tool that extracts and compares resume and job-description keywords, calculates keyword alignment scores, identifies missing skills, and generates automated improvement reports with unit-tested matching logic.

---

## 🧑‍💻 Author

**AAKASH P**

B.Tech Information Technology Student
Panimalar Engineering College

### Skills

```text
Python | Java | C | SQL | DSA | AI/ML | Git | GitHub
```

---

## 🔗 GitHub

**GitHub Profile**

https://github.com/aakashp2008

**Project Repository**

https://github.com/aakashp2008/ats-resume-keyword-optimizer

---

## ⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the repository
🐛 Report issues
💡 Suggest improvements

---

## 📜 License

This project is intended for educational and portfolio purposes.

You may modify and extend the project for learning and development.

---

<p align="center">
  Made with ❤️ using Python
</p>

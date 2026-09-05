# 🤖 ATS Resume Keyword Optimizer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/NLP-Text%20Processing-green" alt="NLP">
  <img src="https://img.shields.io/badge/ATS-Keyword%20Analysis-orange" alt="ATS">
  <img src="https://img.shields.io/badge/Testing-Pytest-yellow" alt="Pytest">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status">
</p>

<p align="center">
  <b>A Python-based ATS-style resume analyzer that compares a resume with a job description, identifies matched and missing keywords, calculates a keyword alignment score, and generates an improvement report.</b>
</p>

---

## 📌 Overview

**ATS Resume Keyword Optimizer** is a Python-based text analysis tool designed to help students and job seekers understand how well their resume matches a specific job description.

The application analyzes both documents and identifies:

* ✅ Matching keywords
* ❌ Missing keywords
* 📊 Keyword match percentage
* 📄 Resume statistics
* 💡 Improvement recommendations
* 📝 Automatically generated analysis report

> **Note:** This project provides heuristic ATS-style keyword analysis. It does not reproduce the proprietary scoring algorithm of any specific Applicant Tracking System.

---

## 🎥 Project Demo

![Project Demo](https://raw.githubusercontent.com/aakashp2008/ats-resume-keyword-optimizer/main/assets/demo.gif)

> **Important:** The GIF must actually exist at `assets/demo.gif` in the GitHub repository for the demo to appear.

---

## ✨ Features

### 📄 Resume Analysis

* Reads resume text files
* Normalizes resume content
* Extracts meaningful keywords
* Identifies technical skills
* Calculates basic document statistics

### 💼 Job Description Analysis

* Reads job descriptions from text files
* Extracts relevant keywords
* Detects technical requirements
* Compares job requirements with resume content

### 🔍 Keyword Matching

* Compares resume keywords with job requirements
* Identifies matched keywords
* Identifies missing keywords
* Calculates keyword coverage

### 📊 ATS Match Score

The application calculates a keyword alignment score based on:

```text
Match Score =
(Matched Job Keywords / Total Job Keywords) × 100
```

### 💡 Recommendations

The application provides suggestions based on:

* Overall keyword score
* Missing keywords
* Resume-job alignment

### 📝 Report Generation

Automatically generates:

```text
ats_report.txt
```

The report contains the complete analysis.

### 🧪 Unit Testing

The project includes automated tests for:

* Perfect keyword matching
* Partial keyword matching
* No keyword matching
* Empty job descriptions

---

## 🛠️ Technologies Used

| Technology          | Purpose                     |
| ------------------- | --------------------------- |
| Python              | Core programming language   |
| Regular Expressions | Text normalization          |
| Sets                | Keyword comparison          |
| Dictionaries        | Structured analysis results |
| File Handling       | Resume and JD processing    |
| Pytest              | Unit testing                |
| Git                 | Version control             |
| GitHub              | Project hosting             |

---

## 📂 Project Structure

```text
ats-resume-keyword-optimizer/
│
├── app.py
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
├── ats_report.txt
└── README.md
```

> `ats_report.txt` is generated automatically when the application runs and should normally be included in `.gitignore`.

---

## 🚀 Getting Started

### Prerequisites

Make sure **Python 3.x** is installed.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

The main application uses Python standard-library modules, so no external packages are required to run it.

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/aakashp2008/ats-resume-keyword-optimizer.git
```

Navigate to the project directory:

```bash
cd ats-resume-keyword-optimizer
```

---

## ▶️ Run the Application

Start the application:

```bash
python app.py
```

The application will start from the terminal.

Example:

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

## 🏠 Main Menu

The application provides four main options.

### 1️⃣ Analyze Sample Resume

Uses:

```text
sample_data/resume.txt
```

and:

```text
sample_data/job_description.txt
```

to perform an automatic analysis.

### 2️⃣ Analyze Custom Files

Allows users to provide their own resume and job-description text files.

Example:

```text
Enter resume text file path:
resume.txt

Enter job description text file path:
job_description.txt
```

### 3️⃣ View Sample Data

Displays the sample resume and sample job description.

### 4️⃣ Exit

Closes the application.

---

## 🔐 Login & Authentication

This project does **not require login or authentication**.

It is designed as a lightweight local resume-analysis application.

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
```

---

## 🔎 Analysis Workflow

The application follows this workflow:

```text
                ┌─────────────────┐
                │     Resume      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Processing  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │Keyword Extraction│
                └────────┬────────┘
                         │
                         │
                ┌────────▼────────┐
                │ Job Description  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │Keyword Extraction│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Keyword Matching │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Match Score    │
                └────────┬────────┘
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          Matched     Missing   Recommendations
          Keywords    Keywords
                         │
                         ▼
                ┌─────────────────┐
                │  Analysis Report │
                └─────────────────┘
```

---

## 🧠 Keyword Matching Logic

The project uses set operations to compare extracted keywords.

The basic calculation is:

```text
Match Score =
(Matched Job Keywords / Total Job Keywords) × 100
```

### Example

```text
Total Job Keywords = 10
Matched Keywords = 7
```

Therefore:

```text
Score = (7 / 10) × 100

Score = 70%
```

---

## 📊 Score Interpretation

|     Score | Alignment    |
| --------: | ------------ |
|   80–100% | 🟢 Excellent |
|    60–79% | 🔵 Good      |
|    40–59% | 🟡 Moderate  |
| Below 40% | 🔴 Low       |

> These categories are project-defined indicators and are **not official ATS thresholds**.

---

## 🔍 Matched Keywords

The application displays keywords that appear in both:

```text
Resume
+
Job Description
```

Example:

```text
✓ Python
✓ Java
✓ SQL
✓ Git
```

This helps identify areas where the resume already aligns with the job.

---

## ❌ Missing Keywords

The application also identifies keywords found in the job description but not in the resume.

Example:

```text
• Docker
• REST
• AWS
```

These can help the user identify skills or terminology that may need attention.

> Only add a missing keyword if you genuinely have the corresponding skill, knowledge, or experience.

---

## 💡 Recommendations

The system can provide recommendations such as:

* Improve keyword alignment
* Add relevant skills when truthful
* Use specific technical terminology
* Mention technologies in project descriptions
* Prioritize important technical requirements

---

## 📄 Generated Report

After analysis, the application generates:

```text
ats_report.txt
```

The report contains:

* 📊 Match score
* 📈 Alignment level
* ✅ Matched keywords
* ❌ Missing keywords
* 📄 Document information
* 💡 Recommendations
* 🕒 Report generation timestamp

---

## 🧪 Testing

The project includes unit tests using **Pytest**.

Install Pytest:

```bash
pip install pytest
```

Run the tests:

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

## 🧩 Concepts Demonstrated

This project demonstrates practical knowledge of:

* Python programming
* Modular programming
* Functions
* Sets
* Dictionaries
* File handling
* Regular expressions
* String processing
* Text normalization
* Keyword extraction
* Set intersection
* Set difference
* Data analysis
* Error handling
* Automated testing
* Report generation

---

## 🎯 Project Objectives

The main objectives are:

1. Analyze resume content programmatically.
2. Extract relevant job-description keywords.
3. Compare resume and job requirements.
4. Identify matching keywords.
5. Identify missing keywords.
6. Calculate a measurable alignment score.
7. Generate improvement recommendations.
8. Produce an automated report.
9. Practice modular software development.
10. Implement basic automated testing.

---

## 🎓 Learning Outcomes

Through this project, the developer gains experience in:

* Processing unstructured text using Python
* Building rule-based NLP-style applications
* Comparing two text documents
* Using sets for efficient keyword matching
* Working with regular expressions
* Building modular Python applications
* Writing unit tests
* Generating structured reports
* Handling file-related errors
* Solving a practical real-world problem

---

## 🔒 Security & Privacy

This project runs locally and does not require uploading resumes to an external server.

### ⚠️ Public Repository Safety

Do not upload a real resume containing:

* Personal phone number
* Personal email address
* Home address
* Government ID numbers
* Other sensitive information

Use a sample or sanitized resume for the public GitHub repository.

---

## ⚠️ Limitations

This project currently uses rule-based keyword analysis.

It does **not**:

* Reproduce proprietary ATS algorithms
* Guarantee ATS screening success
* Fully understand semantic relationships
* Evaluate resume formatting
* Parse PDF files directly
* Parse DOCX files directly
* Evaluate the depth of candidate experience
* Verify whether a candidate genuinely possesses a skill
* Predict whether a company will shortlist a candidate

Therefore, the score should be treated as a **guideline rather than a hiring prediction**.

---

## 🚀 Future Enhancements

### 📄 1. PDF Resume Support

Add PDF parsing using libraries such as:

```text
PyMuPDF
pdfplumber
```

### 📝 2. DOCX Resume Support

Add Microsoft Word resume parsing.

### 🤖 3. Advanced NLP

Implement:

```text
TF-IDF
Cosine Similarity
Sentence Transformers
Named Entity Recognition
```

to improve semantic matching.

### 🌐 4. Web Interface

Build a browser-based interface using:

```text
HTML
CSS
JavaScript
```

or:

```text
Streamlit
```

### ⚡ 5. FastAPI Backend

Convert the application into a REST API.

Possible endpoints:

```text
POST /analyze
GET /health
GET /report
```

### 📊 6. Interactive Dashboard

Display:

* ATS score
* Skill coverage
* Matched skills
* Missing skills
* Keyword frequency
* Recommendations
* Comparison charts

### ☁️ 7. Cloud Deployment

Deploy the application to a cloud platform.

### 🔐 8. Authentication

Add secure user accounts and resume management.

### 🗄️ 9. Database Integration

Store:

* Resumes
* Job descriptions
* Analysis history
* Scores
* Recommendations

using SQLite, PostgreSQL, or another database.

---

## 💼 Why This Project?

This project goes beyond a basic beginner-level CRUD application.

It combines:

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

It can demonstrate practical development skills for:

* 💻 Software Engineering internships
* 🐍 Python internships
* 🤖 AI/ML internships
* 📊 Data-related internships
* 🎓 College projects
* 💼 Placement preparation
* 🧑‍💻 Technical interviews

---

## 📌 Resume Project Description

You can add this project to your resume as:

> **ATS Resume Keyword Optimizer** — Developed a Python-based ATS-style resume analysis tool that extracts and compares resume and job-description keywords, calculates keyword alignment scores, identifies missing skills, and generates automated improvement reports with unit-tested matching logic.

---

## 🏆 Key Highlights

```text
✓ Modular Python Architecture
✓ Rule-Based NLP
✓ Keyword Extraction
✓ Set-Based Matching
✓ ATS-Style Scoring
✓ Automated Recommendations
✓ Report Generation
✓ Unit Testing
✓ Local File Processing
✓ Real-World Career Application
```

---

## 🧑‍💻 Author

### AAKASH P

**B.Tech Information Technology Student**
**Panimalar Engineering College**

### Technical Skills

```text
Python | Java | C | SQL | DSA | AI/ML | Git | GitHub
```

---

## 🔗 GitHub

### GitHub Profile

https://github.com/aakashp2008

### Project Repository

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

This project is intended for educational, learning, and portfolio purposes.

You are free to modify and extend the project for learning and development.

---

<p align="center">
  <b>Made with ❤️ using Python</b>
</p>

<p align="center">
  <i>Building practical projects, one step at a time.</i>
</p>

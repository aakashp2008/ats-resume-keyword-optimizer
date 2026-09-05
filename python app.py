# ============================================================
# MODULE 1: resume_parser.py
# ============================================================

import os
import re


def load_text_file(file_path):
    """
    Load text from a UTF-8 text file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()


def normalize_text(text):
    """
    Normalize text for keyword processing.
    """
    text = text.lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9+#.\-/ ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_words(text):
    """
    Extract individual words/tokens from text.
    """
    normalized = normalize_text(text)
    return normalized.split()


def get_text_statistics(text):
    """
    Return basic document statistics.
    """
    words = extract_words(text)
    sentences = re.split(r"[.!?]+", text)
    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len(sentences)
    }


# ============================================================
# MODULE 2: keyword_analyzer.py
# ============================================================

import re
from collections import Counter


STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "have", "in", "into", "is", "it", "of", "on", "or", "that",
    "the", "their", "this", "to", "using", "with", "will", "you", "your",
    "we", "our", "they", "them", "was", "were", "been", "can", "should",
    "must", "such", "than", "also", "about", "through", "which", "who",
    "within", "more", "other", "work", "working"
}


TECHNICAL_KEYWORDS = {
    "python", "java", "c", "c++", "javascript", "typescript", "html",
    "css", "react", "angular", "node", "node.js", "fastapi", "flask",
    "django", "spring", "sql", "mysql", "postgresql", "mongodb", "sqlite",
    "firebase", "git", "github", "docker", "kubernetes", "linux", "aws",
    "azure", "gcp", "api", "rest", "restful", "json", "xml", "pandas",
    "numpy", "scikit-learn", "tensorflow", "pytorch", "machine", "learning",
    "deep", "nlp", "artificial", "intelligence", "ai", "data", "analytics",
    "statistics", "tableau", "powerbi", "excel", "data structures",
    "algorithms", "dsa", "oop", "oops", "object-oriented", "testing",
    "pytest", "unit testing", "automation", "selenium", "agile", "scrum",
    "jira", "debugging", "problem-solving", "communication", "leadership",
    "teamwork"
}


def clean_token(token):
    token = token.lower().strip()
    token = re.sub(r"^[^a-z0-9+#.]+|[^a-z0-9+#.]+$", "", token)
    return token


def extract_keywords(text):
    normalized = normalize_text(text)
    words = normalized.split()
    keywords = []

    for word in words:
        word = clean_token(word)
        if not word or word in STOP_WORDS or len(word) <= 2:
            continue
        keywords.append(word)

    for keyword in TECHNICAL_KEYWORDS:
        if " " in keyword and keyword in normalized:
            keywords.append(keyword)

    return set(keywords)


# ============================================================
# MODULE 3: matcher.py
# ============================================================

def calculate_match(resume_keywords, job_keywords):
    resume_keywords = {k.lower() for k in resume_keywords}
    job_keywords = {k.lower() for k in job_keywords}

    if not job_keywords:
        return {
            "score": 0,
            "matched": set(),
            "missing": set(),
            "total_job_keywords": 0,
            "recommendations": ["The job description does not contain enough keywords."]
        }

    matched = resume_keywords.intersection(job_keywords)
    missing = job_keywords.difference(resume_keywords)

    score = round((len(matched) / len(job_keywords)) * 100, 2)
    recommendations = generate_recommendations(score, missing)

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
        "total_job_keywords": len(job_keywords),
        "matched_count": len(matched),
        "missing_count": len(missing),
        "recommendations": recommendations
    }


def generate_recommendations(score, missing):
    recommendations = []
    if score >= 80:
        recommendations.append("Your resume has strong keyword alignment with the job description.")
    elif score >= 60:
        recommendations.append("Your resume has good keyword alignment, but some relevant skills are missing.")
    elif score >= 40:
        recommendations.append("Your resume has moderate keyword alignment. Add relevant missing skills.")
    else:
        recommendations.append("Your resume has low keyword alignment. Carefully review requirements.")

    if missing:
        recommendations.append("Add missing keywords only when you genuinely have the experience.")

    recommendations.append("Use specific technical terms instead of vague descriptions.")
    return recommendations


# ============================================================
# MODULE 4: report_generator.py
# ============================================================

from datetime import datetime


def generate_report(result, resume_path, job_path):
    score = result["score"]
    matched = sorted(result["matched"])
    missing = sorted(result["missing"])
    recommendations = result["recommendations"]

    try:
        resume_stats = get_text_statistics(open(resume_path, "r", encoding="utf-8").read())
        job_stats = get_text_statistics(open(job_path, "r", encoding="utf-8").read())
    except Exception:
        resume_stats = job_stats = {"characters": 0, "words": 0, "sentences": 0}

    lines = [
        "=" * 70,
        "                 ATS RESUME ANALYSIS REPORT",
        "=" * 70,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "DOCUMENTS",
        "-" * 70,
        f"Resume: {resume_path}",
        f"Job Description: {job_path}",
        "",
        "MATCH SCORE",
        "-" * 70,
        f"ATS Keyword Match Score: {score}%",
        f"Alignment Level: {'EXCELLENT' if score >= 80 else 'GOOD' if score >= 60 else 'MODERATE' if score >= 40 else 'LOW'}",
        "",
        "KEYWORD SUMMARY",
        "-" * 70,
        f"Job Keywords: {result['total_job_keywords']}",
        f"Matched Keywords: {result['matched_count']}",
        f"Missing Keywords: {result['missing_count']}",
        "",
        "MATCHED KEYWORDS",
        "-" * 70,
    ]

    lines.extend([f"✓ {k}" for k in matched] if matched else ["No matching keywords found."])
    lines.extend(["", "MISSING KEYWORDS", "-" * 70])
    lines.extend([f"• {k}" for k in missing] if missing else ["No major missing keywords detected."])
    
    lines.extend(["", "RECOMMENDATIONS", "-" * 70])
    for i, rec in enumerate(recommendations, 1):
        lines.append(f"{i}. {rec}")

    return "\n".join(lines)


def save_report(report, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report)


# ============================================================
# MODULE 5: app.py (Main entrypoint)
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESUME_FILE = os.path.join(BASE_DIR, "sample_data", "resume.txt")
JOB_FILE = os.path.join(BASE_DIR, "sample_data", "job_description.txt")
REPORT_FILE = os.path.join(BASE_DIR, "ats_report.txt")


def main():
    print("\n" + "=" * 65)
    print("              ATS RESUME KEYWORD OPTIMIZER")
    print("=" * 65)
    
    # Ensure sample data directory exists for quick execution
    os.makedirs(os.path.join(BASE_DIR, "sample_data"), exist_ok=True)
    
    if not os.path.exists(RESUME_FILE):
        with open(RESUME_FILE, "w", encoding="utf-8") as f:
            f.write("Python Java SQL Git Machine Learning Data Structures")
    if not os.path.exists(JOB_FILE):
        with open(JOB_FILE, "w", encoding="utf-8") as f:
            f.write("Looking for software engineer with Python, Java, SQL, REST APIs, and Git.")

    try:
        resume_text = load_text_file(RESUME_FILE)
        job_text = load_text_file(JOB_FILE)
    except Exception as e:
        print(f"Error loading sample files: {e}")
        return

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)
    result = calculate_match(resume_keywords, job_keywords)
    report = generate_report(result, RESUME_FILE, JOB_FILE)

    print("\n" + report)
    save_report(report, REPORT_FILE)
    print(f"\nReport successfully generated and saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()

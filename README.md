📄 Resume Reviewer

An AI-powered Resume Feedback Tool built with Streamlit, LangChain, and Google Gemini AI. This app helps job seekers improve their resumes by providing detailed insights, including strengths, weaknesses, and actionable suggestions.

🚀 Features

Upload your resume as a PDF or paste the text directly.

AI-generated feedback highlighting:

✅ Strengths of your resume

⚠️ Weaknesses or missing elements

💡 Suggestions to improve formatting, content, and overall impact

Simple and interactive Streamlit UI.

🛠️ Tech Stack

Python – Core programming language

Streamlit – For building the web interface

LangChain – For prompt management and LLM integration

Google Gemini AI (via LangChain) – To analyze and generate feedback

PyMuPDF (fitz) – To extract text from uploaded PDF resumes

dotenv – To securely load API keys

📌 How It Works

Choose an input method: Upload PDF or Paste Text.

The app extracts text (if PDF is uploaded).

The extracted/pasted resume is passed to Gemini AI through LangChain.

AI analyzes and provides feedback under three categories:

Strengths

Weaknesses

Suggestions for improvement

Results are displayed in an easy-to-read format.

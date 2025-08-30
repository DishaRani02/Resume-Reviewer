import os
from dotenv import load_dotenv
import streamlit as st
import fitz  # for PDF
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.llm import LLMChain

load_dotenv()
genai.configure(api_key=("AIzaSyBirb5cAlfnhsXju4Lm4zD2VO956SOtYJI"))

st.title("📄 Resume Feedback")
option = st.radio("Choose input:", ["Upload PDF", "Paste Text"])
resume_text = ""

if option == "Upload PDF":
    file = st.file_uploader("Upload your resume", type="pdf")
    if file:
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                resume_text += page.get_text()
else:
    resume_text = st.text_area("Paste your resume here")

if resume_text:
    prompt = PromptTemplate.from_template(
        """Give feedback on this resume:
        {resume}
        Feedback should include:
        - Strengths
        - Weaknesses
        - Suggestions to improve"""
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.5,
        google_api_key=api_key
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    if st.button("Get Feedback"):
        with st.spinner("Analyzing..."):
            result = chain.invoke({"resume": resume_text})
            st.subheader("Feedback:")
            # Print result to check its structure if unsure
            if isinstance(result, dict):
                # Try both possible keys
                st.write(result.get("output", result.get("text")))
            else:
                st.write(result)

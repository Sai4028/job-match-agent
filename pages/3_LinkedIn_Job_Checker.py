import streamlit as st
import json

from service.profile_manager import load_profile
from service.ai_matcher import evaluate_job_fit

st.title("LinkedIn Job Checker")

profile = load_profile()

if not profile:
    st.warning("Please create your profile first.")
    st.stop()

ai_profile = profile.get("ai_profile", {})

if isinstance(ai_profile, str):
    ai_profile = json.loads(ai_profile)

api_key = st.secrets["GEMINI_API_KEY"]

job_title = st.text_input(
    "Job Title"
)

job_description = st.text_area(
    "Paste LinkedIn Job Description",
    height=300
)

if st.button("Analyze Job"):

    if not job_description:
        st.warning(
            "Please paste the job description."
        )
        st.stop()

    with st.spinner(
        "Analyzing..."
    ):

        result = evaluate_job_fit(
            ai_profile,
            job_title,
            job_description,
            api_key
        )

        st.subheader("Match Result")

        st.json(result)

import streamlit as st
from service.profile_manager import load_profile
from service.job_search import search_jobs
from service.scoring_engine import calculate_score
import json

st.title("Job Search")

profile = load_profile()

if not profile:
    st.warning("Please create your profile first.")
    st.stop()

ai_profile = profile.get("ai_profile", {})

# Handle old profiles where ai_profile was saved as string
if isinstance(ai_profile, str):
    ai_profile = json.loads(ai_profile)

recommended_roles = ai_profile.get(
    "recommended_roles",
    []
)

st.subheader("Recommended Roles")

selected_roles = []

for role in recommended_roles:
    if st.checkbox(role, value=True):
        selected_roles.append(role)

st.subheader("Preferred Industries")
st.write(
    ai_profile.get(
        "preferred_industries",
        []
    )
)

st.subheader("Locations")
st.write(
    profile.get(
        "locations",
        ""
    )
)

if st.button("Search Jobs"):

    jobs = search_jobs(selected_roles)

    st.subheader("Jobs Found")

    if not jobs:
        st.warning("No jobs found.")
    else:

        for job in jobs:

            score = calculate_score(
                job.get("title", ""),
                recommended_roles
            )

            recommendation = "Skip"

            if score >= 90:
                recommendation = "Strong Apply"
            elif score >= 75:
                recommendation = "Apply"
            elif score >= 60:
                recommendation = "Consider"

            st.info(
                f"""
Role: {job.get('title', 'N/A')}

Company: {job.get('company', 'N/A')}

Location: {job.get('location', 'N/A')}

Score: {score}%

Recommendation: {recommendation}
"""
            )

            if job.get("apply_link"):
                st.link_button(
                    "Apply",
                    job["apply_link"]
                )

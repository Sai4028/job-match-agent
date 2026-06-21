import streamlit as st
from service.profile_manager import load_profile
from service.job_search import search_jobs
from service.scoring_engine import calculate_score

st.title("Job Search")

profile = load_profile()

if not profile:
    st.warning("Please create your profile first.")
    st.stop()

ai_profile = profile.get("ai_profile", {})

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

    for job in jobs:

    score = calculate_score(
        job["title"],
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
    Role: {job['title']}
    
    Company: {job['company']}
    
    Location: {job['location']}
    
    Score: {score}%
    
    Recommendation: {recommendation}
    """
        )

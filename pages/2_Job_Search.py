import streamlit as st
import json

from service.profile_manager import load_profile
from service.linkedin_jobs import search_jobs
from service.ai_matcher import evaluate_job_fit

st.title("Job Search")

profile = load_profile()

if not profile:
    st.warning("Please create your profile first.")
    st.stop()

api_key = st.secrets["GEMINI_API_KEY"]

ai_profile = profile.get("ai_profile", {})

if isinstance(ai_profile, str):
    ai_profile = json.loads(ai_profile)

recommended_roles = ai_profile.get(
    "recommended_roles",
    []
)
st.subheader("Debug - Recommended Roles")

st.write(recommended_roles)

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

    with st.spinner("Searching and evaluating jobs..."):

        jobs = search_jobs(selected_roles)

        st.subheader("Jobs Found")

        if not jobs:

            st.warning("No jobs found.")

        else:

            for job in jobs:

                try:

                    result = evaluate_job_fit(
                        ai_profile,
                        job.get("title", ""),
                        job.get("description", ""),
                        api_key
                    )

                    score = result.get(
                        "score",
                        0
                    )

                    recommendation = result.get(
                        "recommendation",
                        "Unknown"
                    )

                    reason = result.get(
                        "reason",
                        ""
                    )

                    # Skip poor matches
                    if score < 40:
                        continue

                except Exception as e:

                    score = 0
                    recommendation = "Error"
                    reason = str(e)

                st.markdown(
                    f"""
                ### 🎯 {job['title']}
                
                **{job['company']}** | {job['location']}
                
                **Match Score:** {score}%
                """
                )
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if job.get("url"):
                        st.link_button(
                            "🔗 View Job",
                            job["url"]
                        )
                
                with col2:
                    st.button(
                        "📄 Generate Resume",
                        key=f"resume_{job['title']}"
                    )
                
                with st.expander("View Analysis"):
                
                    st.write(
                        f"**Recommendation:** {recommendation}"
                    )
                
                    st.write(
                        f"**Reason:** {reason}"
                    )
                
                st.divider()

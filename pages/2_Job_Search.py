import streamlit as st
import json

from service.profile_manager import load_profile
from service.linkedin_jobs import search_jobs
from service.ai_matcher import evaluate_job_fit
from service.resume_generator import generate_resume

st.title("Job Search")

if "evaluated_jobs" not in st.session_state:
    st.session_state["evaluated_jobs"] = []

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

# SEARCH JOBS

if st.button("Search Jobs"):

    with st.spinner("Searching and evaluating jobs..."):

        jobs = search_jobs(selected_roles)

        evaluated_jobs = []

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

                if score < 40:
                    continue

                job["evaluation"] = result

                evaluated_jobs.append(job)

            except Exception as e:

                st.error(
                    f"Error evaluating {job.get('title','')}: {str(e)}"
                )

        st.session_state["evaluated_jobs"] = evaluated_jobs

# DISPLAY JOBS

if st.session_state["evaluated_jobs"]:

    st.subheader("Jobs Found")

    for job in st.session_state["evaluated_jobs"]:

        result = job.get(
            "evaluation",
            {}
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

            if st.button(
                "📄 Generate Resume",
                key=f"resume_{job['title']}"
            ):

                try:

                    with st.spinner(
                        "Generating tailored resume..."
                    ):

                        tailored_resume = generate_resume(
                            ai_profile,
                            job.get(
                                "title",
                                ""
                            ),
                            job.get(
                                "description",
                                ""
                            ),
                            api_key
                        )

                        st.session_state[
                            f"resume_{job['title']}"
                        ] = tailored_resume

                except Exception as e:

                    st.error(
                        f"Resume Generation Error: {str(e)}"
                    )

        with st.expander("View Analysis"):

            st.write(
                f"**Recommendation:** {recommendation}"
            )

            st.write(
                f"**Reason:** {reason}"
            )

            st.json(result)

        resume_key = f"resume_{job['title']}"

        if (
            resume_key in st.session_state
            and st.session_state[resume_key]
        ):

            with st.expander(
                "📄 Tailored Resume",
                expanded=True
            ):

                st.markdown(
                    st.session_state[
                        resume_key
                    ]
                )

        st.divider()

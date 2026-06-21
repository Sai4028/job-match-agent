import streamlit as st
from service.profile_manager import load_profile

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
    st.success(
        f"Searching jobs for {len(selected_roles)} selected roles"
    )

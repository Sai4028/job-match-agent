import google.generativeai as genai


def generate_resume(
    ai_profile,
    job_title,
    job_description,
    api_key
):

    genai.configure(
        api_key=api_key
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are an expert ATS Resume Consultant.

Candidate Profile:

{ai_profile}

Target Job Title:

{job_title}

Target Job Description:

{job_description}

Your task is to tailor the candidate's resume for the target role.

IMPORTANT RULES:

1. Use only information available in the candidate profile.
2. Do NOT invent achievements.
3. Do NOT invent percentages, revenue impact, savings, growth numbers or metrics.
4. Do NOT invent company names.
5. Do NOT invent dates.
6. Do NOT generate placeholders such as:
   - [Phone Number]
   - [Email Address]
   - [LinkedIn URL]
   - [Location]
7. If information is unavailable, omit it.
8. Preserve all existing candidate information.
9. Focus on improving ATS relevance.
10. Highlight the most relevant skills and experiences for the target role.

Return the output in the following format:

# Professional Summary

Provide a tailored professional summary.

# Key Skills To Highlight

List the most relevant skills.

# Experience Areas To Emphasize

List relevant experience themes and accomplishments already present in the profile.

# ATS Keywords

List ATS keywords relevant to the target role.

# Resume Optimization Suggestions

Provide specific suggestions to improve the existing resume for this job.
"""

    response = model.generate_content(
        prompt
    )

    return response.text

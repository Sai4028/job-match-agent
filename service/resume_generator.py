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
You are an expert resume writer.

Candidate Profile:

{ai_profile}

Target Job Title:

{job_title}

Target Job Description:

{job_description}

Create a tailored resume.

Provide:

1. Professional Summary

2. Key Skills

3. Experience Highlights

4. ATS Keywords

Make it highly relevant for the target role.
"""

    response = model.generate_content(
        prompt
    )

    return response.text

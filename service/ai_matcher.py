import json
import google.generativeai as genai


def evaluate_job_fit(
    ai_profile,
    job_title,
    job_description,
    api_key
):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are an expert career coach.

Candidate Profile:
{json.dumps(ai_profile)}

Job Title:
{job_title}

Job Description:
{job_description}

Return ONLY JSON:

{{
  "score": 0,
  "recommendation": "",
  "reason": ""
}}

Rules:
- Score between 0 and 100
- Consider skills
- Consider domains
- Consider experience
- Consider seniority
- Consider transferable skills
"""

    response = model.generate_content(prompt)

    content = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(content)

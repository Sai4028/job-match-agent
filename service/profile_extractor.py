import json
import google.generativeai as genai


def extract_profile(resume_text, api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Analyze the following resume and return ONLY valid JSON.

    Extract:
    - name
    - total_experience
    - current_role
    - skills
    - domains
    - certifications

    Resume:
    {resume_text}
    """

    try:
        response = model.generate_content(prompt)
    
        content = response.text
    
        return content
        
    except Exception as e:
        return f"ERROR: {str(e)}"

import json
import google.generativeai as genai


def extract_profile(resume_text, api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are an expert resume analyzer.
    
    Analyze the resume and return ONLY valid JSON.
    
    Schema:
    
    {{
      "name": "",
      "total_experience": "",
      "current_role": "",
      "skills": {{
          "Product": [],
          "AI & Data": [],
          "Execution": []
      }},
      "domains": [],
      "certifications": [],
      "recommended_roles": [],
      "seniority_level": "",
      "preferred_industries": []
    }}
    
    Rules:
    - Return only valid JSON.
    - No markdown.
    - No explanations.
    - Infer suitable roles from experience and skills.
    - Infer seniority level.
    - Infer industries worked in.
    
    Resume:
    
    {resume_text}
    """

    try:
        response = model.generate_content(prompt)
    
        content = response.text
    
        return content
        
    except Exception as e:
        return f"ERROR: {str(e)}"

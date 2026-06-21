import requests


def search_jobs(selected_roles):

    jobs = []

    try:

        response = requests.get(
            "https://www.arbeitnow.com/api/job-board-api"
        )

        data = response.json()

        search_terms = []

        for role in selected_roles:

            role_lower = role.lower()

            if "product" in role_lower:
                search_terms.extend([
                    "product manager",
                    "product owner",
                    "product lead",
                    "head of product",
                    "principal product",
                    "group product"
                ])

            if "ai" in role_lower:
                search_terms.extend([
                    "ai product",
                    "genai",
                    "artificial intelligence"
                ])

            if "erp" in role_lower:
                search_terms.extend([
                    "erp",
                    "enterprise"
                ])

        search_terms = list(set(search_terms))

        for job in data.get("data", []):

            title = job.get(
                "title",
                ""
            ).lower()

            description = job.get(
                "description",
                ""
            ).lower()

            if any(
                term in title or term in description
                for term in search_terms
            ):

                jobs.append(
                    {
                        "title": job.get(
                            "title",
                            ""
                        ),
                        "company": job.get(
                            "company_name",
                            ""
                        ),
                        "location": job.get(
                            "location",
                            ""
                        ),
                        "description": job.get(
                            "description",
                            ""
                        ),
                        "apply_link": job.get(
                            "url",
                            ""
                        )
                    }
                )

        return jobs[:10]

    except Exception as e:

        return [
            {
                "title": "Error",
                "company": str(e),
                "location": "",
                "description": "",
                "apply_link": ""
            }
        ]

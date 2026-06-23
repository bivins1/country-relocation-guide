def generate_country_guide(client, country_data, guide_type) -> str:
    """
    Generates a simple, easy to read guide using Gemini AI based on the user's choice.
    """

    if guide_type == "vacation":
        prompt = f"""
        You are a vacation assistant.
        Generate a simple travel guide for people looking to have a vacation using the provided country data.
        Use this structure when providing your answer:
        Overview
        Culture
        Country Landmarks
        Travel Tips

        This is the provided country data:
        {country_data}
        """

    elif guide_type == "relocation":
        prompt = f"""
        You are a relocation assistant.
        Generate a simple travel guide for people looking to relocate using the provided country data.
        Use this structure when providing your answer:
        Overview
        Cost of Living
        Culture
        Security
        Travel Tips

        This is the provided country data:
        {country_data}
        """

    elif guide_type == "study":
        prompt = f"""
        You are an expert international student advisor.

        Generate a STUDY GUIDE for international students who want to study in this country.

        IMPORTANT: Focus ONLY on education and student life.

        Use this structure:

        1. Education System Overview
        2. Top Universities & Admission Requirements
        3. Tuition Fees & Cost of Living
        4. Scholarships & Financial Aid
        5. Student Visa Requirements
        6. Student Life & Culture
        7. Final Advice for International Students

        Keep it simple, practical, and easy to understand.

        Country data:
        {country_data}
        """
    else:
        raise ValueError("Invalid guide type provided.")

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        return response.text

    except Exception as e:
        raise RuntimeError(f"Error generating the guide: {e}") from e
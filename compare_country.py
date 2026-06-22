# from fetch_country import fetch_country 
# from initialize_gemini import initialize_gemini
# from save_comparison import save_comparison

# def compare_countries():
#     print("compare two countries of your choosing")

#     country1_name=input("what is the first country: ").strip().lower()
#     country2_name=input("what is the second country:").strip().lower()

#     if not country1_name or country2_name:
#         print("no choice made. Exiting.....")
#         return
    
#     country1 = fetch_country(country1_name)
#     country2 = fetch_country(country2_name)

#     if not country1 or country2:
#         print("country not found. Exiting ...")
#         return
    
#     try:
#         client=initialize_gemini()
#     except Exception as e:
#         print(f"Failed to initialize AI: {e}")
#         return

#     prompt = f"""
#     You are an international travel advisor.

#     Compare these two countries side by side.

#     Country 1:
#     {country1}

#     Country 2:
#     {country2}

#     Include:

#     1. Overview
#     2. Similarities
#     3. Major Differences
#     4. Time Zone Comparison
#     5. Travel Comparison
#     6. Study Comparison
#     7. Relocation Comparison
#     8. Cost of Living
#     9. Safety
#     10. Final Recommendation

#     Keep the response concise and professional.
#     """
#     comparison=''
#     try:
#        response =client.models.generate_content(
#         model="gemini-3.5-flash",
#         contents=prompt )
       
#        comparison=response.text or ""
#        print(comparison)
       

#     except Exception as e:
#         print(f"Error generating comparison: {e}")
#         return


#     choice = input("\nSave comparison? (yes/no): ").strip().lower()

#     if choice == "yes":
#         filename = f"{country1_name}vs{country2_name}.txt"
#         save_comparison(comparison, filename)
#     elif choice == "no":
#         print("Comparison discarded.")
#     else:
#         print("Invalid choice.")


from fetch_country import fetch_country
from initialize_gemini import initialize_gemini


def compare_countries(country1_name, country2_name):

    country1 = fetch_country(country1_name)
    country2 = fetch_country(country2_name)

    if not country1 or not country2:
        return "One or both countries are invalid."

    try:
        client = initialize_gemini()
    except Exception as e:
        return f"Failed to initialize AI: {e}"

    prompt = f"""
    Compare these two countries:

    Country 1:
    {country1}

    Country 2:
    {country2}

    Include:
    - Overview
    - Similarities
    - Differences
    - Time zones
    - Travel comparison
    - Study comparison
    - Relocation comparison
    - Final recommendation

    Keep it concise and structured.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text or ""

    except Exception as e:
        return f"Error generating comparison: {e}"
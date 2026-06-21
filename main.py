from search_country import country_search
from generate_checklist import travel_checklist
from compare_country import compare_countries


def main():

    while True:

        print("\n" + "=" * 55)
        print("           COUNTRY RELOCATION GUIDE")
        print("=" * 55)

        print("\nYour AI assistant for:")
        print("• Country vacation guides")
        print("• Country relocation guides")
        print("• Study abroad guides")
        print("• Personalized travel checklists")
        print("• Side-by-side country comparisons")

        print("\nPlease choose an option:\n")
        print("1. Search a country and generate a guide")
        print("2. Generate a travel checklist")
        print("3. Compare two countries")
        print("4. Exit")

        user_option = input("\nEnter your choice: ").strip()

        if user_option == "1":
            country_search()

        elif user_option == "2":
            travel_checklist()

        elif user_option == "3":
            compare_countries()

        elif user_option == "4":
            print("\nThank you for using Country Relocation Guide.")
            print("Safe travels and best wishes on your journey! 🌍")
            break

        else:
            print("\nInvalid option. Please choose 1, 2, 3, or 4.")

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()
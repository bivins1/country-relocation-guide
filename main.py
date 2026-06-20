from search_country import country_search
from generate_checklist import travel_checklist
from compare_country import compare_countries

def main():

    print("WELCOME TO COUNTRY RELOCATION GUIDE, we provide you with country relocation guides\n country vacation guides\n country study guides.\n We also help you with your tavel checklist depending on the occasion and help you compare countries to halp facilitate your decision making  ")

    print("1. search country and generate relevant guide\n")
    print("2. generate travel checklist\n")
    print("3. compare countries\n")

    user_option=input("please choose an option:").strip().lower()

    
    if user_option == "1":
       country_search()

    if user_option=="2":
        travel_checklist()

    if user_option == "3":
        compare_countries()

    else:
        print("invalid option, please choose 1, 2 or 3")
        return
    

if __name__ == "__main__":
    main()


    



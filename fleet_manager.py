# Fleet manager modular system
def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Troi"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Command"]
    ids = ["001", "002", "003", "004", "005"]
    return names, ranks, divs, ids

def display_menu():
    print("\n=== FLEET MANAGEMENT SYSTEM ===")
    print("1. Display Roster")
    print("2. Add Crew Member")
    print("3. Remove Crew Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    
    choice = input("Select option: ")
    return choice

def main():
    names, ranks, divs, ids = init_database()
    print("FLEET MANAGEMENT SYSTEM v2.0")
    
    while True:
        choice = display_menu()
        
        if choice == "2":
            add_member(names, ranks, divs, ids)
        elif choice == "3":
            remove_member(names, ranks, divs, ids)
        elif choice == "9":
            print("Shutting down...")
            break
        else:
            print(f"Option {choice} - Coming soon!")

if __name__ == "__main__":
   main()
   
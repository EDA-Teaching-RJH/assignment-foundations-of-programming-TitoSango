# Fleet manager modular system
def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Troi"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Command"]
    ids = ["001", "002", "003", "004", "005"]
    return names, ranks, divs, ids


# Display roster
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

# Add member function
def add_member(names, ranks, divs, ids):
    new_id = input("Enter ID: ")
    if new_id in ids:
        print("ID already exists")
        return
    
    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    new_rank = input("Enter Rank: ")
    if new_rank not in valid_ranks:
        print("Invalid rank")
        return
    
    new_name = input("Enter Name: ")
    new_div = input("Enter Division: ")
    
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    
    print("Member added")


# Remove member by ID
def remove_member(names, ranks, divs, ids):
    target_id = input("Enter ID to remove: ")
        
    if target_id not in ids:
        print("ID not found")
        return
        
    idx = ids.index(target_id)
        
    removed_name = names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)
        
    print(removed_name + " removed")


# Update rank function
def update_rank(names, ranks, ids):
    target_id = input("Enter ID to update: ")
    
    if target_id not in ids:
        print("ID not found")
        return
    
    idx = ids.index(target_id)
    
    print("Current rank: " + ranks[idx])
    
    new_rank = input("Enter new rank: ")
    ranks[idx] = new_rank
    
    print("Rank updated")



def main():
    names, ranks, divs, ids = init_database()
    print("FLEET MANAGEMENT SYSTEM")
    
    while True:
        choice = display_menu()

        if choice == "1":
            display_roster(names, ranks, divs, ids)
        elif choice == "2":
            add_member(names, ranks, divs, ids)
        elif choice == "3":
            remove_member(names, ranks, divs, ids)
        elif choice == "4":
            update_rank(names, ranks, ids)
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
        elif choice == "6":
            filter_by_division(names, divs)
        elif choice == "7":
            calculate_payroll(ranks)
        elif choice == "8":
            count_officers(ranks)
        elif choice == "9":
            print("Shutting down...")
            break
        else:
            print(f"Option {choice} - Coming soon!")

if __name__ == "__main__":
   main()
   
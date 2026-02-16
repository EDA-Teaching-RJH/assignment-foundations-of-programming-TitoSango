# Fleet manager modular system
def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Troi"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Command"]
    ids = ["001", "002", "003", "004", "005"]
    return names, ranks, divs, ids

def main():
    names, ranks, divs, ids = init_database()
    print(f"Loaded {len(names)} crew members")

if __name__ == "__main__":
   main()
   
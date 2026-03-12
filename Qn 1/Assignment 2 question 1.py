# Function to find teammates
def find_teammates(number_needed):
    print("Searching for", number_needed, "teammate(s)...")


# Function for battle royale mode
def battle_royale():
    # Read the number of players already in the team
    players = int(input("Enter number of players in your team: "))

    # A full team has 3 players
    teammates_needed = 3 - players

    # Call function to find the remaining teammates
    find_teammates(teammates_needed)

    # Start the match
    print("Match starting . . .")


# Function for practice mode
def practice():
    # Read the desired map for practice mode
    desired_map = input("Enter the map for practice: ")

    # Print launch message
    print("Launching practice on", desired_map)


# Main program
mode = input("Enter game mode (br for battle royale): ")

# Decide which mode to launch
if mode == "br":
    battle_royale()
else:
    practice()
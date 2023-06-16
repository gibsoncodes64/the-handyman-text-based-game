import time

def introduction():
    print("Welcome to Shadows of Redemption!")
    time.sleep(2)
    print("You are Kael, a lone swordsman on a quest to save the town of Eldridge from the Shadowfiend.")
    time.sleep(2)
    print("Your journey begins now!\n")

def explore_town():
    print("You arrive in the town of Eldridge, shrouded in fear and darkness.")
    time.sleep(2)
    print("The townsfolk are hiding, and the streets are empty.")
    time.sleep(2)
    print("Where would you like to go?")
    time.sleep(1)
    print("1. The Elder's House")
    time.sleep(1)
    print("2. The Crypts")
    time.sleep(1)

def elder_house():
    print("You enter the Elder's House and meet Seraphina, the town's wise sage.")
    time.sleep(2)
    print("She tells you about the Shadowfiend and the ancient Luminar Stone that can defeat it.")
    time.sleep(2)
    print("Seraphina provides you with a map to the crypts and wishes you luck on your journey.")
    time.sleep(2)

def crypts():
    print("You enter the crypts, guided by the map provided by Seraphina.")
    time.sleep(2)
    print("As you navigate the treacherous maze, you encounter traps and monstrous creatures.")
    time.sleep(2)
    print("You must overcome these obstacles to reach the heart of the crypts.")
    time.sleep(2)
    print("Finally, you stand before the Shadowfiend, ready to face your ultimate challenge.")
    time.sleep(2)

def battle():
    print("The Shadowfiend engulfs the chamber in darkness, making it difficult to see.")
    time.sleep(2)
    print("What would you like to do?")
    time.sleep(1)
    print("1. Attack with your sword")
    time.sleep(1)
    print("2. Use the Luminar Stone")
    time.sleep(1)

def ending_victory():
    print("You strike the Shadowfiend with the Luminar Stone, breaking through its darkness.")
    time.sleep(2)
    print("The creature lets out a final wail and dissipates, leaving only fading shadows.")
    time.sleep(2)
    print("You have saved the town of Eldridge and brought light back to its people!")
    time.sleep(2)
    print("Congratulations! You have achieved redemption and fulfilled your heroic destiny.")
    time.sleep(2)
    print("Thank you for playing Shadows of Redemption.")

def ending_defeat():
    print("Your attacks are futile against the Shadowfiend's incorporeal form.")
    time.sleep(2)
    print("The creature overwhelms you with its power, and darkness consumes everything.")
    time.sleep(2)
    print("Your journey ends here, but the legend of the Shadowfiend's reign of terror lives on.")

def play_game():
    introduction()
    explore_town()

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        elder_house()
        crypts()
    elif choice == '2':
        crypts()
    else:
        print("Invalid choice. Please try again.")
        play_game()

    battle_choice = input("Enter your choice (1 or 2): ")

    if battle_choice == '1':
        ending_defeat()
    elif battle_choice == '2':
        ending_victory()
    else:
        print("Invalid choice. Please try again.")
        play_game()

play_game()

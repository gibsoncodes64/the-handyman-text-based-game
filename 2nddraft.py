# ASCII Title
print("|                                            _________________  ____   ____      ______                                                                             |")
print("|                                           /                 \|    | |    | ___|\     \                                                                            |")
print("|                                           \______     ______/|    | |    ||     \     \                                                                           |")
print("|                                              \( /    /  )/   |    |_|    ||     ,_____/|                                                                          |")
print("|                                               ' |   |   '    |    .-.    ||     \--'\_|/                                                                          |")
print("|                                                 |   |        |    | |    ||     /___/|                                                                            |")
print("|                                                /   //        |    | |    ||     \____|\                                                                           |")
print("|                                               /___//         |____| |____||____ '     /|                                                                          |")
print("|                                              |`   |          |    | |    ||    /_____/ |                                                                          |")
print("|                                              |____|          |____| |____||____|     | /                                                                          |")
print("|                                                \(              \(     )/    \( |_____|/                                                                           |")
print("|                                                 '               '     '      '    )/                                                                              |")
print("|                                                                                   '                                                                               |")                                                                                                                         
print("|                    ____   ____        ____  _____   ______        _____    _____      _____    ______  _______          ____  _____   ______                      |")
print("|                   |    | |    |  ____|\   \|\    \ |\     \   ___|\    \  |\    \    /    /|  |      \/       \    ____|\   \|\    \ |\     \                     |")
print("|                   |    | |    |/     /\    \\\    \| \     \ |    |\    \ | \    \  /    / | /          /\      \ /    /  \   \\\     \| \     \                    |")
print("|                   |    |_|    ||    |  |    |\|    \  \     ||    | |    ||  \____\/    /  //     /\   / /\     ||    |  |    |\|    \  \     |                   |")
print("|                   |    .-.    ||    |__|    | |     \  |    ||    | |    | \ |    /    /  //     /\ \_/ / /    /||    |__|    | |     \  |    |                   |")
print("|                   |    | |    ||    .--.    | |      \ |    ||    | |    |  \|___/    /  /|     |  \|_|/ /    / ||    .--.    | |      \ |    |                   |")
print("|                   |    | |    ||    |  |    | |    |\ \|    ||    | |    |      /    /  / |     |       |    |  ||    |  |    | |    |\ \|    |                   |")
print("|                   |____| |____||____|  |____| |____||\_____/||____|/____/|     /____/  /  |\____\       |____|  /|____|  |____| |____||\_____/|                   |")
print("|                   |    | |    ||    |  |    | |    |/ \|   |||    /    | |    |`    | /   | |    |      |    | / |    |  |    | |    |/ \|   ||                   |")
print("|                   |____| |____||____|  |____| |____|   |___|/|____|____|/     |_____|/     \|____|      |____|/  |____|  |____| |____|   |___|/                   |")
print("|                     \(     )/    \(      )/     \(       )/    \(    )/          )/           \(          )/       \(      )/     \(       )/                     |")
print("|                      '     '      '      '       '       '      '    '           '             '          '         '      '       '       '                      |")
print("|                                                              (A desk 2 game)                                                                                      |")
print("|                                                         (Welcome to The Handyman)                                                                                 |")


lines = ["____________________________________________________________________________________________________________________________________________________"]

from time import sleep
import sys

for line in lines:                  # for each line of text (or each message)
    for c in line:                  # for each character in each line
        print(c, end='')            # print a single character, and keep the cursor there.
        sys.stdout.flush()          # flush the buffer
        sleep(0.01)                  # wait a little to make the effect look good

# Welcome screen
print("Welcome to 'The Handyman Game'")
print("Type (s) to start the adventure")
print("Type (c) to view credits")

import time
while True:
    choice = input("Enter your choice: ")

    if choice.lower() == "c":
        # Credits screen
        print("Credits:")
        print("Game created by [Laiq,Kurtis,Evan,samuel,payikene]")
        print("Artwork by [Artist Name]")
        print("Special thanks to [Acknowledgements]")
        print("Game powered by Python")
    elif choice.lower() == "s":
    # Name input
        print("Starting the adventure...")
        print("Tell me, hero, what should we call you?")
    name = input("Enter your name: ")
    print("Hello",name)
    print(f"Welcome to Eldridge Well more Specifically the outskirts of Eldridge this is the home of a great warrior and even better swordsman\nthe stuff of the legend can you guess who it is yet?.")
    time.sleep(1)
    print("You are a great warrior, an even better swordsman... the stuff of legend.")
    time.sleep(1)  # Simulate delay for dialogue/artwork
    print("You,", name + " are known as 'The Handyman'.")
    print("You have won many battles in your life, but Eldridge has been quiet recently.")
    break
while True:
    choice = input("Read A Letter:Y/N: ")
    if choice.lower() == "Y":
        # Credits screen
      print("You wake up to a very official-looking wax-sealed letter by your door...")
    time.sleep(2)  # Simulate delay for dialogue
    # Read letter
    print("You read the letter:")
    print("Dear", name + ",")
    print(f"We have relied on you in the past, and the time has come again when we need your help!")
    print(f"The town of Eldridge has fallen victim to a mysterious creature that is ravaging our crops and taking our livestock.")
    print(f"Please come to the center of Eldridge town and see for yourself.")
    print(f"You're our only hope.")
    print(f"Sincerely,")
    print(f"Lorelai, Town Mayor")
    break
 # Accept task
while True:
    choice = input("Will you accept the task? (Yes/No): ")

    if choice.lower() == "yes":
        # You agreed to save the town
        print(f"You have agreed to save the town!")
        print(f"Armed with only your sword and an unyielding spirit, you embark on your journey.")
        time.sleep(2)  # Simulate delay for dialogue/artwork

        # Load artwork of a boarded-up cabin
        print(f"You arrive in a desolate-looking village.")
        print(f"Most windows and doors are boarded shut, and an eerie silence fills the air.")
        print(f"Only three people are in sight: a guard, a farmhand, and a blacksmith.")

        # Who do you speak to?
        person = input(f"Who would you like to talk to? (Guard/Farmhand/smithi): ")

        if person.lower() == "guard":
            # Guard dialogue
            print(f"The guard looks at you and shrugs. It's clear he doesn't trust you.")

        elif person.lower() == "farmhand":
            # Farmhand dialogue
            print(f"The farmhand greets you and says, 'Greetings,", name + ".'")
            print(f"'I think you'd better come with me.'")
            print(f"The farmhand takes you to the last known location")
            print(f"See Animals remains and hear nosise")
              
        elif person.lower() == "smithi":
            # Blacksmith dialogue
            print(f"The blacksmith exclaims, 'Hello,", name + "! It's such a pleasure to meet somebody of your stature.'")
            print(f"'Wait a minute... You can't be serious... coming to fight with a blade as wretched as that?!'")
            choice = input("Let me sharpen it for you? (Yes/No): ")
            if choice.lower() == "yes":
                # Sharpen sword
                print(f"The blacksmith sharpens your sword, making it more effective in battle.")
            elif choice.lower() == "no":
                # Decline sword sharpening
                print(f"You decline the blacksmith's offer and decide to go about your day.")
                print(f"However, your sword remains dull and may not be as effective against the creature.")
            
            else:
                # Invalid choice
                print("Invalid choice!")

        else:
            # Invalid choice
            print("Invalid choice!")

    elif choice.lower() == "no":
        # You chose not to accept the task
            print("You are not the hero we once thought you were.")
            print("Game over.")
    
    else:
        # Invalid choice
        print("Invalid choice!")
    break
        
else:
    # Invalid choice
        print("Invalid choice!")
    
while True:

    person=input("Investigate(Sounds/Remains): ")
    if person.lower()=="sounds":
                print(f" You Followed the Sound and your are suddently Attacked by the Monster")
    elif person.lower()== "Remains":
                print(f"Fallow Trail Leading to the Creature")
    person=input("Observe/Attack: ")
    if person.lower()=="observe":
            print(" Observe Scar Chance to stun")
    elif person.lower() =="Attack":
                print("Attack is in Progress") 
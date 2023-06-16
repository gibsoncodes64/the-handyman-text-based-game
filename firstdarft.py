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
    print(f"Welcome to Eldridge Well more Specifically the outskirts of Eldridge this is the home of a great warrior and even better swordsman, the stuff of the legend can you guess who it is yet?.")
    time.sleep(1)
    print("You are a great warrior, an even better swordsman... the stuff of legend.")
    time.sleep(1)  # Simulate delay for dialogue/artwork
    print("You,", name + ", are known as 'The Handyman'.")
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
    print("We have relied on you in the past, and the time has come again when we need your help!")
    print("The town of Eldridge has fallen victim to a mysterious creature that is ravaging our crops and taking our livestock.")
    print("Please come to the center of Eldridge town and see for yourself.")
    print("You're our only hope.")
    print("Sincerely,")
    print("Lorelai, Town Mayor")
    break
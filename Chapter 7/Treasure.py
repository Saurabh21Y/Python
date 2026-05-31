# Treasure Island - Text Adventure Game
# A game of choice, wit, and survival.

import time

def print_pause(message, delay=1.5):
    """Prints a message and pauses for a short duration to build suspense."""
    print(message)
    time.sleep(delay)

def play_game():
    # Title Screen and Intro
    print(r'''
*******************************************************************************
          __________
         /\____;;____\
        | /      /   /\
        |/____  /___/  \
        |   /| |   |   |
        |  / | |   |   |
        | /  | |___|___|
        |/___|/____;;___\
        /               \
       /_________________\
*******************************************************************************
''')
    print("Welcome to Treasure Island!")
    print("Your mission is to find the lost treasure of Captain Flint.")
    print("Choose wisely, as one wrong step could lead to your doom...\n")
    time.sleep(2)

    has_key = False

    # --- Choice 1: The Crossroad ---
    print_pause("You find yourself standing at a foggy crossroad near the shoreline.")
    print_pause("The sandy path to the right leads along a windy cliff.")
    print_pause("The narrow path to the left leads deep into a dark, whispering forest.")
    
    choice1 = input("Which direction do you want to go? Type 'left' or 'right': ").strip().lower()
    print()

    if choice1 == "left":
        # --- Path Left: The Forest ---
        print_pause("You venture into the dark jungle. The trees arch overhead, blocking out the sky.")
        print_pause("As you walk, you notice a strange hollow tree trunk glowing with a faint, magical blue light.")
        
        choice2 = input("Do you want to 'search' the hollow tree or 'ignore' it and walk on? ").strip().lower()
        print()

        if choice2 == "search":
            print_pause("You reach your hand into the glowing hollow...")
            print_pause("Your fingers brush against metal. You pull out a heavy, sparkling Golden Key!")
            print_pause("You tuck the key safely into your pocket and continue along the path.")
            has_key = True
        else:
            print_pause("You decide it's safer not to touch unknown glowing objects.")
            print_pause("You walk past the tree and keep moving forward.")

        # --- Choice 3: The Lake ---
        print_pause("\nAfter walking for another mile, the trees part.")
        print_pause("You stand at the edge of a vast, mist-covered lake.")
        print_pause("In the middle of the lake sits a mysterious dark castle, glowing under the moonlight.")
        print_pause("There are no bridges, and the water looks deep and cold.")

        choice3 = input("Do you want to 'swim' across or 'wait' at the shore? ").strip().lower()
        print()

        if choice3 == "swim":
            print_pause("You jump into the chilly water and begin swimming toward the castle.")
            print_pause("The water is peaceful... until you notice a massive shadow moving rapidly beneath you.")
            print_pause("Suddenly, a giant prehistoric crocodile surges from the depths!")
            print_pause("GAME OVER: You became a midnight snack for the beast of the lake.")
            return
        
        elif choice3 == "wait":
            print_pause("You decide to wait patiently by the shore.")
            print_pause("A low, rhythmic creaking sound echoes across the water.")
            print_pause("Out of the thick mist, a mysterious hooded boatman in a wooden ferry approaches.")
            print_pause("He stops at the dock and looks at you with hollow, glowing eyes.")

            if has_key:
                print_pause("\nThe boatman spots the Golden Key peeking out of your pocket.")
                print_pause("He bows silently and says: 'Ah! You possess the key to Captain Flint's vault.'")
                print_pause("'I shall row you across for free.'")
                print_pause("He motions for you to step aboard and slowly rows you across the calm lake to the castle.")
            else:
                print_pause("\nThe boatman speaks in a raspy voice:")
                print_pause("'Only those with the key, or the wits to match, may cross.'")
                print_pause("'Answer my riddle, and I shall ferry you. Fail, and you remain stranded forever.'")
                
                riddle_answer = input("\n'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?' \nAnswer: ").strip().lower()
                print()

                if "echo" in riddle_answer:
                    print_pause("The boatman nods slowly. 'Correct.'")
                    print_pause("He gestures for you to step aboard and silently rows you across the lake to the castle.")
                else:
                    print_pause("The boatman shakes his head. 'Incorrect. The answer was an echo.'")
                    print_pause("He rows back into the mist, leaving you stranded as the tide rises.")
                    print_pause("GAME OVER: Stranded on the shore forever.")
                    return

            # --- Choice 4: The Castle Doors ---
            print_pause("\nYou step off the ferry and stand before the colossal iron gates of the castle.")
            print_pause("You push them open and enter a grand, silent hall.")
            print_pause("In front of you are three colored doors: Red, Blue, and Yellow.")
            print_pause("Looking closely at the dusty floor, you also notice a small wooden trapdoor hidden under an old rug.")

            choice4 = input("Which door will you open? Type 'red', 'blue', 'yellow', or 'trapdoor': ").strip().lower()
            print()

            if choice4 == "red":
                print_pause("You open the Red door.")
                print_pause("A blinding blast of roaring dragon fire bursts out of the room!")
                print_pause("GAME OVER: You were roasted to a crisp.")
            elif choice4 == "blue":
                print_pause("You open the Blue door.")
                print_pause("A pack of hungry, snarling shadow beasts lunges out from the darkness!")
                print_pause("GAME OVER: You were eaten by the beasts.")
            elif choice4 == "yellow":
                print_pause("You open the Yellow door.")
                print_pause("Inside the room, you see a majestic treasure chest sitting on a stone pedestal.")
                
                if has_key:
                    # (Note: In the current flow, we gave the key to the boatman if we had it,
                    # unless we solved the riddle instead. But let's check if the player still has a key or not.
                    # Actually, if we solved the riddle and kept the key, or if we didn't search the tree, we don't have it.)
                    print_pause("You insert your Golden Key into the lock and turn it.")
                    print_pause("The chest clicks open! It's filled with glittering diamonds, gold coins, and ancient crowns!")
                    print_pause("YOU WIN! You have claimed the ultimate treasure of Captain Flint!")
                else:
                    print_pause("The treasure chest is locked tight with a heavy brass padlock.")
                    print_pause("You try to pry it open with a nearby stone, but you trigger a hidden pressure plate!")
                    print_pause("The walls begin to rumble, and the ceiling collapses on top of you!")
                    print_pause("GAME OVER: Crushed by the castle's ancient traps.")
            elif choice4 == "trapdoor":
                print_pause("You pull back the dusty rug and open the creaking wooden trapdoor.")
                print_pause("You slide down a long, winding stone slide into the darkness...")
                print_pause("...and land softly on a massive pile of plush, velvet cushions!")
                print_pause("You look around in awe. You are directly inside the treasure vault!")
                print_pause("The vault doors are open, and mountains of gold, rubies, and gems surround you.")
                print_pause("YOU WIN! You found the secret vault and escaped with the legendary treasure!")
            else:
                print_pause("You hesitate and stand frozen, unable to decide.")
                print_pause("A trapdoor opens beneath your feet, plunging you into an endless abyss.")
                print_pause("GAME OVER: Indecision was your downfall.")
        else:
            print_pause("GAME OVER: Invalid choice led you to wander into a quicksand pit.")

    elif choice1 == "right":
        # --- Path Right: Quicksand/Beach ---
        print_pause("You walk along the windy cliff shoreline.")
        print_pause("The beautiful ocean waves distract you, and you don't notice the ground beneath you shifting.")
        print_pause("You step directly into a patch of deep, sinking quicksand!")
        print_pause("As you struggle, you sink faster. The sea tide rises, and the waves wash over you.")
        print_pause("GAME OVER: Drowned in quicksand.")
    else:
        print_pause("You stand frozen at the crossroad, unable to make a decision.")
        print_pause("Suddenly, a pack of wild island wolves emerges from the mist and chases you off the cliff!")
        print_pause("GAME OVER: Death by indecision.")

if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if replay != "yes" and replay != "y":
            print("\nThanks for playing Treasure Island! Goodbye!")
            break
        print("\n" * 5)

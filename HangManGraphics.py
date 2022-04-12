def HangMan(x):  # function to play/choose the graphics
    if x == 0: # starting hangman
        print("   __________  ")
        print("   |        |  ")
        print("   |           ")
        print("   |           ")
        print("   |           ")
        print("   |           ")
        print(" __|________   ")
    elif x == 1:
        x = x + 1
        print("   __________  ")
        print("   |        |  ")
        print("   |        0  ")
        print("   |           ")
        print("   |           ")
        print("   |           ")
        print(" __|________   ")
    elif x == 2:
        x = x + 1
        print("   __________  ")
        print("   |        |  ")
        print("   |        0  ")
        print("   |        |  ")
        print("   |           ")
        print("   |           ")
        print(" __|________   ")
    elif x == 3:
        x = x + 1
        print("   __________  ")
        print("   |        |  ")
        print("   |        0  ")
        print("   |        |  ")
        print("   |        |  ")
        print("   |           ")
        print(" __|________   ")
    elif x == 4:
        x = x + 1
        print("   __________  ")
        print("   |        |  ")
        print("   |        0  ")
        print("   |        |\ ")
        print("   |        |  ")
        print("   |           ")
        print(" __|________   ")
    elif x == 5:
        x = x + 1
        print("   __________  ")
        print("   |        |  ")
        print("   |        0  ")
        print("   |       /|\ ")
        print("   |        |  ")
        print("   |           ")
        print(" __|________   ")
    elif x == 6: # last chance
        x = x + 1
        print("   __________  ")
        print("   |        |  ")
        print("   |        0  ")
        print("   |       /|\ ")
        print("   |        |  ")
        print("   |       /   ")
        print(" __|________   ")
        print("On more wrong and you're dead...")
    elif x == 7:  # you die
        print("   __________  ")
        print("   |        |  ")
        print("   |        0  ")
        print("   |       /|\ ")
        print("   |        |  ")
        print("   |       / \ ")
        print(" __|________   ")
        print("You died...")
        exit()  # stop code
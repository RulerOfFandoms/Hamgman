# Open hangman.txt
f = open("hangman.txt", "r")
hangmanword = (f.read())
f.close()

print('''You're going to play hangman. You try to guess the word by entering letters. You get 8 wrong and your man
dies. \nWhen entering guesses, please enter in uppercase.\n''')
#rules/instructions

LetterList = list(hangmanword) # insert word into list
x = 0 # starting number from wrong guesses

#print(LetterList)
displaylist = [] # make list
for i in LetterList:
    displaylist.append("_")  # add blank spaces

def winner():  # if you win
    print('''YOU'RE A WINNER!!''')
    exit()

print(displaylist) #print the list with blanks
def letterguess(): # guessing letters
    global LetterList
    global displaylist
    global x
    global counter
    guess = input("Please guess a letter :")
    counter = 0  # starts variable for checking through list
    for i in LetterList:
        if guess == i:
            displaylist.pop(counter) # removes thing in the place holder
            displaylist.insert(counter,guess) # adds guess into place holder
            counter = counter + 1
        else:
            counter = counter + 1
            x = x + 1 # adds to number of wrongs





while True:
    if displaylist == ['d', 'i', 'n', 'o', 's', 'a', 'u', 'r']: # full list
        winner()
    else:
        letterguess()
        x = x + 1 - counter # how many you got wrong
        print("Guesses wrong: " + str(x)) # number of wrong guesses
        from HangManGraphics import HangMan #import other file
        HangMan(x) # brings varable x to other file
        print(displaylist) # prints updated list


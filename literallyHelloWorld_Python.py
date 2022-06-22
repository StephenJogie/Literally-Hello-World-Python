# Version 0.1.1 of literally just Hello World in Python 3.7
# Additions in 0.1.1:
#     1. stringManipulationForFunIGuess(input) function was added (need to import random for the fun)
#       -Makes a copy of an input string and randomly capitalizes characters
#       -Prints the original and then the new version to console. Pretty cool I guess
# Additions in 0.1.2:
#     2. replace all camelCase with snake_case because that's what the PEP-8 style guide says

import random as randy
indentLvl = 3 #Global variable ew

def literallyHelloWorld() -> None:
    print("Hello World")
    return

def helloSomeArgument(object: str) -> None:
    print("Hello " + object)
    return

def userInterface() -> int:
    print("So, anyways, pick which version of Hello World you want to play I guess: \n")
    print("\t"*indentLvl + "1. Classic Version for the purists")
    print("\t"*indentLvl + "2. Gamer Version for the Gaming Gamers with working keyboards! \n")
    userChoice = int(input("Make your choice (1 or 2): ")) #please enter an actual integer dear god
    return userChoice

def stringManipulationForFunIGuess(input: str) -> None:
    """
    |Inputs : Some input string
    |Outputs : Prints to console the input string with characters randomly capitalized
    |Does not return anything, maybe change later to return the string of the result if needed
    |Process: 1. Make a list of the input string converted to lowercase
    |         2. traverse the list and randomly capitalize letters, use random library
    |         3. Convert the result list to a string and print to console
    """
    listCopy = list(input.lower())  
    sizeOfThing = len(input)
    for x in range(0,sizeOfThing-1):
        isCap = randy.randint(0,1)
        if (isCap == 1):
            listCopy[x]=listCopy[x].upper()
    copy = ''.join(listCopy)
    print("Original: %s" % str(input))
    print("New and Improved: %s" % copy)
    return

    
def main() -> None:
    print("I'm trying to learn some python so my friends don't call me a boomer anymore \n \n")
    chooseQuit = 0
    while (chooseQuit == 0):
    
        input1 = int(userInterface())

        if (input1 == 1):
            literallyHelloWorld()
        else:
            object = str(input("Okay gamer, what/who do you want to say hello to: "))
            helloSomeArgument(object)
        chooseQuit = int(input("\n \n Want to Quit (1 for yes, 0 for no): "))
        print("\n \n \n")

    print("Thanks for gaming I guess")
    #V0.1.1 new additions. Video gaming expansion epilogue or whatever you kids say I guess
    print("... \n \n \n Now for some more fun for sure this time!")
    pendingSodomy = str(input("Enter a string to be randomly capitalized here: "))
    stringManipulationForFunIGuess(pendingSodomy)
    return

if __name__ == "__main__":
    main()
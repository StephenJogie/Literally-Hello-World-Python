# Version 0.1.0 of literally just Hello World in Python 3.7
indentLvl = 3

def literallyHelloWorld():
    print("Hello World")

def helloSomeArgument(object):
    print("Hello " + object)

def userInterface():
    print("So, anyways, pick which version of Hello World you want to play I guess: \n")
    print("\t"*indentLvl + "1. Classic Version for the purists")
    print("\t"*indentLvl + "2. Gamer Version for the Gaming Gamers with working keyboards! \n")
    userChoice = int(input("Make your choice (1 or 2): ")) #please enter an actual integer dear god
    return userChoice



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
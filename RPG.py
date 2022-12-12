#Global variabel for våpen. Den vil enten være true eller false, avhengig av om spilleren har funnet den ennå eller ikke. Våpenet kan endre utfallet i noen av rommene.
weapon = False


#Om spilleren har funnet våpenet, så kan de bruke det til å drepe monsteret de møter på her og rømme.
#Om de ikke har våpenet så kan de bare rømme, eller så blir de drept om de velger å slåss.
def darkCreature():
    actions = ["fight","flee"]
    global weapon
    print("A strange, tall, dark figure has appeared. It's walking towards you. You are horrified, but you can either flee or fight for your life. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("The knife you found earlier came in handy. You use it to kill the ghoul. After moving forward, you find an exit and escape.")
                print("Would you like to quit, or retry?")
                print("Options: quit/retry")
                userInput = input()
                if userInput == "quit":
                    quit()
                if userInput == "retry":
                    break
            else:
                print("The ghoul has murdered you.")
                print("Would you like to quit, or retry?")
                print("Options: quit/retry")
                userInput = input()
                if userInput == "quit":
                    quit()
                if userInput == "retry":
                    break
        elif userInput == "flee":
            showBones()
        else:
            print("Please enter a valid option.")

#Dette er et av rommene der spilleren kan finne våpenet. Om spilleren finner det, så blir weapon variabelen satt til true.
#De kan bruke våpenet i det neste rommet om de finner det.
def showBones():
    directions = ["backward","forward"]
    global weapon
    print("The moment you enter this room, you're greeted by a wall of bones. You have this eerie feeling that you can't shake off. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward/forward")
        userInput = input()
        if userInput == "left":
            print("You bump into a wall, and part of it falls apart. You find a knife and bring it with you.")
            weapon = True
        elif userInput == "backward":
            startScene()
        elif userInput == "forward":
            darkCreature()
        else:
            print("Please enter a valid option.")

#Dette er enda et sted der spilleren kan rømme, eller bli drept. Uansett hva skjer så får de igjen et valg om de vil retry eller quit.
def deadRoom():
    directions = ["right","left","backward"]
    print("As soon as you enter the room, you hear whispering. You feel like you've awoken the dead. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            print("As soon as you enter the room, the door behind you closes. You hear growling, and see ghoul-like creatures slowly rising up. They murder you.")
            print("Would you like to quit, or retry?")
            print("Options: quit/retry")
            userInput = input()
            if userInput == "quit":
                quit()
            if userInput == "retry":
                break
        elif userInput == "left":
            print ("You made it! You found an exit.")
            print("Would you like to quit, or retry?")
            print("Options: quit/retry")
            userInput = input()
            if userInput == "quit":
                quit()
            if userInput == "retry":
                break
        elif userInput == "backward":
            startScene()
        else:
            print("Please enter a valid option.")


#Om spilleren valgte å gå right fra forrige scenen, ender de opp her. Dette er ett av stedene de kan finne en utgang.
#Om de når utgangen så får de et valg om å retry, eller quit. De kan også gå backward fra her.
def bagScene():
    directions = ["forward","backward"]
    print("You see a bag on the floor. The contents have been spilled out, and they look fresh. Someone else has been here recently. What would you like to do?")
    userInput =""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            print("You made it! You've found an exit.")
            print("Would you like to quit, or retry?")
            print("Options: quit/retry")
            userInput = input()
            if userInput == "quit":
                quit()
            if userInput == "retry":
                break
        elif userInput == "backward":
            showTallFigure()
        else: print("Please enter a valid option.")

#Om spilleren går backward fra dette rommet, går de tilbake til intro-scenen.
#Om de går left eller right så spilles en ny scene av.
def showTallFigure():
    directions = ["right","backward"]
    print("You see a tall, shadowy figure appear in the distance. You start getting the creeps. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            bagScene()
        elif userInput == "left":
            print("You bump into a wall.")
        elif userInput == "backward":
            startScene()
        else:
            print("Please enter a valid option.")


#startScene() funksjonen. Starter eventyret og gir spilleren et valg om hvor de vil gå videre. Avhengig av hva spilleren velger, så starter en annen scene.
#For eksempel. hvis brukeren skriver "left", så begynner showTallFigure() scenen. 
def startScene():
    directions = ["left","right","forward"]
    print("You are surrounded by trees. Everywhere you look you see trees. You could go any direction. Where would you like to go?")
    userInput =""
    while userInput not in directions:
        print("Options: left/right/backward/forward")
        userInput = input() 
        if userInput == "left":
            showTallFigure()
        elif userInput == "right":
            showBones()
        elif userInput == "forward":
            deadRoom()
        elif userInput == "backward":
            print("You bump into a wall.")
        else:
            print("Please enter a valid option.")

#Startfunksjonen. Gir en velkomst til spilleren så starter den en annen funksjon introScene(). Spilleren kan skrive navnet sitt her.
if __name__ == "__main__":
    while True:
        print("Welcome!")
        print("You're an avid adventurer!")
        print("However, during your adventures, you managed to get yourself lost, and you need to escape.")
        print("Let's start with your name.")
        name = input()
        print("Have fun, " +name+ ".")
        startScene()

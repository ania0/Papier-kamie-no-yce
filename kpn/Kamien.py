from random import randint
 
#create a list of play options
t = ["K", "P", "N"]
 
#assign a random play to the computers
computer = t[randint(0,2)]
 
#set player to False
player = False
 
while player == False:
#set player to True
    player = input("K-Kamień P-Papier N-Nożyce")
    if player == computer:
        print("Remis")
    elif player == "K":
        if computer == "P"
            print("Przegrałeś)
        else:
            print("Wygrałeś")
    elif player == "P":
        if computer == "N":
            print("Przegrałeś")
        else:
            print("Wygrałeś")
    elif player == "N":
        if computer == "K":
            print("Przegrałeś")
        else:
            print("Wygrałeś")
    
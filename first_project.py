#make the rock paper scisor game 
""" we will asign the computer vlaue to pick form since the computer only understands binary numbers we will take 
rock as = 1
paper as = -1
and scisor as = 0
""" 
#here we go now 
import random
bot  = random.choice([-1, 0, 1])
win = 0
loose = 0
draw = 0
youstr = input("ENTER YOUR CHOICE  = ")
youdict = {"r":1,"p":-1,"s":0}
if youstr not in youdict:
    print("acha behen diye lodiye")
else:
    yourchoice = youdict[youstr]
    reversedict = {1:"r",-1:"p",0:"s"}

    print(f"you chose {reversedict[yourchoice]} \ncomputer chose {reversedict[bot]}")
    

    if (bot == yourchoice):
            print("DRAW")
            draw +=1

    else:
        if (bot == 1 and yourchoice == -1):
            print("DAMMMM BROO YOU WON 🥳🥇!!!!!")
            win +=1
        elif(bot == -1 and yourchoice ==0):
            print("DAMMMM BROO YOU WON 🥳🥇!!!!!")
            win +=1
        elif (bot == 0 and yourchoice == 1):
            print("DAMMMM BROO YOU WON 🥳🥇!!!!!")
            win +=1
        elif (bot == 1 and yourchoice == 0):
            print("HAHA LOSER 🫵🏻🤣 !!!")
            loose +=1
        elif (bot == 0 and yourchoice == -1):
            print("HAHA LOSER 🫵🏻🤣 !!!")
            loose +=1
        elif (bot==-1 and yourchoice ==1):
            print("HAHA LOSER 🫵🏻🤣 !!!")
            loose +=1
        else:
             print("KUCH TOH HUG DIYA MENE HE ")

        print(f"Wins: {win} | Losses: {loose} |DRAWS : {draw}")   



'''
SO BABY HERE IS HOW YOU PLAY IT FOR ROCK YOU CHOOSE r AND FOR PAPER YOU CHOOSE p AND FOR SCISSOR YOU CHOOSE s AND THAN BOT WILL 
MAKE HIS CHOICE THAN WE WILL SEE IF YOU WIN OR LOOSE 
'''
        
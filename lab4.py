################
# Lab 4
# Author: Yathoorshan
# Email: s.yathu@hotmail.com
# Student ID: 213216437
# Section A
###############

# you'll need the random module
#import rando
from  random import  randint

### Write your functions below ###
def getCardValue():
    rnum=randint(2,14)
    return rnum


def getCardStr(cardValue):
    cstng=""
    if(cardValue==2):
        cstng="2"
    elif (cardValue==3):
        cstng="3"
    elif (cardValue==4):
        cstng="4"
    elif (cardValue==5):
        cstng="5"
    elif (cardValue==6):
        cstng="6"
    elif (cardValue==7):
        cstng="7"
    elif (cardValue==8):
        cstng="8"
    elif (cardValue==9):
        cstng="9"
    elif (cardValue==10):
        cstng="T"
    elif (cardValue==11):
        cstng="J"
    elif (cardValue==12):
        cstng="Q"
    elif (cardValue==13):
        cstng="K"
    elif (cardValue==14):
        cstng="A"

    return cstng

def getHLGuess():
    buser=""
    while ((buser.upper()!="H") or (buser.upper()!="L" )):
        buser = input("High or Low (H/L)?: ")

        if (buser.upper()=="H"):
            return "HIGH"
        elif (buser.upper()=="L"):
            return "LOW"

def getBetAmount(maximum):
    pts = 0
    while ((pts < 1) or (pts > maximum)):
        pts = input("Input bet amount : ")
        pts=int(pts)
    return pts

def playerGuessCorrect(card1, card2, betType):
    if (card1 > card2 and betType == "LOW") or ((card1 < card2 and betType == "HIGH")):
        return True
    else:
        return False




### Write your main program below ####
msg = """--- Welcome to High-Low ---
Start with 100 points.  Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose. 
Try to make it to 500 points within 10 tries."""
keepplay=True
spoits = 100
cpoints = spoits
cround = 1
print(msg)
while keepplay:


    print("\n")



    print("-----------------------------------------------------------------------------------")
    print("OVERALL POINTS: {} ROUND {}/{}".format(cpoints, cround, 10))

    cardone=getCardValue()
    cardone=getCardStr(cardone)
    print("First card is a [{}]".format(cardone))

    gus=getHLGuess()
    betpoits=getBetAmount(cpoints)


    cardtwo=getCardValue()
    cardtwo=getCardStr(cardtwo)
    print("Second card is a [{}]".format(cardtwo))
    successguess=playerGuessCorrect(cardone,cardtwo,gus)
    if(successguess == True):
        cpoints=cpoints+betpoits
        res="Won"
    else:
        cpoints=cpoints-betpoits
        res="lose"
    print("Card1 [{}] Card2 [{}] - You bet '{}' for {} - YOU {}".format(cardone, cardtwo, gus, betpoits, res))

    if(cpoints>=500):
        print("-----------------------------------------")
        print("YOU MADE IT TO *{}* POINTS IN {} ROUDS !".format(cpoints,cround))
        print("-----------------------------------------")
        keepplay=False
        input("Press enter to exit. ")  # input statement to pause code when finished
    elif (cpoints <=0):
        print("------------------------------------")
        print("YOU HAVE *0* POINTS AFTER {} ROUDS !".format( cround))
        print("------------------------------------")
        keepplay = False
        input("Press enter to exit. ")  # input statement to pause code when finished

    elif(cpoints<=0 or cround==10):
        print("-------------------------------")
        print("ONLY *{}* POINTS IN {} ROUNDS !".format(cpoints, cround))
        print("-------------------------------")
        keepplay=False
        input("Press enter to exit. ")  # input statement to pause code when finished
    else:
        cround=1+cround










1  #########################
# EECS1015 - Lab 5
# Your name -Yathoorshan
# Your student ID-213216437
# Your email-s.yathu@hotmail.com
# Your Section A
#########################

from random import randint
import pyttsx3


def generateRandomList(listsize, maxs):
    avg = 0
    mylist = []
    for i in range(listsize):
        x = randint(1, maxs)
        mylist.append(x)
    print("Generated list")
    print(mylist)
    return mylist


def computeAverage(mylist):
    avg = 0
    val = 0
    for i in range(len(mylist)):
        val = mylist[i]
        avg = avg + val
    avg = float(avg / listsize)
    print("Average value = %.4f" % (avg))


def task1():
    global listsize
    listsize = int(input("Input list size: "))
    maxs = int(input("Input max int: "))
    mylist = generateRandomList(listsize, maxs)
    avg = computeAverage(mylist)


def stringToCharLst(srt):
    mylist = []
    for i in range(len(srt)):
        x = srt[i]
        mylist.append(x)
    print(mylist)
    return mylist


def charsToWord(mylist):
    nlist = []
    notoword = {'0': 'Zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                '8': 'eight', '9': 'nine', '-': 'dash'}
    for i in mylist:
        x = notoword[i]
        nlist.append(x)
    print(nlist)
    separator = "->"
    z = separator.join(nlist)
    print(z)
    return  mylist


def readit(numlist):
    engine=pyttsx3.init()
    engine.say(numlist)
    engine.runAndWait()


def task2():
    global srt

    srt = input("Enter phone number as XXX-XXX-XXXX ")
    srttolist = stringToCharLst(srt)
    numlist = charsToWord(srttolist)

    ans=input("Say word list? (Y/N) :")
    if (ans.upper()=="Y"):
        readit(numlist);


def main():
    print("\n--------- TASK 1: Random List -------------")
    task1()
    print("\n--------- TASK 2: Phone number to text ---")
    task2()

    input("Press enter to exit.")


if __name__ == "__main__":
    main()
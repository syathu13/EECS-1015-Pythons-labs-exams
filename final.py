###########################################
# EECS1015 - Final exam (final.py)
# Name:Yathoorshan
# Student ID:213216437
# Email: s.yathu@hotmail.com
# Section A
###########################################

# import the approriate items from utilities.py and other modules may you require
import random
from utilities import *
#------------------------------task 0-----------------------------------
def task0():
    msg = """
Final Exam - EECS1015
Name: Yathoorshan S
Student ID: 213216437
Email: s.yathu@hotmail.com
Section A
    """

    print(msg)

#------------------------------task 1-----------------------------------
def task1():
    random_num=random.randint(1,3)
    game_list=["","Rock","Paper","Scissors"]

    print("Rock, Paper, Scissors")
    play_again="Y"

    while(play_again=="Y"):
        print("Make your selection. . .")
        user_input=int(input("(1) rock, (2) paper, (3) scissors? "))
        if (user_input==1)or(user_input==2)or(user_input==3):
            print("You: %s" %(game_list[user_input]))
            print("HAL: %s" %(game_list[random_num]))
            printOutcome(game_list[user_input],game_list[random_num])
            play_again = input("Play again (Y/N)? ").upper()
        else:
            print("Invalid selection. Try again")



def printOutcome(user,rand):
    if user == rand:
        print("A Tie!")
    elif user == "Rock":
        if rand == "Scissors":
            print("You Win!")
        else:
            print("HAL wins!")
    elif user == "Paper":
        if rand == "Rock":
            print("You Win!")
        else:
            print("HAL wins!")
    elif user == "Scissors":
        if rand == "Paper":
            print("You Wins!")
        else:
            print("HAL wins!")



#---------------------------task 2 -----------------------------------

def task2():
    input_list=[]
    orig_srt=""
    input_data=input("Input two or more chars separated by spaces:")
    list_len = len(input_data)

    assert list_len >= 2, "Error"
    input_list=input_data.split(" ")
    print("Initial list")
    print(input_list)

    for i in input_data:
        orig_srt+=i.strip()
    print("String version:'%s'"%(orig_srt))
    print("Modified list")
    mod_srt=swapAdjacentElements(input_list)



def swapAdjacentElements(data):
    i=0

    mod_data=""
    if len(data)%2==0:
        list_len=len(data)-1
    else:
        list_len=len(data)-2


    while i< len(data)-1:
        temp=data[i]
        data[i]=data[i+1]
        data[i+1]=temp
        i=i+2
    print(data)
    for i in data:
        mod_data+=i.strip()
    print("String version:'%s'" % (mod_data))



#---------------------------task 3____________________________



def check(infor_list, i):
    for j in infor_list:
        if j == i:
            return True
    return False

def task3():
    res = {}
    stu_year=""
    stu_prgm = ""
    stu_campus=""
    stu_listar=len(students)


    for i in range (stu_listar):

        if check(studentsInfo["CS"], i):
            stu_prgm = "CS"
        elif check(studentsInfo["DM"], i):
            stu_prgm = "DM"
        elif check(studentsInfo["BZ"], i):
            stu_prgm = "BZ"
        elif check(studentsInfo["SE"], i):
            stu_prgm = "SE"

        if check(studentsInfo["Year 1"], i):
            stu_year = "1"
        elif check(studentsInfo["Year 2"], i):
            stu_year = "2"
        elif check(studentsInfo["Year 3"], i):
            stu_year = "3"
        elif check(studentsInfo["Year 4"], i):
            stu_year = "4"

        if  check(studentsInfo["On Campus"], i):
            stu_campus = "On Campus"
        elif check(studentsInfo["Off Campus"], i):
            stu_campus = "Off Campus"


        res[students[i]] = "%10s (year %s) Program: %s Housing: %s"%(students[i], stu_year, stu_prgm,stu_campus)

    for i in sorted(res):
        sort_list=res[i]
        print(sort_list)

#----------------------Task4----------------------------------------------------------------------

def task4():
    input("Press enter to start aquarium.")
    reslt = []

    for i in range(5):
        start_direction = random.randint(0, 1)
        start_pos = random.randint(5, 30)
        reslt.append(SeaLife(start_direction, start_pos))

    current_time_step = 1

    while (current_time_step <= 50):
        print("-" * 40 + "Time: " + str(current_time_step))

        for x in reslt:
            print(x.getStr())
            x.move()

        time.sleep(0.3)
        current_time_step = current_time_step + 1





def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()

    input("Press enter to quit.")


if __name__ == "__main__":
    main()


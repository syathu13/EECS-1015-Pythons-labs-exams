
##############################
# Lab3  --- Starting code (you can cut-and-paste into pycharm)
# Author name: yathoorshan
# Student ID: 213216437
# Email address: s.yathu@hotmail.com
# Section  A
##############################

# Code for task 1 after this line
print("\n--- Task 1 ---: Compute Fare")
print("(1) One way or (2) round trip ? ")
selecton=int(input("Enter 1 or 2 :"))
print("select Age group")
print("(1) under 12")
print("(2) 13-64")
print("(3) 65 or older")
age=int(input("Enter 1 , 2 ,or 3 :"))

far=0
if(selecton==1 ):
    if(age==1 or age==3) :
        far="Total amount due: $0.90 [one way (reduced fare)]"
    else:
        far="Total amount due: $1.80 [one way (full fare)]"
if(selecton==2 ):
    if(age==1 or age==3) :
        far="Total amount due: $1.75 [round trip (reduced far])]"
    else:
        far="Total amount due: $3.50 [round trip (full fare)] "

print(far)



# Code for task 2 after this line
print("\n--- Task 2 ---: Parse string")
msg=input("Input a string : ")
srtl=int(len(msg))
x=0
nmsg=''
while(x!=srtl):
    temp=msg[x]
    if(temp==" "):
            temp=temp.replace(" ","SPACE")
    print("srt[%d] =%s"%(x, temp))
    x = x + 1
    nmsg=temp+nmsg

nmsg=nmsg.replace("SPACE","")
print("Reverse no spaces:",nmsg)



# Code for task 3 after this line
print("\n--- Task 3 ---: The maximum *even* number")
print("Keep entering positive integer ")
print("To quit, input a negative integer")

data1=input("Enter a number :")
data1=int(data1)
enum1=0
temp1=0
while(data1>0):

    if(data1%2==0):
        enum1=data1
    if(enum1>temp1):
        temp1=enum1
    data1 = input("Enter a number :")
    data1 = int(data1)



print("Largest even number:",temp1)



# Code for task 4 after this line
print("\n--- Task 4 ---: Better triangle draw")
num=input("Enter size between 5 and 20:")
num=int(num)

while(num<5 or num>20):
    num=input("Enter size between 5 and 20:")
    num=int(num)


for i in range (num):
    output=""

    for j in range(0,i):
        output=output+"-"
    output = output + "\\"
    print(output)

for i in range (1):
    output=""

    for j in range(num,i,-1):
        output=output+"-"
    output = output + "|"
    print(output)

for i in range (num):
    output=""

    for j in range(num-1,i,-1):
        output=output+"-"
    output = output + "/"
    print(output)



input("Press enter to quit.")
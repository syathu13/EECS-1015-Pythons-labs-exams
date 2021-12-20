################
# Lab 2
# Author: yathoorshan S
# Email: s.yathu@hotmail.com
# Student ID: 213216437
# Section A
###############


print("\n----Task 1---- BMI Calculator")
## Write Task1 code here
name=input("Name : ")
weight=float(input("Weight (Kg) : "))
height=float(input("Height (CM) : "))
name=name.strip().title()



h_in_meters = height /100
BMI = weight/(h_in_meters*h_in_meters)
print("Name : %s Weight : %.2f Height [meter] : %.2f BMI : %.2f"%(name, weight, h_in_meters, BMI))




print("\n----Task 2---- Leetspeak Converter")
## Write Task2 code here
lsrt = input("Type a lonf String :")
lsrt=lsrt.strip().upper()
lsrt=lsrt.replace("T", "+")
lsrt=lsrt.replace("A", "@")
lsrt=lsrt.replace("E", "3")
lsrt=lsrt.replace("I", "|")
lsrt=lsrt.replace("B", "8")
lsrt=lsrt.replace("O", "0")
lsrt=lsrt.replace("C", "[")
lsrt=lsrt.replace("S", "5")

print(lsrt)


print("\n----Task 3---- Flipping String")
## Write Task3 code here

slsrt=input("Input a Long string :")
total_char=len(slsrt)
mid_char=int(total_char/2)
m_srt=slsrt[mid_char]
slsrt=slsrt.upper();

separationindex=slsrt.find(m_srt)
begning_str=slsrt[:mid_char]
end_srt=slsrt[mid_char:]

print("This String is {} characters long. the middle character is '{}'\nFlipped String".format(total_char,m_srt))
print(end_srt+"|"+begning_str)





print("\n----Task 4---- Multiple numbers")
## Write Task4 code here
tsrt=input("Input numbers to multiply :")
tsrt=tsrt.strip()
seprateindex=tsrt.find("*")
first_num_srt=tsrt[:seprateindex].strip()
sec_num_srt=tsrt[seprateindex+1:].strip()
first_number=int(first_num_srt)
sec_number=int(sec_num_srt)
final=first_number*sec_number

print("Extract numbers {} {}".format(first_number, sec_number))
print("{} * {} = {}".format(first_number, sec_number ,final))





input("Press enter to exit. ")  # input statement to pause code when finished
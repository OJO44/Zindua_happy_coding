#Write a python program that allows the user to enter the score of a student and assigns a grade from A to E

Marks = int(input("Enter your marks: "))

if ( Marks >= 80):
    print("A")
elif (Marks >= 60):
    print("B")
elif (Marks >= 50):
    print("C")
elif (Marks >= 40 ):
    print("D")
else :
    print("E")

print(Marks)


#Practice
x = int(input("enter your position: "))
if x >= 5 and x  < 10:
    print("within range")
elif x < 5:
    print("smaller")
else:
    print("not in the category")

print(x)




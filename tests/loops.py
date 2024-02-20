#Create a program that checks a name from a list of names
names = ["Jones", "Phil", "Dimore", "Delilah"]

user = "Jose"

for name in names:
    if name == user:
        print("Name Found")

start = 2
end = 25


for number in range (5,10):
    if number %2== 0:
        print(f"{number} is even!")


#Write a python program using a for loop that prints multiples of 3
count = 0
sum = 0
print( "Before", count, sum)
for value in range (10,20):
    count= count + 1
    sum = sum + value
    print(count, sum, value)
    print("After", sum, count, sum/count)


found = True
print("before", True)
for value in [1,3,5,6,9,10]:
    if value >= 5:
       found = False
    print(value, found)
print("After", found)

#lists
staff = []
print(staff)
staff.append("CIO")
staff.append("Manager")
staff.append("Developer")
staff.append("busines analyst")
print(staff)
staff= staff.sort()
staff= staff.split()
print(staff)

#Build a human versus computer rock paper and scissor game
#rock beats scissior
#scissor beats paper
#paper beats rock

import random:

comp_score = 0
human_score = 0
tie_score = 0

choices = ["rock", "paper", "scissors"]
while true:

def winner(human, computer):
    if human == "rock" and computer ==  "paper":
        print ("human lost")
        return "computer"
    elif human =="rock" and computer == "scissors":
        print ("human win")
        return "human"
    elif human =="scissors" and computer == "paper":
        print ("Human lost")
        return "computer"
    else:
        print("its a tie")

#Validate input
while True:
    human = input( "\n choose. Rock, Paper, or Scissors: ")
    if human == " Rock" or human == "Paper" or human = "Scissors" :
        break
    else:
        print("Try again.")

#Generate computer pick
computer = random.choice(choices)

#print results
print ("human hand:", human)
print("comp hand:", computer)
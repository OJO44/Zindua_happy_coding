#declaring a function
def greetings (name) :
    if (name == "John"):
         print("I hate John")
         
    elif (name == "Paul"):
        print ("Paul is great dude")

    elif (name == "Ivy"):
        print (" I am not sure about my feeling")

    else(name != "John", "Paul", "Ivy"):
        print("I have never met the person")

def sum(num1, num2):
    return (num1 + num2)
    
num1 = int(input("Enter the the first number: "))
num2 = int(input("Enter the the second number: "))
    print(sum(num1, num2))



    name = input("Enter a name: ")

    #calling a function
    greetings(name)
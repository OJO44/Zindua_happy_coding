#Write a python code program that calculate sales profit of a business
def profit_earned():
    Sp = float(input("Enter selling price: "))
    Cp = float(input("Enter cost price: "))
    Profit = Sp - Cp
    return Profit

Profit = profit_earned()
print(f"Profit earned is {Profit}")

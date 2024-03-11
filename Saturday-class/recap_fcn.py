#write a function that calculates the total phone bill in a month
def monthly_phone_bill():
    daily_bill = float(input("Enter daily bill amount: "))
    days = int(input("Enter days of the month: "))
    total_phone_bill = days * daily_bill
    return total_phone_bill

total_bill = monthly_phone_bill()
print(total_bill)
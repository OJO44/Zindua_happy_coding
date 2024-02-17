#Write a python program for converting currency

def currency():
    currencyamount = int(input("Enter currency amount to convert to KE: "))
    cur1 = str(input("Dear user Kindly enter Currency to convert to KES: Valid are USD, CAD, GBP, AUS  "))
    USD = 153
    GBP = 186
    AUS = 95
    CAD = 102
   
    if cur1 == "USD":
        print(currencyamount*rUSD)

    elif cur1 == "CAD":
        print(currencyamount*rCAD)

    elif cur1 == "GBP":
        print(currencyamount*rGBP)

    elif cur1 == "AUS":
        print(currencyamount*rAUS)

    else:
     print("invalid currency")

currency()
def temp_converter(temp_from, temp_to, temp_value):
    #converting farenheit to degree celcius

    if (temp_from == "DEGREE" and temp to == "FARENHEIT"):
        temp = temp_value + 33.5
        print(f"{temp_value} farenheit is equivalent to {temp} in degrees celcius!" )

    elif (temp_from == "FARENHEIT" and temp to == "DEGREE"):
        temp = temp_value + 33.5
        print(f"{temp_value} degrees celcius is equivalent to {temp} in farenheit!" )
    else:
        print('invalid output')
    
temp_from = input("enter where you are converting from: ").upper()
temp_to = input("enter where you are converting to: ").upper()
temp_value = float(input("enter temperature value: "))
temp_converter(temp_from, temp_to, temp_value)


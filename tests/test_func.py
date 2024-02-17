def temp_converter(temp):
    converted = temp - 33.5
    print(f"{temp} degrees celcius is {converted} Farenheit")

def assess(temp):
    if temp > 38 and temp < 42:
        print('Please take some medication')
    else:
        print('You look good buddy')

def main(temp):
    temp = float(temp)
    temp_converter(temp)
    assess(temp)

temp_input = input("Enter temperature in celcius:")
main(temp_input)

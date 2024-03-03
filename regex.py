import re

# Define a regex pattern for a phone number (+254 234 098 134)
#text = "Mentors phone number 254-234-098-134"
#pattern = r"\+\d{3}\s\d{3}\s\d{3}\s\d{3}" 

#result = re.search(pattern, text)
#print(result)

#Practice regular expressions


#new_text = "ABC 123 XYZ 456 &$! 100"

# Creating a pattern using a raw string
#pattern = re.compile(r"\d{3}")  # Match exactly 3 digits. 

# Finding all matches using finditer
#matches = pattern.finditer(new_text)

#for match in matches:
    #print(match.group())




message = ''' hi , today is 23-Feb-2024, yesterday was 22-Feb-2024 and tomorrow will be 23-Feb-2024.
My schedule is free on 26-February-2024, 27.02.2024 and 30/Jun/2024
You can reach me okumu99@gmail.com or support_@demo.net & conference@practice.co.ke.
You can also call me at one ofthe following lines +2547- 111 3339, +2525.555 6767, 017-7778800 '''

#email_pattern = re.compile(r"\w+@[a-zA-Z0-9.-]+\.[a-z]{2,3}")

#matches = email_pattern.finditer(message)

#for match in matches:
#   print(match.group())

# import re

# greeting = "Hi, how are you?"
# pattern = re.compile(r"^(Hi).*\?$")

# matches = pattern.finditer(greeting)

# for match in matches:
#     print(match.group(0))

#The regular expression pattern r"^(Hi).*\?$" is used to match a greeting that starts with "Hi" and ends with a question mark.
#The ^ anchor ensures that the pattern matches "Hi" at the beginning of the string.
#The .* matches any characters in between "Hi" and the question mark.
#The \? specifically matches the question mark at the end of the string.
#In the print statement, match.group(0) is used to print the entire matched string
    
#Here's the significance of using 0 after group():
#
#group(0): This returns the entire matched string (the whole pattern match).
#group(1): This would return the first captured group within parentheses (Hi) in this case.
#If your pattern had more capturing groups (Hi)(, how), you could access them using group(1) and group(2) respectively.


import re

queries = """reach us out on yusuf89@gmail.com and obunga254@kenya.com. call us on (+254) 786-3567 or (+234) 222-5445"""

# Write a function called extract_phone_numbers(string) that takes in a string and returns a list of all the phone numbers present in the string in the format (XXX) XXX-XXXX

def extract_phone_numbers(string):
    extract_phone_number = re.compile(r"\(\+\d{3}?\)\s\d{3}-\d{4}")
    return extract_phone_number.findall(string)

phone_numbers = extract_phone_numbers(queries)

for number in phone_numbers:
    print(number)
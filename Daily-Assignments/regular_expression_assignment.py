import re

queries = """reach us out on yusuf89@gmail.com and obunga254@kenya.com. 
Call us on  (254) 786-3567 or (+234) 222-5445"""

def extract_phone_numbers(string):
    phone_number_pattern = r"\(?\d{3}\) \d{3}-\d{4}"
    phone_numbers = re.findall(phone_number_pattern, string)
    return phone_numbers

phone_numbers = extract_phone_numbers(queries)

for number in phone_numbers:
    print(number)


#Write a function called extract_email_addresses(string) that takes in a string and returns a list of all the email addresses present in the string.
def extract_email_addresses(string):
    email_address_pattern =  r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{3}"
    email_addresses = re.findall(email_address_pattern, string)
    return email_addresses

email_addresses = extract_email_addresses(queries)

for address in email_addresses:
    print(address)



import re

# Define the pattern for the phone number
pattern = r"\(\+254\)[\s.-]?\d{3}[\s.-]?\d{4}"

# Text containing phone numbers
sentence = "define a regex pattern for the phone number (+254) 098 1134, (+254) .098. 1234, (+254) -098-5134"

# Search for phone numbers in the text using the pattern
result = re.search(pattern, sentence)

# Print the result
if result:
    print(result.group())

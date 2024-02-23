import re

queries = """reach us out on yusuf89@gmail.com and obunga254@kenya.com. 
Call us on  (254) 786-3567 or (+234) 222-5445"""

# 1. Write a function called extract_phone_numbers(string) that takes in a string and returns a list of all the phone numbers present in the string in the format (XXX) XXX-XXXX
def extract_phone_numbers(string):
    phone_number_pattern = r"\(?\d{3}\) \d{3}-\d{4}"
    phone_numbers = re.findall(phone_number_pattern, string)
    return phone_numbers

phone_numbers = extract_phone_numbers(queries)

for number in phone_numbers:
    print(number)


#2. Write a function called extract_email_addresses(string) that takes in a string and returns a list of all the email addresses present in the string.
def extract_email_addresses(string):
    email_address_pattern =  r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{3}"
    email_addresses = re.findall(email_address_pattern, string)
    return email_addresses

email_addresses = extract_email_addresses(queries)

for address in email_addresses:
    print(address)

#3. Write a function called replace_email_addresses(string, replacement) that takes in a string and a replacement string, and replaces all email addresses in the given string with the replacement string.
    
def replace_email_addresses(string, replacement):
    email_address_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}"
    replaced_string = re.sub(email_address_pattern, replacement, string)
    return replaced_string

new_queries = replace_email_addresses(queries, "zakarimachara1@jbkenya.com")

print(new_queries)


#Write a program that uses input to prompt a user for their name and then welcomes them.
name = input(" Please enter your name: ")
print("Welcome " + name)

#Write a program to prompt the user for hours and rate per hour to compute gross pay. H=35, R=2.75,Pay=96.2
Pay= int(input( "Enter your pay: /n "))
Hours = float(input("Enter hours: "))
Rate = float(input( "Enter rate:"))
Gross_pay = Hours * Rate 

return Gross_pay



#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.




#1. `def replace_email_addresses(string, replacement):`
   -# This line defines a function named `replace_email_addresses` that takes two parameters: `string` and `replacement`.

#2. `email_address_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}"`
 #  - This line creates a regular expression pattern that matches email addresses. The pattern `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2}` is used to match email addresses in the format of `username@domain.com`.

#3. `replaced_string = re.sub(email_address_pattern, replacement, string)`
   #- This line uses the `re` module's `sub` function to substitute all occurrences of the email addresses in the input `string` with the `replacement` provided. The `re.sub()` function takes the regular expression pattern, the replacement string, and the input string as arguments.

#4. `return replaced_string`
 #  - This line returns the modified string with email addresses replaced.

#5. `new_queries = replace_email_addresses(queries, "zakarimachara1@jbkenya.com")`
 #  - This line calls the `replace_email_addresses` function with two arguments: `queries` (presumably a string containing text with email addresses) and `"zakarimachara1@jbkenya.com"` as the replacement for email addresses.

#6. `print(new_queries)`
 #  - Finally, this line prints the modified string `new_queries`, which is the original input string with all email addresses replaced by the specified replacement email address `"zakarimachara1@jbkenya.com"`.

#In summary, this code defines a function that replaces email addresses in a given string with a specified replacement email address and then demonstrates this functionality by replacing email addresses in the `queries` string and printing the modified result.
import requests
from bs4 import BeautifulSoup

url = "https://www.jumia.co.ke/flash-sales/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


# 1.Getting  Product names
names = soup.find_all("div", class_="name")

formatted_names = []

for name in names:
    #Extract the text content using the .text method
    text_content = name.text.strip()

    # Optionally, remove any extra whitespace or characters
    text_content = text_content.replace("\n", " ")  # Remove newlines
    text_content = text_content.replace("\t", " ")  # Remove tabs

    formatted_names.append(text_content)

print(formatted_names)

#2. Getting brand names
brands = soup.find_all("h3", class_="name")

formatted_brands = []

for brand in brands:
    # Extract the text content using the .text method
    text_content = brand.text.strip()

    # Optionally, remove any extra whitespace or characters
    text_content = text_content.replace("\n", " ")  # Remove newlines
    text_content = text_content.replace("\t", " ")  # Remove tabs

    formatted_brands.append(text_content)



   
# 3. Getting prices
prices = soup.find_all("div", class_="prc" )

formatted_prices = []

for price in prices:
    #Extract the text content using the .text method
    text_content = price.text.strip()

    # Optionally, remove any extra whitespace or characters
    text_content = text_content.replace("\n", " ")  # Remove newlines
    text_content = text_content.replace("\t", " ")  # Remove tabs

    formatted_prices.append(text_content)

# print(formatted_prices)
    
#4. getting discounts
discounts = soup.find_all("div", class_="bdg _dsct" )

formatted_discounts = []

for discount in discounts:
    # Extract the text content using the .text method
    text_content = discount.text.strip()

    # Optionally, remove any extra whitespace or characters
    text_content = text_content.replace("\n", " ")  # Remove newlines
    text_content = text_content.replace("\t", " ")  # Remove tabs

    formatted_discounts.append(text_content)


#5 and 6 .Getting  total number of reviews and product ratings
Reviews = soup.find_all("div", class_="rev" )

formatted_Reviews = []

for review in Reviews:
    # Extract the text content using the .text method
    text_content = review.text.strip()

    # Optionally, remove any extra whitespace or characters
    text_content = text_content.replace("\n", " ")  # Remove newlines
    text_content = text_content.replace("\t", " ")  # Remove tabs

    formatted_Reviews.append(text_content)
   
print(formatted_Reviews)
# #6. product ratings
# Ratings = soup.find_all("div", class_="stars _m _al" )

# formatted_ratings = []

# for rating in Ratings:
#     # Extract the text content using the .text method
#     text_content = rating.text.strip()

#     # Optionally, remove any extra whitespace or characters
#     text_content = text_content.replace("\n", " ")  # Remove newlines
#     text_content = text_content.replace("\t", " ")  # Remove tabs

#     formatted_ratings.append(text_content)

# 7 getting remaining unit left
unit_left = soup.find_all("div", class_="stk" )

formatted_unit_left = []

for unit in unit_left:
    # Extract the text content using the .text method
    text_content = unit.text.strip()

    # Optionally, remove any extra whitespace or characters
    text_content = text_content.replace("\n", " ")  # Remove newlines
    text_content = text_content.replace("\t", " ")  # Remove tabs

    formatted_unit_left.append(text_content)



# iterate through the list at once, consider using zip.
for name,brand,  price, discount, review, unit in zip(formatted_names, formatted_brands, formatted_prices,formatted_discounts,formatted_Reviews, formatted_unit_left,):
    print(f"Items: {name}, Brand: {brand}, Price: {price}, Discount : {discount}, Review: {review}, Units: {unit}, "'\n')

# #prices = soup.find_all("div", class_= "prc" )
# #print(prices)
# #units_left= soup.find_all("div", class_= "stk" )
# #print(units_left)


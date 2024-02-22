#Create a list of dictionaries with products and their highest prices
tech_roles = [
    {"role": "software engineer", "price": 2000},
    {"role": "business_analyst", "price": 1800},
    {"role": "product manager", "price": 2500},
    {"role": "project manager", "price": 1500},
    {"role": "data engineer", "price": 3000}
]

# write a code that Determine the highest paid tech_roles.
max_price = 0
highest_paid_role = " "

for role in tech_roles:
    if role["price"] > max_price:
        max_price = role["price"]
        highest_paid_role = role["role"]

print(f"The highest paid role is '{highest_paid_role}' with a salary of ${max_price}.")
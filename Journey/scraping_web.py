import requests
from bs4 import BeautifulSoup

response = requests.get ("https://www.centralbank.go.ke/rates/forex-exchange-rates/")

#print(response.status_code)

print(response.content)

soup = BeautifulSoup(response.text, "html.parser")
print(soup)

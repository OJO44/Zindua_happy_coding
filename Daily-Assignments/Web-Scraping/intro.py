import requests

response = requests.get ("https://www.centralbank.go.ke/rates/forex-exchange-rates/")

#print(response.status_code)

print(response.content)

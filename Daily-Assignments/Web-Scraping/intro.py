import requests
from bs4 import BeautifulSoup


url = "https://hojaleaks.com/python"
response = requests.get(url)
#print(response.status_code)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)
#scrape https://hojaleaks.com/python and get title/ heading of the first 3 articles
articles = soup.find_all("h1")

for article in articles:
    print(article.text)

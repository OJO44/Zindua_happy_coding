import requests
from bs4 import BeautifulSoup
import csv

url ="https://www.nytimes.com/"
response= requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")  #This line of code creates a BeautifulSoup object called soup by parsing the HTML content of the webpage obtained from the response object using the "html.parser" parser.
                                                     #response.text contains the HTML content of the webpage that was fetched using the requests.get(url) method.

articles = soup.find_all("div", class_= "xdandi" )  #In web scraping, the class attribute can be used to identify specific elements on a webpage that share the same class name.

data = []

for article in articles[:10]:
    title = article.find('h2').get_text()
    description = article.find('p').get_text()
    data.append([title, description])
print(articles)
#  #Refer to file handling.
# with open('nytimes.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['title', 'description'])
#     writer.writeheader()
#     writer.writerows(data)

    
# print('Data has been scraped and stored in nytimes_articles.csv')

#In the context of web scraping using BeautifulSoup in Python, the `.get_text()` method is used to extract the textual content (text) of a BeautifulSoup element. Here's an explanation of how it works in the provided loop:

#1. **`article.find('h2')`**: This line finds the first `<h2>` tag within the `article` element. The `find()` method in BeautifulSoup is used to locate the first tag that matches the specified criteria.

#2. **`.get_text()`**: Once the `<h2>` tag is found, the `.get_text()` method is called on that tag. This method retrieves the text content enclosed within the `<h2>` tag, stripping any HTML tags and returning only the text content.

#3. **`title = article.find('h2').get_text()`**: This line extracts the text content of the `<h2>` tag found within the current `article` element and assigns it to the variable `title`.

#4. **`article.find('p')`**: Similarly, this line finds the first `<p>` tag within the `article` element.

#5. **`description = article.find('p').get_text()`**: It then uses `.get_text()` on the `<p>` tag to extract the text content within the `<p>` tag and assigns it to the variable `description`.

#6. **`data.append([title, description])`**: Finally, the extracted `title` and `description` are appended as a list `[title, description]` to the `data` list, which likely stores information about multiple articles.

#By using `.get_text()`, you extract only the textual content within the specified HTML tags (`<h2>` and `<p>` in this case) without any HTML markup, making it easier to work with and manipulate the extracted text data.

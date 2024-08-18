# First, you will have to import the requests and BeautifulSoup library, which will allow Python to be able to send requests using a link and interact with the DOM. The DOM stands for the Document Object Model and is how a web page is constructed. It's not terribly important that you know how web pages are made for this lesson.
import requests
from bs4 import BeautifulSoup

# We first have to access the webpage using a GET request. A GET request is how a computer asks for access to a website through the Internet. To send the request, you will need the link to the website you want to send the request to.
# The link below will take you to a book store page. Using request.get(), you are able to grab the data from the web page.
data = requests.get("http://books.toscrape.com/")

# Once you have sent the request and saved the data that was sent back, to extract the content or data from the information, you will need to use .content . From there, we add it inside BeautifulSoup.

data_scraping = BeautifulSoup(data.content, "html.parser")

# Next, we will use a method called select(). When people make websites, they often have to put identifiers on page elements called selectors. This is meant for styling the webpage and making it pretty, but we can use selectors to identify elements as well. This method provides full support for CSS selectors, allowing you to select elements in an HTML document (again, if you don't know what CSS or HTML is, it's not that important).

# Because we're asking for specific tags, the way that we scrape or get data from a web page will vary from website to website. We are going to retrieve the book titles from a web page. How this website does it is that the titles are located within anchor tags, which are themselves nested inside h3 tags. To do advanced selecting, you will need >to select the child of a tag.

para = data_scraping.select("h3 > a")

for para_text in para:
  print(para_text.text)

print()
print()
####################################################
# Now let's try scraping for book price. The book price contains a class name price_color. We will need to use .to select class in css. Here it the complete code in order to grab prices on the web page.
import requests
from bs4 import BeautifulSoup

# Make a get requests
data = requests.get("http://books.toscrape.com/")

# Add content
data_scraping = BeautifulSoup(data.content, "html.parser")

# Select elements with class price_color
price_data = data_scraping.select(".price_color")

# Loop through all the data
for price in price_data:
  print(price.text)


#####################################
# This example will now show you how to use sentiment analysis using the library textblob.

from textblob import TextBlob

# The next step we want to do is to create our TextBlob object that will be taking in our string and saving it as a variable
text = TextBlob("Python is a high-level, general-purpose programming language.") # THIS SENTENCE IS NEUTRAL

# Once we have that finished, we can use the method sentiment.polarity to be able to perform sentiment analysis on the text.
# THIS WILL PRODUCT A NEUTRAL SCORE OF 0.0
print(text.sentiment.polarity)
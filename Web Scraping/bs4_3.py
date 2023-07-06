from bs4 import BeautifulSoup
#import requests library
import requests
#the website URL
url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")
heading = doc.find(class_ = "firstHeading")
print(heading)
print(heading.text)
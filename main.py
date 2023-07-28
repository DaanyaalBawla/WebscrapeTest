import requests
from bs4 import BeautifulSoup
#r = requests.get("https://www.google.com/search?client=firefox-b-1-d&q=4chan")
#soup = BeautifulSoup(r.text, "html.parser")
#headers = soup.find_all("h3")
#print(headers)
#for info in headers:
#    print(info.getText())
#    print("------")

city = input("Pick a place where you want to know the weather")
r2 = requests.get("https://www.google.com/search?q=weather+in+"+city)
soup2 = BeautifulSoup(r2.text, "html5lib")
weather = soup2.find('div', class_="BNeawe").text
print(weather)


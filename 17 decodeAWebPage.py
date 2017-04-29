"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

Used python3 and 2to3 on BeautifulSoup
"""
import requests
from bs4 import BeautifulSoup

base_url = "https://www.nytimes.com/"
r = requests.get(base_url)

soup = BeautifulSoup(r.text)

headings = soup.find_all(class_="story-heading")

for heading in headings: 
    if heading.a: 
        print(heading.a.text.replace("\n", " ").strip())
    else: 
        print(heading.contents[0].strip())
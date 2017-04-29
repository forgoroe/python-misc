"""
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article 
on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. 
Your task is to print out the text to the screen so that you can read the full article without 
having to click any buttons.

!!!!!!! Changed objective: Above exercise points to a no longer multiple page article, but a single page one.
		Decided to extract text and links from another website and print contents of those links instead.
"""

import requests
from bs4 import BeautifulSoup

def startSoupOn(urlToScrape):
	base_url = urlToScrape
	r = requests.get(base_url)

	soup = BeautifulSoup(r.text, 'html.parser')
	return soup

def createHrefCollection(listOfLinks):
	hrefDetails = []
	counter = 0 #will be used as id

	for item in listOfLinks:
		href = item.get('href')
		text = item.get_text()

		if href is not None and href.startswith('http'):
			hrefDetails.append({
				'id': counter,
				'href': href,
				'text': text
			})
			counter+=1

	return hrefDetails

if __name__ == '__main__':

	soup = startSoupOn("http://jamesclear.com/creativity")
	
	div = soup.find(class_='entry-content')
	paragraphs = div.find_all('p')
	links = div.find_all('a')

	pContentList = [p.get_text() for p in paragraphs]
	linkDetails = createHrefCollection(links)

	for detail in linkDetails:
		print('id :', detail['id'],' href:', detail['href'],' text:', detail['text'])
		print('\n')
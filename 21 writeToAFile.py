"""
Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, use the code from the solution), 
and instead of printing the results to a screen, write the results to a txt file. 
In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
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

def writeToFile(stringParam, fileName):
	with open(fileName+'.txt', 'w') as open_file:
		open_file.write(stringParam)
		print('String was written to {0}.txt'.format(fileName))



if __name__ == '__main__':

	soup = startSoupOn("http://jamesclear.com/creativity")
	
	div = soup.find(class_='entry-content')
	paragraphs = div.find_all('p')
	links = div.find_all('a')

	pContentList = [p.get_text() for p in paragraphs]
	linkDetails = createHrefCollection(links)

	pForFile = '\n\n'.join(pContentList)
	contentFileName = input('Enter the .txt file name you want to use (without extension) for the paragraph list of the page "{0}": '.format(soup.title.get_text()))
	writeToFile(pForFile,contentFileName)
	
	linksForFile = ''
	for detail in linkDetails:
 		linksForFile += 'ID: {0} HREF: {1} TEXT: {2} \n\n'.format(detail['id'], detail['href'], detail['text'])

	linksFileName = input('Enter the .txt file name you want to use (without extension) for your list of links: ')
	writeToFile(linksForFile, linksFileName)
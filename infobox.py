import wikia
import urllib
import urllib.request
import re
import string
import csv
from bs4 import BeautifulSoup

def findCharacter(name):

	try:
		page = wikia.page("marvel", name)
	except:
		print("The character you are looking for is does not exist in the Earth-616 universe")
		exit()
	currentUrl = page.url;
	currentUrl = currentUrl.replace(" ", "_")
	tempSoup = BeautifulSoup(urllib.request.urlopen(currentUrl),"html.parser")
	wiki = ""
	for soupLine in tempSoup('div',{'id': 'mw-content-text'}):
		character = soupLine.find_all("a")
		for index in range(1,len(character)):
			wiki = character[index]["href"]
			break;

	newUrl = "http://marvel.wikia.com" + wiki
	testUrl = wiki.replace('/wiki/','')
	for header in tempSoup('div', {'class' : 'header-column header-title'}):
		redirect = header.find_all("h2")
	if(len(redirect) == 0):
		if 'Earth-616' not in testUrl:
			if 'Earth' in testUrl:
				print("The character you are looking for is from a different dimension")
				exit()
			return findCharacter(testUrl)
		else:
			return newUrl
	else:
		return newUrl;

def createAliasRelation(newUrl,name):
	outputName = 'alias.csv'
	outputFile = open(outputName,"w+",newline='')
	dataWriter = csv.writer(outputFile)
	soup = BeautifulSoup(urllib.request.urlopen(newUrl).read(),"html.parser")
	columnNames = []
	information = []

	for headline in soup('div', {'class' : 'conjoined-infoboxes'}):
	    character = headline.find_all("h3", class_="pi-data-label pi-secondary-font");
	    links = headline.find_all("div", class_="pi-data-value pi-font")
	    for index, infoNames in enumerate(character):
	    	if(infoNames.text.strip() == "Aliases" or infoNames.text.strip() == "Current Alias" or infoNames.text.strip() == "Real Name"):
	    		temp = []
	    		for individual in links[index].text.split(','):
	    			output = re.sub('\[.*\]', '', individual)
	    			output = output.replace("\"",'');
	    			if(output != ""):
	    				temp.append(output)
	    		information.append(temp)
	    		for aliases in temp:
	    			dataWriter.writerow([name,aliases])
	outputFile.close()

if __name__ == "__main__":
	name = input("Input Heros name: ").strip();
	charUrl = findCharacter(name);
	print(charUrl);
	createAliasRelation(charUrl,name)
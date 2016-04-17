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
		print("The character you are looking for is does not exist in the Earth-616 universe ", name)
		return 0

	currentUrl = page.url;
	#print(currentUrl);
	currentUrl = currentUrl.replace(" ", "_")
	tempSoup = BeautifulSoup(urllib.request.urlopen(currentUrl),"html.parser")
	wiki = ""
	if(len(tempSoup('div', {'id' : 'messageBox'})) > 0):
		for soupLine in tempSoup('div',{'id': 'mw-content-text'}):
			character = soupLine.find_all("a")
			newUrl = "http://marvel.wikia.com" + character[1]["href"]
			testUrl = character[1]["href"].replace('/wiki/','')
			break
	elif(len(tempSoup('div', {'class' : 'conjoined-infoboxes'})) == 0 and len(tempSoup('div', {'class' : 'infobox'})) == 0):
		for soupLine in tempSoup('div',{'id': 'mw-content-text'}):
			character = soupLine.find_all("a")
			for index in range(0,len(character)):
				try:
					print("Title: ",character[index]["title"])
					#if('Earth-616' in character[index]["title"]):
					wiki = character[index]["href"]
					print(wiki)
					break
				except:
					print("Key Error")
					pass
		newUrl = "http://marvel.wikia.com" + wiki
		testUrl = wiki.replace('/wiki/','')
	else:
		newUrl = currentUrl
		testUrl = newUrl.replace('http://marvel.wikia.com/wiki/','') 
	if(len(tempSoup('div', {'class' : 'conjoined-infoboxes'})) == 0 and len(tempSoup('div', {'class' : 'infobox'})) == 0):
		#print("recurse")
		if 'Earth-616' not in testUrl:
			if 'Earth' in testUrl:
				print("The character you are looking for is from a different dimension", name)
				return 0
			return findCharacter(testUrl)
		else:
			return newUrl
	else:
		#print("redirect")
		return newUrl;

def createAliasRelation(newUrl,name,Charid):
	outputName = 'alias.csv'
	outputFile = open(outputName,"a",newline='')
	dataWriter = csv.writer(outputFile)
	soup = BeautifulSoup(urllib.request.urlopen(newUrl).read(),"html.parser")
	columnNames = []
	information = []

	for headline in soup('div', {'class' : 'conjoined-infoboxes'}):
	    character = headline.find_all("h3", class_="pi-data-label pi-secondary-font");
	    links = headline.find_all("div", class_="pi-data-value pi-font")
	    for index, infoNames in enumerate(character):
	    	if(infoNames.text.strip() == "Real Name"):
	    		temp = []
	    		for individual in links[index].text.split(','):
	    			output = re.sub('\[.*\]', '', individual)
	    			output = output.replace("\"",'');
	    			if(output != ""):
	    				temp.append(output)
	    		information.append(temp)
	    		for aliases in temp:
	    			dataWriter.writerow([Charid,name,aliases])
	outputFile.close()

def findIndividual():
	fileName = input("Input Heros File: ").strip()
	charUrl = findCharacter(fileName)
	print(charUrl)
	if(charUrl != 0):
		createAliasRelation(charUrl,fileName,0)

if __name__ == "__main__":
	#fileName = input("Input Heros File: ").strip();
	csvfile = open("character.csv", newline='',encoding='utf-8')
	csvReader = csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in csvReader:
		charUrl = findCharacter(row[1]);
		print(charUrl);
		if(charUrl != 0):
			createAliasRelation(charUrl,row[1],row[0])
	#findIndividual();
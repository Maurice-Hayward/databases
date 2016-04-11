import csv
import re

def characterParser(fileName):
	_digits = re.compile('\d')
	bannedWords = ['Earth','Game','Deadpool','Ultimate','Lego','Age of Apocalypse','House of M','HAS','X-Men: Battle of the Atom','Marvel','MAA']
	relevantCharacters = []
	csvfile = open(fileName, newline='',encoding='utf-8')
	csvReader = csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in csvReader:
		if('(' in row[1]):
			print(row[1])
			if any(word in row[1] or bool(_digits.search(row[1])) for word in bannedWords):
				print("Removed: ",row[0],row[1])
			else:
				relevantCharacters.append([row[0],row[1]]);
		else:
			relevantCharacters.append([row[0],row[1].replace("\"",'')]);
	csvfile.close();
	#print(relevantCharacters)
	newcsvFile = open(fileName,"w+",newline='',encoding='utf-8')
	newcsvWriter = csv.writer(newcsvFile)
	for character in relevantCharacters:
		newcsvWriter.writerow(character)
	newcsvFile.close();
if __name__ == "__main__":
	characterParser("character.csv")

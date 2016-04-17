import csv
import re

def characterParser(fileName):
	_digits = re.compile('\d')
	bannedWords = ['Earth','Game','Deadpool','Ultimate','Lego','Age of Apocalypse','House of M','HAS','X-Men: Battle of the Atom','Marvel','MAA']
	relevantCharacters = []
	csvfile = open(fileName, newline='',encoding='utf-8')
	csvReader = csv.reader(csvfile,delimiter=',',quotechar='|')
	for row in csvReader:
		if('(' in row[0]):
			if any(word in row[0] or bool(_digits.search(row[0])) for word in bannedWords):
				if("Earth-616" not in row[0]):
					print("Removed: ",row[0],row[1])
				else:
					relevantCharacters.append([row[0],row[1]]);
			else:
				relevantCharacters.append([row[0],row[1]]);
		else:
			relevantCharacters.append([row[0].replace("\"",''),row[1].replace("\"",'')]);
	csvfile.close();
	#print(relevantCharacters)
	newcsvFile = open(fileName,"w+",newline='',encoding='utf-8')
	newcsvWriter = csv.writer(newcsvFile)
	for character in relevantCharacters:
		newcsvWriter.writerow(character)
	newcsvFile.close();

def useRealNames(fileName):
	csvfile = open(fileName, newline='',encoding='utf-8')
	csvReader = csv.reader(csvfile,delimiter=',',quotechar='|')
	relevantCharacters = []
	for row in csvReader:
		if('(' in row[1]):
			m = row[1].split('(', 1)[1].split(')')[0]
			print(m)
			relevantCharacters.append([row[0],m])
		else:
			relevantCharacters.append([row[0],row[1]]);
	csvfile.close();
	#print(relevantCharacters)
	newcsvFile = open(fileName,"w+",newline='',encoding='utf-8')
	newcsvWriter = csv.writer(newcsvFile)
	for character in relevantCharacters:
		newcsvWriter.writerow(character)
	newcsvFile.close();

if __name__ == "__main__":
	#characterParser("powers.csv")
	useRealNames("character.csv")

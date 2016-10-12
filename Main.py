gedcomFile = open('GregoryGoldshtenp01.ged', 'r')
writeFile = open('outputFile.ged', 'w')

levelTags = [['0', 'INDI'],['1', 'NAME'],['1', 'SEX'],['1', 'BIRT'],['1', 'DEAT'],['1', 'FAMC'],['1', 'FAMS'],['0', 'FAM'],['1', 'MARR'],['1', 'HUSB'],['1', 'WIFE'],['1', 'CHIL'],['1', 'DIV'],['2', 'DATE'],['0', 'HEAD'],['0', 'TRLR'],['0', 'NOTE']]

def checkValidTag(s, tags):
	s = s.split(' ')
	if len(s) < 2:
		return False
	elif len(s) == 2:
		s[1] = s[1][:-1]
	for i in range(17):
		if(s[0] == tags[i][0] and s[1] == tags[i][1]):
			return True
	return False

def writeInfo(f, s, tags):
	if checkValidTag(s, tags):
		s = s.split(' ')
		#print("Level: " + s[0])
		#print("Tag Name: " + s[1])
		f.write("Level: " + s[0] + "\n")
		if(len(s) == 2):
			f.write("Tag Name: " + s[1])
		else:
			#print("Tag Info: " + "".join(s[2:])[:-1])
			f.write("Tag Name: " + s[1] + "\n")
			f.write("Tag Info: " + "".join(s[2:]))
	else:
		#print("INVALID TAG")
		f.write("INVALID TAG\n")
	
s = gedcomFile.readline()
while s != "":
	#print("Checking for line: " + s)
	writeInfo(writeFile, s, levelTags)
	s = gedcomFile.readline()
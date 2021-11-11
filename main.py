from os.path import isfile

story = []

def openFile(file_name):
	f = open(file_name, 'r')
	txt = f.read()
	story = txt.split('\n')
	title = story
	if input('Make this the default story? (y/n)') == 'y':
		f = open('defaultName.txt', 'w')
		f.write(file_name)
	f.close()


def findDefault():
	f = open('defaultName.txt', 'r')
	default = f.read()
	if default == '':
		return ''
	f.close()
	return default

def fileInit():
	fileName = input("Enter the name of the story file: ")
	if not isfile(fileName):
		fileInit()
	openFile(fileName)


def filePrint():
	for i in range (story.size()-1):
		print(story[i])
	
name = findDefault()
if name == '':
	fileInit()
print(story[0])

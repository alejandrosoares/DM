from PIL import Image
from os import scandir


directory = 'C:/DistribuidoraMarcia/dm/dm/media/img/Duravit/'

categories = ['jardin', 'nenas', 'plasticos', 'playa']
fileList = []
pathFileList = []
sizeList = []


def ShowNameAndSize():

	a = 0
	for f in fileList:
		whiteSpace = 70 - len(f)
		print(f + " "*whiteSpace + str(sizeList[a]))
		a += 1 



def ShowList(array):
	a = 0
	for x in array:
		print(f'{a} - {x}')
		a += 1

def Size():
	
	for f in pathFileList:
		img = Image.open(f)
		sizeList.append(img.size)


def List(path):
	
	for c in categories:
		for o in scandir(path + c):
			if o.is_file():
				if o.name[len(o.name) - 4:] == '.jpg':
					fileList.append(o.name)
					pathFileList.append(path + c + '/' + o.name)



def Run():
	List(directory)
	Size()
	ShowNameAndSize()

if __name__=='__main__':
	Run()
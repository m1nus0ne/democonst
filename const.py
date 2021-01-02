from PIL import Image
from os import listdir,chdir
from sys import exit
from time import sleep


chdir('pic')
if len(listdir())!=1:
	print('Only 1 file expected')
	sleep(2)
	exit()

pic=listdir()[0]


im=Image.open(pic)


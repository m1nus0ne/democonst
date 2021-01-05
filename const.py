from PIL import Image,ImageDraw
from os import listdir,chdir
from sys import exit
from time import sleep
#Часто работаем с кортежами, пишем нужную функцию округления
def rround(*args):
	arr = [round(i) for i in args]
	return tuple(arr)

#Подсос избражения
chdir('pic')
if len(listdir())!=1:
	print('Only 1 file expected')
	sleep(2)
	exit()
pic=listdir()[0]
im =Image.open(pic)
#ДА
WIDTH=im.size[1]
HEIGHT=im.size[0]
BORDER=20
#Вкладываем основную пикчу в рамку, рамку+пикчу на демотиватор с надписью

b_im=Image.new('RGB',(HEIGHT+BORDER,WIDTH+BORDER),(0,0,0))
draw = ImageDraw.Draw(b_im)
draw.rectangle((0,0,HEIGHT+BORDER,WIDTH+BORDER),None,(255,255,255),BORDER//4)# TODO: Попавить расчеты
b_im.paste(im,(int(0.5*BORDER),int(BORDER*0.5)))


f_im = Image.new('RGB', rround((HEIGHT+BORDER)*1.2,(WIDTH+BORDER)*1.8),(0,0,0))
f_im.paste(b_im,rround((0.8*HEIGHT-BORDER)/8,(0.2*WIDTH-BORDER)/8))
f_im.show()



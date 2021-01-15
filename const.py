from PIL import Image, ImageDraw, ImageFont
from os import listdir, chdir
from sys import exit
from time import sleep
from CONFIG import *  # Ты шизоид?
from textwrap import wrap








# Часто работаем с кортежами, пишем нужную функцию округления
def rround(*args):
	return tuple(map(round, args))

def textprint(text,y_cord: int,font:ImageFont):
	'''В блядском PIL нет функции ввода в область, пишем ее сами
		Выравнивание по центру'''
	global Y_PLAIN
	if font.size == 40:
		text = wrap(text,HEAD_LIMIT)
		for line in text:
			x_cord = (result_image.width-len(line)*24)/2 # Оп центруем
			draw = ImageDraw.Draw(result_image)
			draw.text(rround(x_cord,y_cord),line, WHITE, HEAD_FONT)

			y_cord+=HEAD_SHIFT*1.5
	else:
		text = wrap(text, PLAIN_LIMIT)
		for line in text:
			x_cord = (result_image.width - len(line) * 17) / 2
			draw = ImageDraw.Draw(result_image)
			draw.text(rround(x_cord, y_cord), line, WHITE, PLAIN_FONT)

			y_cord += PLAIN_SHIFT * 1.5

	Y_PLAIN = y_cord





# Подсос избражения
chdir('pic')
if len(listdir()) != 1:
	print('Only 1 file expected')
	sleep(2)
	exit()
pic = listdir()[0]

im = Image.open(pic)
"""
Пояснение: автозаполнение в pycharm работает нормально, но по какой-то причине объект, создаваемый ф-цией Image.open(),
не воспринимается как объект класса Image.Image и если использовать синтаксис как показвно выше, то pycharm будет нормально с ним работать
P.S. с Image.new() такого не происходит
/m1nus0ne: Напоминает ожидаемый тип ввода в функциях
P.S. Это рыготня опять не видит CONFIG.py
/Мамин поц: видит
"""
height = im.height
width = im.width
# Вкладываем основную пикчу в рамку, рамку+пикчу на демотиватор с надписью

background = Image.new('RGB', (width + BORDER, height + BORDER), (0, 0, 0))

draw = ImageDraw.Draw(background)
draw.rectangle((0, 0, width + BORDER, height + BORDER), None, WHITE, LINE_SIZE)
background.paste(im, rround(0.5 * BORDER, BORDER * 0.5))

result_image = Image.new('RGB', (background.width + 2 * IMAGE_OFFSET_X, background.height + IMAGE_OFFSET_Y + TEXT_OFFSET))
# На самом деле TEXT_OFFSET должено быть переменной
result_image.paste(background, (IMAGE_OFFSET_X, IMAGE_OFFSET_Y))
HEAD_LIMIT =(background.width - IMAGE_OFFSET_X)//24
PLAIN_LIMIT = (background.width - IMAGE_OFFSET_X)//17

# Добавляем текст по классике: ЗАГОЛОВОК текст, маштабируем поле ввода вниз, ширина по консту
# Отцентровка расчитываеться отдельно
draw = ImageDraw.Draw(result_image)
textprint(HEAD_TEXT,background.height+IMAGE_OFFSET_Y,HEAD_FONT)
textprint(PLAIN_TEXT,Y_PLAIN,PLAIN_FONT)
result_image.show()
print((width, width))
print(result_image.size)
print(Y_PLAIN)
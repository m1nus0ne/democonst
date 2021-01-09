from PIL import Image, ImageDraw, ImageFont
from os import listdir, chdir
from sys import exit
from time import sleep
from CONFIG import *  # Ты шизоид?
from textwrap import wrap

# Часто работаем с кортежами, пишем нужную функцию округления
def rround(*args):
	return tuple(map(round, args))
def 

# Подсос избражения
chdir('pic')
if len(listdir()) != 1:
	print('Only 1 file expected')
	sleep(2)
	exit()
pic = listdir()[0]

im: Image.Image = Image.open(pic)
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

background = Image.new('RGB', (width + BORDER, height + BORDER), (0, 0, 0))  # TODO: здесь

draw = ImageDraw.Draw(background)
draw.rectangle((0, 0, width + BORDER, height + BORDER), None, WHITE, LINE_SIZE)
background.paste(im, rround(0.5 * BORDER, BORDER * 0.5))  # TODO: и здесь заменить BORDER через LINE_SIZE

result_image = Image.new('RGB', (width + 2 * IMAGE_OFFSET_X, height + IMAGE_OFFSET_Y + TEXT_OFFSET))
# На самом деле TEXT_OFFSET должено быть переменной
result_image.paste(background, (IMAGE_OFFSET_X, IMAGE_OFFSET_Y))
HEAD_LIMIT =(result_image.width - IMAGE_OFFSET_X)//24
PLAIN_LIMIT = (result_image.width - IMAGE_OFFSET_X)//17

# Добавляем текст по классике: ЗАГОЛОВОК текст, маштабируем поле ввода вниз, ширина по консту
# !!!!!16pt == 9pic
draw = ImageDraw.Draw(result_image)
draw.text((IMAGE_OFFSET_X, height+IMAGE_OFFSET_Y*2), 'NIGGERS '*10, font=PLAIN_FONT,fill=WHITE,align='m')
result_image.show()
print((width, width))
print(result_image.size)

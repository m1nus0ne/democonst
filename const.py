from PIL import Image, ImageDraw
from os import listdir, chdir
from sys import exit
from time import sleep
from constants import *


# Часто работаем с кортежами, пишем нужную функцию округления
def rround(*args):
    return tuple(map(round, args))


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
"""
height = im.size[0]
width = im.size[1]
# Вкладываем основную пикчу в рамку, рамку+пикчу на демотиватор с надписью

background = Image.new('RGB', (height + BORDER, width + BORDER), (0, 0, 0)) # TODO: здесь
draw = ImageDraw.Draw(background)
draw.rectangle((0, 0, height + BORDER, width + BORDER), None, WHITE, LINE_SIZE)
background.paste(im, (int(0.5 * BORDER), int(BORDER * 0.5))) # TODO: и здесь заменить BORDER через LINE_SIZE

result_image = Image.new('RGB', (height + 2 * IMAGE_OFFSET_X, width + IMAGE_OFFSET_Y + TEXT_OFFSET))
# На самом деле TEXT_OFFSET должено быть переменной
result_image.paste(background, (IMAGE_OFFSET_X, IMAGE_OFFSET_Y))
result_image.show()

from PIL import Image, ImageDraw, ImageFont
from os import listdir, chdir
from sys import exit
from time import sleep
from democonst.CONFIG import *   # TODO: Блять у тебя справка с дурки есть? Шпак помоги



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
/m1nus0ne: Напоминает ожидаемый тип ввода в функциях
P.S. Это рыготня опять не видит CONFIG.py
"""
height = im.size[0]
width = im.size[1]
# Вкладываем основную пикчу в рамку, рамку+пикчу на демотиватор с надписью

background = Image.new('RGB', (height + BORDER, width + BORDER), (0, 0, 0)) # TODO: здесь
draw = ImageDraw.Draw(background)
draw.rectangle((0, 0, height + BORDER, width + BORDER), None, WHITE, LINE_SIZE)
background.paste(im, (int(0.5 * BORDER), int(BORDER * 0.5))) # TODO: и здесь заменить BORDER через LINE_SIZE

result_image = Image.new('RGB', (height + 2 * IMAGE_OFFSET_X, width + IMAGE_OFFSET_Y + TEXT_OFFSET))
# На самом деле TEXT_OFFSET должено быть переменной /m1nus0ne Подергал ползунки на сайте, там все по консту
result_image.paste(background, (IMAGE_OFFSET_X, IMAGE_OFFSET_Y))
result_image.show()
#Добавляем текст по классике: ЗАГОЛОВОК текст, маштабируем поле ввода
#TODO: Сказывается ли отсутствие одного текста на расположеие другого?
HEAD =
head_image = Image.new()




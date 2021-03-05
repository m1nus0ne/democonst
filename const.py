from PIL import Image, ImageDraw
from os import listdir, chdir
from sys import exit
from time import sleep
from CONFIG import *
from textwrap import wrap


#Читем текст для демотиватора
with open('text.txt', encoding='utf-8') as file:
    try:
        N = int(file.readline())

        text = file.readlines()
    except ValueError:
        print('Проверьте заполнение text.txt согласно образцу')
        input()
        exit()
ARR = []
for i in range(0,2*N,2):
    ARR.append([text[i][:-1:],text[i+1][:-1:]])



# Часто работаем с кортежами, пишем нужную функцию округления
def rround(*args):
    return tuple(map(round, args))


def textprint(text, y_cord: int, font: ImageFont):
    '''В (уважаемом) PIL нет функции ввода в область, пишем ее сами
		Выравнивание по центру'''
    if font.size == 40:
        text = wrap(text, HEAD_LIMIT)
        for line in text:
            x_cord = (result_image.width - len(line) * 24) / 2  # Оп центруем
            draw = ImageDraw.Draw(result_image)
            draw.text(rround(x_cord, y_cord), line, WHITE, HEAD_FONT)

            y_cord += HEAD_SHIFT * 1.5
    else:
        text = wrap(text, PLAIN_LIMIT)
        for line in text:
            x_cord = (result_image.width - len(line) * 17) / 2
            draw = ImageDraw.Draw(result_image)
            draw.text(rround(x_cord, y_cord), line, WHITE, PLAIN_FONT)

            y_cord += PLAIN_HEIGHT * 1.5



# Подсос избражения
chdir('pic')
if len(listdir()) != 1:
    print('Папка pic должна содержать только 1 изображение')
    sleep(2)
    exit()
pic = listdir()[0]
im = Image.open(pic)



# Вкладываем основную пикчу в рамку, рамку+пикчу на демотиватор с надписью
for i in range(N):
    height = im.height
    width = im.width
    HEAD_TEXT = ARR[i][0]
    PLAIN_TEXT = ARR[i][1]



    background = Image.new('RGB', (width + BORDER, height + BORDER), (0, 0, 0))
    HEAD_LIMIT = (background.width - IMAGE_OFFSET_X) // 24
    PLAIN_LIMIT = (background.width - IMAGE_OFFSET_X) // 17



    draw = ImageDraw.Draw(background)
    draw.rectangle((0, 0, width + BORDER, height + BORDER), None, WHITE, LINE_SIZE)
    background.paste(im, rround(0.5 * BORDER, BORDER * 0.5))



    TEXT_OFFSET = int(
        len(wrap(HEAD_TEXT, HEAD_LIMIT)) * HEAD_HEIGHT * 1.5 + len(wrap(PLAIN_TEXT, PLAIN_LIMIT)) * PLAIN_HEIGHT * 1.5)
    result_image = Image.new('RGB', (
    background.width + 2 * IMAGE_OFFSET_X, background.height + 2 * IMAGE_OFFSET_Y + TEXT_OFFSET + INDENTS_OFFSET * 2))
    result_image.paste(background, (IMAGE_OFFSET_X, IMAGE_OFFSET_Y))



    # Добавляем текст по классике: ЗАГОЛОВОК текст, маштабируем поле ввода вниз, ширина по консту
    # Отцентровка расчитываеться отдельно
    draw = ImageDraw.Draw(result_image)
    textprint(HEAD_TEXT, background.height + IMAGE_OFFSET_Y + INDENTS_OFFSET, HEAD_FONT)
    Y_PLAIN = background.height + IMAGE_OFFSET_Y + INDENTS_OFFSET + len(wrap(HEAD_TEXT, HEAD_LIMIT))*HEAD_HEIGHT*1.5
    textprint(PLAIN_TEXT, Y_PLAIN + INDENTS_OFFSET, PLAIN_FONT)
    result_image.thumbnail(im.size)
    im = result_image
im = Image.open(pic)
result_image.thumbnail(im.size)


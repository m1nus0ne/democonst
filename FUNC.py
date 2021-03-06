from textwrap import wrap
from PIL import Image, ImageDraw
from CONFIG import *

# Часто работаем с кортежами, пишем нужную функцию округления
def rround(*args):
    return tuple(map(round, args))


def textprint(text, y_cord: int, font: ImageFont, img: Image, limit : int):
    '''В (уважаемом) PIL нет функции ввода в область, пишем ее сами
		Выравнивание по центру'''
    if font.size == 40:
        text = wrap(text, limit)
        for line in text:
            x_cord = (img.width - len(line) * HEAD_WIDTH) / 2  # Оп центруем
            draw = ImageDraw.Draw(img)
            draw.text(rround(x_cord, y_cord), line, WHITE, HEAD_FONT)

            y_cord += HEAD_HEIGHT * 1.5
    else:
        text = wrap(text, limit)
        for line in text:
            x_cord = (img.width - len(line) * PLAIN_WIDTH) / 2
            draw = ImageDraw.Draw(img)
            draw.text(rround(x_cord, y_cord), line, WHITE, PLAIN_FONT)

            y_cord += PLAIN_HEIGHT * 1.5



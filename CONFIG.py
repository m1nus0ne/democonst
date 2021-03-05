from PIL import ImageFont

#Дружокб, каждое изменение этого файла лучше избежать
BORDER = 20 #Рамка
IMAGE_OFFSET_X = 68 #Вертикальный отступ
IMAGE_OFFSET_Y = 37 #Горизонтальный отступ
LINE_SIZE = 4 #Толщина обводки рамки
INDENTS_OFFSET = 30 #Отступ между абзацаи


# COLORS
WHITE = (255, 255, 255)  # POWER
BLACK = (0, 0, 0)  # LIVES MATTER

#КАТЕГОРИЧЕСКИ НЕ СОВЕТУЮ ИЗМЕНЯТЬ
HEAD_FONT = ImageFont.truetype('font.ttf',  size=40) # 24pic ширина 28pic высота
HEAD_HEIGHT = 28
HEAD_WIDTH = 24
PLAIN_FONT = ImageFont.truetype('font.ttf',  size=28)  # 17pic ширина 20pic  высота
PLAIN_HEIGHT = 20
PLAIN_WIDTH = 17

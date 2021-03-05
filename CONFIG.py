from PIL import ImageFont

#Дружокб, каждое изменение этого файла лучше избежать
BORDER = 20
IMAGE_OFFSET_X = 68
IMAGE_OFFSET_Y = 37

LINE_SIZE = 4
HEAD_FONT = ImageFont.truetype('font.ttf',  size=40)  # 24pic ширина 28pic высота
PLAIN_FONT = ImageFont.truetype('font.ttf',  size=28)  # 17pic ширина 20pic  высота
HEAD_SHIFT = 28
PLAIN_SHIFT = 20
INDENTS_OFFSET = 15



# COLORS
WHITE = (255, 255, 255)  # POWER
BLACK = (0, 0, 0)  # LIVES MATTER

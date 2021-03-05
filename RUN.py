from  os import chdir
from const import  result_image,pic
result_image.show()

if input('Сохранить? (y/n)\n') == 'y':
    chdir('../result')
    result_image.save(pic)
    print('Ваш демотиватор сохранен в папку result\n'
          'После работы не забудте очистить папки result и pic')



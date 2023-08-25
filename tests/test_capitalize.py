#from exercises.capitalize import capitalize
from capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно для пустой строки!')

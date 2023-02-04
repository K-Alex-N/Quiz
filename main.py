print('''
1. Игра
2. Статистика
3. Админ панель
''')
while True:
    a = input('Введите номер меню: ')
    if a in ('123'):
        break
    else:
        print('Номер должен быть от 1го до 3х')

if a == 1:
    pass
elif a == 2:
    pass
else:
    assert a != 3
    pass

#######################################

class Game:
    def __init__(self):
        self.score = 0

class User:
    def __init__(self, name):
        self.name = name
        self.score = 0

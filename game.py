def start_game(player):
    score = 0
    print('___Игра началачь___')
    print(f'Игрок: {player}. Счет: {score}')


def get_list_of_users():
    f = open('users/users.txt', encoding='utf-8')
    return [x.split()[0] for x in f.readlines()]


def create_new_user() -> str:
    a = input('Введите имя нового игрока: ')
    f = open('users/users.txt', 'a', encoding='utf-8')
    f.write(f'\n{a}')
    f.close()
    return a


def introduction():
    p = [
        '1. Создать нового игрока',
        '*  Выбрать игрока из списка ниже'
    ]
    tuple(map(print, p))

    list_of_users = get_list_of_users()
    for i, v in enumerate(list_of_users):
        print(f'   {i + 2}. {v}')

    while True:
        a = input('\nВыберите пункт меню: ').strip()
        try:
            a = int(a.strip())
        except:
            print('Неверный формат данных. Должно быть целое число.')
            continue
        if a == 1:
            player = create_new_user()
        elif a in range(2, len(list_of_users) + 2):
            player = list_of_users[a - 2]
        else:
            print('Такого номер нет в меню')
            continue
        start_game(player)
        break


introduction()


def user_list():
    pass

from os import listdir, remove


def quiz_list():
    i = 1
    for file in listdir(path='quiz'):
        f = open(f'quiz/{file}', encoding='utf-8')  # контекстным менеджером переписать
        print(f'{i}. {f.readline()}', end='')
        f.close()
        i += 1





def get_file_idx() -> set[int]:
    "создаем актуальное множество из названий всех файлов с вопросами (название без '.txt', только число)"
    return set(int(x[:-4]) for x in listdir(path='quiz'))


def is_valid_del_data(s: str) -> bool:
    try:
        lst = list(map(int, s.split()))
    except:
        print('В списке должны быть только номера вопросов')
        return False

    flag = True
    l = len(get_file_idx())
    for x in lst:
        if x <= 0 or x - 1 >= l:
            print(f'Нет вопроса с номером {x}')
            flag = False

    return flag

def del_quiz(s: str) -> None:
    # нужна проверка введенных данных
    if not is_valid_del_data(s):
        # вернуться на повторный запрос ввода на удаление
        # и там должга быть отмена (выход) из запроса на удаление (т.к. если человек передумал то без удаления чего то он выйти не сможет)

    # get_file_idx()
    question_list = listdir(path='quiz')
    for i in s.split():
        try:
            file_name = question_list[int(i)]
            remove(f'quiz/{file_name}')
            print(f'Вопрос под номером {int(i) + 1} удален')
        except:
            print(f'Не удалось удалить вопрос под номером {int(i) + 1}')

is_valid_del_data('1 3 2')
# del_quiz('1')

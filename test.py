from os import listdir, remove

i = 1
for file in listdir(path='quiz'):
    f = open(f'quiz/{file}', encoding='utf-8')    # контекстным менеджером переписать
    print(f'{i}. {f.readline()}', end='')
    f.close()
    i += 1


def del_quiz(s: str) -> None:
    # нужна проверка введенных данных
    question_list = listdir(path='quiz')
    for i in s.split():
        try:
            file_name = question_list[int(i)]
            remove(f'quiz/{file_name}')
            print(f'Вопрос под номером {int(i) + 1} удален')
        except:
            print(f'Не удалось удалить вопрос под номером {int(i)+1}')

def is_data_valid(s: str) -> bool:


del_quiz('1')
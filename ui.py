import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите название : '), number)
    body = check_len_text_input(
        input('Введите текст: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nПрограмма 'Заметки'. \n\n"
          "Меню:\n\n"
          "1 - показать все заметки\n"
          "2 - добавить заметки\n"
          "3 - удалить заметки\n"
          "4 - редактировать заметки\n"
          "5 - поиск заметки по дате\n"
          "6 - поиск заметки по id\n"
          "7 - выход\n\n"
          "Выберете необходимую функцию: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Программа завершает работу, до свидания!")

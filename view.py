commands=['Открыть файл',
          'Сохранить файл',
          'Показать все контакты',
          'Создать контакт',
          'Удалить контакт',
          'Изменить контакт',
          'Найти контакт',
          'Выход из программы']

def main_menu() -> int:
    print('Главное меню:\t')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}.{item}')
    choice = int(input('Выберите пункт меню: '))
    return choice

def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()
def input_error():
    print('Ошибка ввода. Введите корректный пункт меню')

def create_new_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find=input('Введите искомый элемент:')
    return find

def change_contact():
    find=input('Введите имя контакта, который хотите изменить:')
    return find



phonebook = []
path = "phonebook.txt"

def get_phonebook():
    global phonebook
    return phonebook

def open_file():
    global phonebook
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file=data.readlines()
    for contact in file:
        phonebook.append(contact.strip().split(';'))
    print('Файл успешно открыт')

def add_new_contact(new_contact: list):
    global phonebook
    phonebook.append(new_contact)

def search_contact(find: str):
    global phonebook
    result = []
    for contact in phonebook:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def save_file():
    global phonebook
    global path
    pb_str=[]
    for contact in phonebook:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))
    print('Файл сохранен')

def delete_contact(find:str):
    global phonebook
    global path
    new_phonebook=[]
    for contact in phonebook:
        if find in contact[0]:
            pass
        else:
            new_phonebook.append(';'.join(contact))
            with open(path, 'w', encoding='UTF-8') as data:
                data.write('\n'.join(new_phonebook))
            print('Запись удалена')

def change_contact(find):
    global phonebook
    index=0
    contact_to_change = search_contact(find)
    for i, contact in enumerate(phonebook):
        if contact_to_change[0][0] in contact[0]:
            index=i
            break
    choice=int(input('Выберите, что хотите изменить:\n\t1-имя\n\t2-номер телефона\n\t3-комментарий\n'))
    match choice:
        case 1:
            phonebook[index][0] = input('Введите новое имя:')
        case 2:
            phonebook[index][1] = input('Введите новый телефон: ')
        case 3:
            phonebook[index][2] = input('Введите новый комментарий')
    print("контакт изменен")
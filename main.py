def work_with_contacts():
    choice = show_menu()
    contacts = read_txt('contacts.txt')
    

    while choice!= 8:
        if choice == 1:
            print_result(contacts)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(contacts, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(contacts, last_name, new_number))
        elif choice == 4:
            lastname = input('Введите фамилию: ')
            print(delete_by_lastname(contacts, lastname))
        elif choice == 5:
            number = input('Введите номер: ')
            print(find_by_number(contacts, number))
        elif choice == 6:
            user_data = input('Введите новые данные: ')
            add_user(contacts, user_data)
            write_txt('contacts.txt', contacts)
        elif choice == 7:  
            src_file = input('Введите имя исходного файла: ')
            dst_file = input('Введите имя целевого файла: ')
            line_num = int(input('Введите номер строки для копирования: '))
            copy_line(src_file, dst_file, line_num)
            print(f'Строка {line_num} из файла {src_file} скопирована в файл {dst_file}')

        choice = show_menu()
        if choice == 8:
            write_txt('contacts.txt', contacts)
            break

def show_menu():
    print('Меню:')
    print('1. Показать телефонную книгу')
    print('2. Найти по фамилии')
    print('3. Изменить номер')
    print('4. Удалить по фамилии')
    print('5. Найти по номеру')
    print('6. Добавить новый контакт')
    print('7. Копировать данные из одного файла в другой')
    print('8. Выход')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 1 <= choice <= 8:
                return choice
            else:
                print('Неверный выбор. Пожалуйста, выберите пункт от 1 до 8.')
        except ValueError:
            print('Неверный ввод. Пожалуйста, введите число.')

def read_txt(filename):
    contacts = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'], line.strip().split(',')))
            contacts.append(record)
    return contacts

def write_txt(filename, contacts):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in contacts:
            phout.write(','.join(record.values()) + '\n')

def print_result(contacts):
    for record in contacts:
        print(record)

def find_by_lastname(contacts, last_name):
    result = [record for record in contacts if record['Фамилия'] == last_name]
    if result:
        return result
    else:
        return 'Контакт не найден'

def change_number(contacts, last_name, new_number):
    for record in contacts:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return 'Номер изменен'
    return 'Контакт не найден'

def delete_by_lastname(contacts, lastname):
    contacts[:] = [record for record in contacts if record['Фамилия']!= lastname]
    return 'Контакт удален'

def find_by_number(contacts, number):
    result = [record for record in contacts if record['Телефон'] == number]
    if result:
        return result
    else:
        return 'Контакт не найден'

def add_user(contacts, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    contacts.append(record)

def copy_line(src_file, dst_file, line_num):
    with open(src_file, 'r', encoding='utf-8') as src:
        lines = src.readlines()
        if line_num > 0 and line_num <= len(lines):
            line_to_copy = lines[line_num - 1]
            with open(dst_file, 'a', encoding='utf-8') as dst:
                dst.write(line_to_copy)
        else:
            print('Неверный номер строки')

work_with_contacts()
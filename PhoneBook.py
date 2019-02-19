import pickle
from password import password_func

'''Phonebook'''
'''before use of 'phone.dat' file requared to fill and pickle 
object(dictionary - keys(names) : values(phonenumbers)) by 'data.py' file'''


def title():
    '''Функция выводит заголовок'''
    print('''
###############################################################
            ДОБРО ПОЖАЛОВАТЬ В "ТЕЛЕФОННЫЙ СПРАВОЧНИК УПО"
###############################################################
'''
)


def menu():
    '''Функция выводит меню выбора'''
    print('''		    МЕНЮ ПРОГРАММЫ
        	1 - Просмотреть весь справочник УПО.
        	2 - Найти сотрудника УПО по фамилии.
        	3 - Добавить сотрудника в телефонный справочник.
        	4 - Удалить сотрудника из телефонного справочника.
        	5 - Выход.
        ''')


def choice_func():
    choice = input('Сделайте Ваш выбор: ')
    return choice


def cont_list():
    print('***********************')
    print('СПИСОК СОТРУДНИКОВ УПО: ')        
    print('***********************')
    with open('phones.dat', 'rb') as f:
        data_phones = pickle.load(f)
        i = 1
        for key, value in sorted(data_phones.items()):
            print('{}. {} : {}'.format(i, key, value))
            i += 1
    print()


def cont_search():
    sec_name = (input('\nВведите фамилию сотрудника, чтобы найти телефон: ').upper())
    with open('phones.dat', 'rb') as f:
        data_phones = pickle.load(f)
        try:
            print('\n-->', sec_name, ' : ', data_phones[sec_name], '\n')
        except KeyError as k:
            print('\n==>', k, '<== Сотрудника с такой фамилией нет!\n')


def cont_add():
    name_to_add = (input('\nУкажите фамилию сотрудника для добавления в справочник: ').upper())
    number = (input('Укажите номер телефона нового сотрудника: '))
    with open('phones.dat', 'rb') as f:
        data_phones = pickle.load(f)
        if name_to_add not in data_phones.keys():
            data_phones.update({name_to_add: number})
            with open('phones.dat', 'wb') as f:
                pickle.dump(data_phones, f)
                print('\n==> Сотрудник с фамилией {} успешно добавлен в справочник.\n'.format(name_to_add))
        else:
            print('\n==> Сотрудник с фамилией {} уже есть в справочнике.\n'.format(name_to_add))


def cont_del():
    name_to_del = (input('\nУкажите фамилию сотрудника для удаления из справочника: ').upper())
    with open('phones.dat', 'rb') as f:
        data_phones = pickle.load(f)
        if name_to_del in data_phones.keys():
            del data_phones[name_to_del]
            print('\n==> {} успешно удален из справочника.\n'.format(name_to_del))
            with open('phones.dat', 'wb') as f:
                pickle.dump(data_phones, f)
        else:
            print('\n==> Сотрудника {} нет в справочнике.\n'.format(name_to_del))


def exit_ContList():
    print('\nЖелаю удачи! До свидания!')


def launch_choice():
    choice = choice_func()
    while True:
        if choice == '1':
            cont_list()
        elif choice == '2':
            cont_search()
        elif choice == '3':
            cont_add()
        elif choice == '4':
            cont_del()
        elif choice == '5':
            exit_ContList()
            break
        else:
            print('\nИзвините, в меню нет пункта <<{}>>.'.format(choice))
            print('==> Сделайте правильный выбор из меню.\n')
        menu()
        choice = input('\nСделайте Ваш выбор: ')


if __name__ == '__main__':
    # password_func()
    title()
    menu()
    launch_choice()


input('\nPress Enter to exit...')

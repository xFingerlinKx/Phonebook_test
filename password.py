def password_func():
    '''Функция запрашивает пароль при входе в программу'''
    password = input('Введите пароль: ')
    print()
    while password != '123':
        print('Пароль неверный.\n', end='')
        password = input('Введите пароль: ')
        print()
    if password == '123':
        print('Доступ разрешен.')

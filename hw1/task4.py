def check_user1(user_dict):
    user_name = input('Введите свой логин: ')
    user_pwd = input('Введите свой пароль: ')
    for key, val in user_dict.items():  #  O(n)
        if (user_name == key) and (user_pwd == val[0]):
            if val[1]:
                return user_name, True  #  O(1)
            else:
                print(f'Вы не активировали свою учетную запись. Хотите активировать сейчас?')
                if input('Yes/No ?') in ['Yes', 'yes', 'YES', 'y', 'Y']:
                    print('Наслаждайтесь доступом!')
                    return user_name, True  #  O(1)
                else:
                    print('Доступ запрещен')
                    return user_name, False  #  O(1)
    print(f'{user_name} не зарегестрирован или не верный пароль')
    return user_name, False
"""сложность алгоритма O(n)"""

def check_user2(user_dict):
    user_name = input('Введите свой логин: ')
    user_pwd = input('Введите свой пароль: ')
    if user_dict.get(user_name) is None:    # O(1)
        print(f'{user_name} не зарегестрирован или не верный пароль')
        return user_name, False
    if user_dict[user_name][0] == user_pwd:  # O(1)
        if not user_dict[user_name][1]:
            print(f'Вы не активировали свою учетную запись. Хотите активировать сейчас?')
            user_answer = input('Yes/No ?')  # O(1)
            if user_answer in ['Yes', 'yes', 'YES', 'y', 'Y']:
                print('Наслаждайтесь доступом!')
            else:
                print('Доступ запрещен')
                return user_name, False
        return user_name, True
"""сложность второго алгоритма O(1)"""

user_dict = {'Soldat': ['pwdSoldat', True], 'Ivanov': ['pwdIvanov', False], 'Haba': ['pwdHaba', False],
             'Peto': ['pwdPeto', True], 'Slonov': ['pwdSlonov', False], 'Solomon': ['pwdSolomon', True], }
user_name, activatad = check_user1(user_dict)
if activatad:
    user_dict[user_name][1] = True
print('=================Method 2===================')
user_name, activatad = check_user2(user_dict)
if activatad:
    user_dict[user_name][1] = True

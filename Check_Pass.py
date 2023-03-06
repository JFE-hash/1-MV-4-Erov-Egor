print('Введите пароль: ')
pass_check1 = input()
print('Повторите пароль: ')
pass_check2 = input()
if pass_check1 == pass_check2:
    print('Пароль принят')
else:
    print('Пароль не принят')
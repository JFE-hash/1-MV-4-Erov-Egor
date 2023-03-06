print('Введите первый цвет: ')
first_col = input()
print('Введите второй цвет: ')
second_col = input()
if first_col == 'Красный' and second_col == 'Синий':
    print('Получится фиолетовый')
elif first_col == 'Синий' and second_col == 'Красный':
    print('Получится фиолетовый')
elif first_col == 'Красный' and second_col == 'Желтый':
    print('Получится оранжевый')
elif first_col == 'Желтый' and second_col == 'Красный':
    print('Получится оранжевый')
elif first_col == 'Синий' and second_col == 'Желтый':
    print('Получится зеленый')
elif first_col == 'Желтый' and second_col == 'Синий':
    print('Получится зеленый')
else:
    print('Неверный формат данных')
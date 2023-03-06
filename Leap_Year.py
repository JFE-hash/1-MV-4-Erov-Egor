def leap_is(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        print(f'Год {year} - високосный')
    else:
        print('Этот год не високосный')


leap_is(2004)
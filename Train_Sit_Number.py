cupe_down = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
cupe_up = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
plaz_up = [38, 40, 42, 44, 46, 48, 50, 52, 54]
plaz_dowmn = [37, 39, 41, 43, 45, 47, 49, 51, 53]
print('Какое у вас место?')
n = int(input())
if n in cupe_down:
    print(f'Ваше место {n} - нижнее купе')
elif n in cupe_up:
    print(f'Ваше место {n} - верхнее купе')
elif n in plaz_up:
    print(f'Ваше место {n} - верхний плацкарт')
else:
    print(f'Ваше место {n} - нижний плацкарт')
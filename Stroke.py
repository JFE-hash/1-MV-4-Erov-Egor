print('Сколько слов вы хотите?')
n = int(input())
print('Введите слова по порядку: ')
stroke = ''
for i in range(n):
    word = input()
    stroke += word
print('Получившаяся строка:', stroke)
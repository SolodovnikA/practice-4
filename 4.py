print('Вы поедете на бал?')
ans = input()
error = ['Да', 'да', 'Нет', 'нет']
if ans not in error:
    print('Верно')
else:
    print('Неверно')
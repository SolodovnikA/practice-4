length = input('Собака короткошёрстной породы? ')
height1 = input('Рост собаки менее 50 см? ')
tail = input('У собаки короткий хвост? ')
ears = input('У собаки длинные уши?')
body = input('У собаки короткое тело? ')
weight = input('Собака весит более 50 кг? ')
nature = input('У собаки доброжелательный характер? ')
height2 = input('У собаки рост менее 70 см? ')
colour = input('Окрас рыжий с белыми отметинами? ')
white = input('Белоснежный окрас? ')
# Да
# да
# Нет
# нет
if length == 'Да' or length == 'да':
    if height1 == 'Да' or height1 == 'да':
        if tail == 'Да' or tail == 'да':
            print('Английский бульдог')
        elif tail == 'Нет' or tail == 'нет':
            if ears == 'Да' or ears == 'да':
                print('Гончая')
            elif ears == 'Нет' or ears == 'нет':
                if body == 'Да' or body == 'да':
                    print('Мопс')
                elif body == 'Нет' or body == 'нет':
                    print('Чихуахуа')
    elif height1 == 'Нет' or height1 == 'нет':
        if weight == 'Да' or weight == 'да':
            print('Датский дог')
        elif weight == 'Нет' or weight == 'нет':
            print('Фоксхаунд')
elif length == 'Нет' or length == 'нет':
    if height1 == 'Да' or height1 == 'да':
        if nature == 'Да' or nature == 'да':
            print('Кокер-спаниэль')
        elif nature == 'Нет' or nature == 'нет':
            print('Ирландский сеттер')
    elif height1 == 'Нет' or height1 == 'нет':
        if height2 == 'Да' or height2 == 'да':
            if ears == 'Да' or ears == 'да':
                print('Большой вандейский грифон')
            elif ears == 'Нет' or ears == 'нет':
                print('Колли')
        elif height2 == 'Нет' or height2 == 'нет':
            if colour == 'Да' or colour == 'да':
                print('Сенбернар')
            elif colour == 'Нет' or colour == 'нет':
                if white == 'Да' or white == 'да':
                    print('Ирландский волкодав')
                elif white == 'Нет' or white == 'нет':
                    print('Ньюфаундленд')


print()     # Отступ


# Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки)
# с двумя каменными вставками для чисел.

# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом,
# а второе было всегда пустым.

# К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус,
# где были написаны правила для решения этого "ребуса".

# Во вторую вставку нужно было написать те пары чисел друг за другом,
# чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.

# Пример кратности(деления без остатка):
# 1 + 2 = 3 (сумма пары)
# 9 / 3 = 3 (ровно 3 без остатка)
# 9 кратно 3 (9 делится на 3 без остатка)

# Пример 1:
# 9 - число из первой вставки
# 1218273645 - нужный пароль
# (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)

# Можно использовать как цикл for, так и цикл while
# Первое число не входит в одно из чисел пары
# Пары чисел подбираются от 1 до 20 для текущего числа.

num = int(input('Введите число: '))

result = ''
# Проходимся циклом от 1, т.к. первое число не входит в одно из чисел пары,
# и до num, при этом не учитывается последнее число в num
for i in range(1, num):
    # Подбираем пару для этого проходимся циклом от i+1,
    # т.к. второе число должно быть на 1 больше первого,
    # и до num, при этом не учитывается последнее число в num
    for j in range(i+1, num):
        if num % (i+j) == 0:
            result += f'{i}{j}'

print(f'{num} - {result}')



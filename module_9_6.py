print()     # Отступ


# Напишите функцию-генератор all_variants(text), которая принимает строку text и
# возвращает объект-генератор, при каждой итерации которого будет возвращаться
# подпоследовательности переданной строки.

def all_variants(text):
    len_text = len(text)

    # Перебираем все возможные длины подпоследовательностей от 1 до n
    for i in range(1, len_text + 1):

        # Перебираем все возможные начальные позиции подпоследовательностей для текущей длины
        for start in range(len_text - i + 1):
            yield text[start:start + i]


a = all_variants("abc")
for i in a:
    print(i)

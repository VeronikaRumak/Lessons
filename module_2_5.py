print() # Отступ

# Напишите функцию get_matrix с тремя параметрами n, m и value,
# которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
# заполненную значениями value и возвращать эту матрицу в качестве результата работы.

# Объявите функцию get_matrix и напишите в ней параметры n, m и value.
# Создайте пустой список matrix внутри функции get_matrix.
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):  # Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
        matrix.append([])  # В первом цикле добавляйте пустой список в список matrix.
        for j in range(m):  # Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
            matrix[i].append(value)  # Во втором цикле пополняйте ранее добавленный пустой список значениями value.
    return matrix  # После всех циклов верните значение переменной matrix.

# Выведите на экран(консоль) результат работы функции get_matix.
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)


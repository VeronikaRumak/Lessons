from module_fake_math import divide as fake_divide
from module_true_math import divide as true_divide

# Создайте модули fake_math и true_math.
# Напишите функции divide в обоих методах. Разница между этими функциями - возвращаемое значение.
# Создайте модуль main (если ещё не создан),
# импортируйте в него функции divide из модулей fake_math и true_math,
# назвав их разными именами на своё усмотрение, чтобы не было конфликтов имён,
# при помощи оператора as.
# Запустите эти функции в модуле main,
# передав первым аргументом произвольное число отличное от 0, вторым аргументом - 0
# Выведи результаты вызовов этих функций на экран(в консоль).


result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

print()     # Отступ


# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.


# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции
# будет простым числом и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res > 1:
            for i in range(2, res + 1):
                if res % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")

        return res
    return wrapper


# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)



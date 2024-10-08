import datetime
from multiprocessing import Pool


print()     # Отступ


# Создайте функцию read_info(name), где name - название файла. Функция должна:
def read_info(name):

    # Создавать локальный список all_data.
    all_data = []

    # Открывать файл name для чтения.
    with open(name, 'r', encoding='utf-8') as file:

        # Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
        while True:
            line = file.readline()
            if not line:
                break

            # Во время считывания добавлять каждую строку в список all_data.
            all_data.append(line)


# Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.

# Создайте список названий файлов в соответствии с названиями файлов архива.
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Вызовите функцию read_info для каждого файла по очереди (линейно)
# и измерьте время выполнения и выведите его в консоль.
start_time_line = datetime.datetime.now()

for filename in filenames:
    read_info(filename)

end_time_line = datetime.datetime.now()

print(f"Время выполнения линейного вызова: {end_time_line - start_time_line}")


# Используйте конструкцию if __name__ == '__main__' при многопроссном подходе.
if __name__ == '__main__':

    start_time_multi = datetime.datetime.now()

    # Вызовите функцию read_info для каждого файла, используя многопроцессный подход:
    # контекстный менеджер with и объект Pool.
    with Pool(processes=4) as pool:

        # Для вызова функции используйте метод map,
        # передав в него функцию read_info и список названий файлов.
        pool.map(read_info, filenames)

    end_time_multi = datetime.datetime.now()

    # Измерьте время выполнения и выведите его в консоль.
    print(f"Время выполнения многопроцессного вызова: {end_time_multi - start_time_multi}")





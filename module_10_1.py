# Сделать паузу можно при помощи функции sleep из модуля time,
# предварительно импортировав её: from time import sleep.
from time import sleep
from threading import Thread
from datetime import datetime


print()     # Отступ


# Необходимо создать функцию write_words(word_count, file_name),
# где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
def write_words(word_count, file_name):

    # Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>"
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}"
            file.write(word + '\n')

            # в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
            sleep(0.1)

    # В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
    print(f"Завершилась запись в файл {file_name}")


# Взятие текущего времени
start_time_func = datetime.now()

# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
# Объявление функции write_words
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time_func = datetime.now()

# Вывод разницы начала и конца работы функций
print(f"Время выполнения функций: {end_time_func - start_time_func} секунд")


# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами
# для функции:

# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков.
start_time_thread = datetime.now()

thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

end_time_thread = datetime.now()

print(f"Время выполнения потоков: {end_time_thread - start_time_thread} секунд")

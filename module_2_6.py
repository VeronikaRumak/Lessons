print()
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.


# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
def single_root_words(root_word, *other_words):
    # Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    same_words = []

    # При проверке наличия одного слова в составе другого стоит учесть, то регистр символов не должен влиять ни на что
    # ('Disablement' - 'Able') ('Able', 'able', 'AbLe' - все подходят)
    root_word_lower = root_word.lower()

    # При помощи цикла for переберите предполагаемо подходящие слова.
# Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
    for i in other_words:
        if root_word_lower in i.lower() or i.lower() in root_word_lower:
            same_words.append(i)
    return same_words


# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)







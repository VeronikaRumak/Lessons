print() # Отступ

# Вам необходимо решить задачу из реальной жизни:
# "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":

# На вход даны следующие даннные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразование множества в список.
# sorted() сортирует список в алфавитном порядке
students = list(sorted(students))

# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]

# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

# avarge_score_0 = sum(grades[0]) / len(grades[0])
# avarge_score_1 = sum(grades[1]) / len(grades[1])
# avarge_score_2 = sum(grades[2]) / len(grades[2])
# avarge_score_3 = sum(grades[3]) / len(grades[3])
# avarge_score_4 = sum(grades[4]) / len(grades[4])

# student_grades_set = {students[0]: avarge_score_0, students[1]: avarge_score_1, students[2]: avarge_score_2,
                      # students[3]: avarge_score_3, students[4]: avarge_score_4}

avarge_score = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
                sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]

student_grades_set = {students[0]: avarge_score[0], students[1]: avarge_score[1], students[2]: avarge_score[2],
                      students[3]: avarge_score[3], students[4]: avarge_score[4]}

print(student_grades_set)









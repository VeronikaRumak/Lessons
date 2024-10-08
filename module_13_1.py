import asyncio
import time


print()     # Отступ


# Необходимо сделать имитацию соревнований по поднятию шаров Атласа.

# Напишите асинхронную функцию start_strongman(name, power),
# где name - имя силача, power - его подъёмная мощность.
async def start_strongman(name, power):
    # Реализуйте следующую логику в функции:

    # Для каждого участника количество шаров одинаковое - 5.
    count_balls = 5

    # В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
    print(f'Силач {name} начал соревнования.')

    for ball in range(count_balls):
        # После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>'
        # с задержкой обратно пропорциональной его силе power.
        await asyncio.sleep(power)
        print(f'Силач {name} поднял шар номер {ball + 1}')

    # В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
    print(f'Силач {name} закончил соревнования.')


# Также напишите асинхронную функцию start_tournament,
# в которой создаются 3 задачи для функций start_strongman.
async def start_tournament():
    # Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
    # После поставьте каждую задачу в ожидание (await).
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


# Запустите асинхронную функцию start_tournament методом run.
asyncio.run(start_tournament())




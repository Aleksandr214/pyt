# задача 36
# Напишите функцию print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# По умолчанию номер столбца и строки = 9.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.

# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         answer = []
#         for j in range(1, num_columns + 1):
#             answer.append(str(operation(i, j)))
#         print("        ".join(answer))
 
 
# print_operation_table(lambda x, y: x * y)


def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x * y)

# ЗАДАЧА 34
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки.
# В ответе напишите Парам пам-пам, 
# если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести:
# Количество фраз должно быть больше одной!.

# На входе:

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:

# Парам пам-пам

def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')
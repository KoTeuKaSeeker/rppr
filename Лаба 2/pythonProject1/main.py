import numpy
import random

#Сохраняет матрицу в файл
def saveMatrix(a, M, N, f):
    for y in range(N):
        for x in range(M):
            f.write(str(a[y][x]) + " ")
        f.write('\n')
error = True
while error:
    try:
        M = int(input("Введите ширину таблицы: ")) #Количество столбцов матрицы
        N = int(input("Введите высоту таблицы: ")) #Количество строк матрицы
        error = False
    except:
        print("Введены неверные данные.")
        error = True

f = open("text.txt", "w") #Создание файла text.txt на запись

a = numpy.array([[random.randint(100, 999) for j in range(M)] for i in range(N)]) #Матрица, заполненная случайными числами от 10 до 99

f.write("Входная матрица: \n")
saveMatrix(a, M, N, f)

sum = 0

#Массив, в котором будет хранится последняя строка матрицы с долей столбцов
p = [0 for x in range(M)]

#Сумма матрицы
for x in range(M):
    for y in range(N):
        sum += a[y][x]

#Нахождение доли для каждого из столбцов
for x in range(M):
    p[x] = 0
    for y in range(N):
        p[x] += a[y][x]
    p[x] = round(p[x] / sum, 1)

#Вставление строчки в матрицу
a = numpy.vstack([a, p])

f.write('\n')
f.write("Обработанная матрица: \n")
saveMatrix(a, M, N + 1, f)

#Закрытие файла
f.close()
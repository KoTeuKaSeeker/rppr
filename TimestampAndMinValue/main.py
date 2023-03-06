import random


def task1(timestamp):
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1970

    daysTillNow = timestamp // (24 * 60 * 60)
    extraTime = timestamp % (24 * 60 * 60)
    extraDays = 0
    isLeap = False

    while daysTillNow >= 365:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            isLeap = True
            if daysTillNow < 366:
                break

            daysTillNow -= 366
        else:
            daysTillNow -= 365

        year += 1

    extraDays = daysTillNow + 1

    month = 0
    monthIndex = 0

    if isLeap:
        while True:
            if monthIndex == 1:
                if extraDays - 29 < 0:
                    break

                month += 1
                extraDays -= 29
            else:
                if extraDays - daysInMonth[monthIndex] < 0:
                    break

                month += 1
                extraDays -= daysInMonth[monthIndex]

            monthIndex += 1
    else:
        while True:
            if extraDays - daysInMonth[monthIndex] < 0:
                break

            month += 1
            extraDays -= daysInMonth[monthIndex]
            monthIndex += 1

    if extraDays > 0:
        month += 1
        day = extraDays
    else:
        if month == 2 and isLeap == 1:
            day = 29
        else:
            day = daysInMonth[month - 1]

    hours = extraTime // (60 * 60)
    minutes = (extraTime % (60 * 60)) // 60
    seconds = (extraTime % (60 * 60)) % 60

    print(str(year) + "-" + str(month) + "-" + str(day))
    print(str(hours) + ":" + str(minutes) + ":" + str(seconds))


def task2(ar):
    minim = ar[0]
    for i in range(len(ar)):
        if ar[i] < minim:
            minim = ar[i]
    return minim


if __name__ == "__main__":
    print("Задача 1")
    current_timestamp = 1678106747
    task1(current_timestamp)
    
    print("\Задача 2")
    ar = []
    for i in range(random.randint(5, 10)):
        ar.append(random.randint(-10, 10))

    print("Исходный список: " + str(ar) + "\n")

    print("Если массив не отсортирован")
    print("Минимальное число с сложностью O(n): " + str(task2(ar)) + "\n")

    print("Если массив отсортирован")
    ar = sorted(ar)
    print(ar)
    print("Минимальное число с сложностью O(1): " + str(ar[0]) + "\n")
import os, os.path

def parse_csv(path):
    got_data = {}
    with open(path, "r", encoding='utf-8') as raw_csv:
        for line in raw_csv:
            (idx, number, dateTime, plateNumber, carModel) = line.replace("\n", "").split(",")
            got_data.update({int(idx): {"number": int(number), "dateTime": dateTime, "plateNumber": plateNumber,"carModel": carModel}})
    return got_data

def sorted_by_carModel(d) -> dict:
    return dict(sorted(d.items(), key=lambda f: f[1]["carModel"]))

def sorted_by_number(d) -> dict:
    return dict(sorted(d.items(), key=lambda f: f[1]["number"]))

def select_more_than(d, value) -> dict:
    return dict((k, v) for k, v in d.items() if v["number"] > value)

def print_date(dict):
    for k, v in dict.items():
        print(
            f"Запись №{k}: номер = {v['number']}, дата и время = {v['dateTime']}, номерной знак = {v['plateNumber']}, марка автомобиля = {v['carModel']}")


def add_new_data(path, d, number, dateTime, plateNumber, carModel):
    with open(path, "w", encoding='utf-8') as f:
        for k, v in d.items():
            f.write(f"{k},{v['number']},{v['dateTime']},{v['plateNumber']},{v['carModel']}\n")
        f.write(f"{len(d)+1},{number},{dateTime},{plateNumber},{carModel}\n")
    d.update({len(d)+1: {"number": number, "dateTime": dateTime, "plateNumber": plateNumber, "carModel": carModel}})


def get_files_count_in_directory(path):
    (loc, dirs, files) = next(os.walk(path))
    return len(files)

dir = input("Введите дирректорию: ")
print(f"Количество файлов в папке: {get_files_count_in_directory(dir)}")

got_data = parse_csv("data.csv")
print("\nОтсортировано по имени: ")
print_date(sorted_by_carModel(got_data))
print("\nОтсортировано по номеру: ")
print_date(sorted_by_number(got_data))
print("\nТолько строки, у которых номер больше 500: ")
print_date(select_more_than(got_data, 500))

#Добавление новых данных
add_new_data("data.csv", got_data, 12341, "15.05.2021", "#43424", "Камаз")
add_new_data("data.csv", got_data, 423, "21.11.2023", "#4321", "УАЗ")
add_new_data("data.csv", got_data, 231, "11.02.2023", "#4241", "Нисан")
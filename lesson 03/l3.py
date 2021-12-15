import json
import csv

# Написать программу, которая выполняет следующее:

#    *Примечание: вычисление значений f1(x), f2(x), f3(x) реализовать в виде
#    отдельных Python функций(можно с применением лямбда-выражений). Из -
#    менение x в диапазоне от 5 до 90 с шагом 1 реализовать в виде генератора.

def generator():
    for i in range(5, 90):
        yield i

#    1) вычисляет значения функций f1(x)=x/(x+100) и f2(x)=1/x при изме -
#   нении x в диапазоне от 5 до 90 с шагом 1.
#    2) вычисляет значение функций f3(x)=20*(f1(x) + f2(x))/x.
#    3) представляет результат в виде словаря следующего вида*: {x1: [f1(x1),
#       f2(x1), f3(x1)], x2: [f1(x2), f2(x2), f3(x2)], ...};
def f1 (x):
    return x / (x+100)

def f2(x):
    if x!= 0:
        return 1/x
    else:
        return 0

def f3(x):
    return 20*(f1(x) + f2(x))/x

#    4) сохраняет результат вычислений в CSV-файл, заголовком(столбцами)
#    которого являются значения x, f1(x), f2(x), f3(x);

result_dict = {}
file_path_csv = "./my-result.csv"
file_path_json = "./my-result.json"
l_gen = generator()

with open(file_path_csv, "w") as file_object:
    my_csv_writer = csv.writer(file_object, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_csv_writer.writerow(["x", "f1(x)", "f2(x)", "f3(x)"])

    for i in l_gen:
        tmp = [f1(i), f2(i), f3(i)]
        result_dict[i] = tmp
        tmp.insert(0, i)
        my_csv_writer.writerow(tmp)

#    5) читает записанный CSV-файл и представляет результат в виде списка
#    [[x1, f1(x1), f2(x1), f3(x1)], [x2, f1(x2), f2(x2), f3(x2)], ...];
#csv_file = ''
result_dict = []
with open(file_path_csv, "r") as file_object:
    csv_file = csv.DictReader(file_object)
    
    for row in csv_file:
        result_dict.append(list(dict(row).values()))

#    6) сохраняет список[[x1, f1(x1), f2(x1), f3(x1)], [x2, f1(x2), f2(x2), f3(x2)], ...] в
#    JSON-файл.
with open(file_path_json, "w") as file_object:
    json.dump(result_dict, file_object, indent=2)


print('The program designed for the third lesson has been completed!')

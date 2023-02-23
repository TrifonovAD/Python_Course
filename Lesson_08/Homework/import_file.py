import os
import var
import ast

def import_data():
    # filename = 'test.txt'
    filename = input('Input file name: ') + '.txt' # Для проверки лежит файл test.txt и test2.txt
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f2:
            for item in f2:
                var.id += 1
                item = item.split()
                dictionary = {'ID': str(var.id), 'surname': item[0], 'name': item[1], 'patronymic': item[2], 'phone_number': item[3]}
                with open(var.file_base, 'a', encoding="utf-8") as f1:
                    f1.write(f'{dictionary}\n')
    else:
        print('File not found!')
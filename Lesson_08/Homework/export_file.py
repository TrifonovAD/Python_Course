import os
import var
import ast

def export_data():
    filename = input('Input file name: ') + '.txt'
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f1:
            with open(var.file_base, "r", encoding="utf-8") as f2:
                for i in f2:
                    res_dict = ast.literal_eval(i)
                    f1.write(f"{res_dict['ID']}. {res_dict['surname']} " 
                                f"{res_dict['name']} {res_dict['patronymic']}\n"
                                f"Номер телефона: {res_dict['phone_number']}\n\n")
    else:
        print('Error! File exist\n\n')
import var
import ast

def edit_record():
    flag = False
    tmp_list = []
    data = input("Input number record's, name or surname: ")
    with open(var.file_base, 'r', encoding="utf-8") as f:
        for i in f:
            res_dict = ast.literal_eval(i)
            if (data == res_dict.get('ID') 
                    or data == res_dict.get('surname') 
                    or data == res_dict.get('name')):
                print ('Input new data')
                res_dict['surname'] = input('surname: ')
                res_dict['name'] = input('name: ')
                res_dict['patronymic'] = input('patronymic: ')
                res_dict['phone_number'] = input('phone number: ')
                flag = True
            tmp_list.append(res_dict)
    with open(var.file_base, 'w', encoding="utf-8") as f:
        for i in tmp_list:
            print(i, file = f)
    print('The record was edited successfully!' if flag else 'Record not found!')
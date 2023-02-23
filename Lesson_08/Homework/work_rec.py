import var
import ast

def read_records():
    var.all_data=[]
    with open(var.file_base, encoding='utf-8') as f:
        for i in f:
            res_dict = ast.literal_eval(i)
            var.all_data.append(' '.join(list(res_dict.values())))
        if var.all_data:
            var.id = int(var.all_data[-1].split()[0])

def show_all_rec():
    read_records()
    if not var.all_data:
        print("Empty data\n")
    else:
        print('-'*50)
        print(*var.all_data, sep="\n")
        print('-'*50)


def add_record():
    array = ['surname', 'name', 'patronymic', 'phone_number']
    string = ''
    var.id += 1
    for  i in array:
        tmp = input(f'Enter {i} ')
        string += i + '=' + tmp + ';'
    string = 'ID' + '=' + str(var.id) + ';' + string
    string = string[:len(string)-2]
    dictionary = dict(subString.split("=") for subString in string.split(";"))
    with open(var.file_base, 'a', encoding="utf-8") as f:
        f.write(f'{dictionary}\n')
    print('\nNew record added succesful!\n')

def del_record():
    flag = False
    tmp_list = []
    count = 1
    data = input("Input number record's, name or surname: ")
    with open(var.file_base, 'r', encoding="utf-8") as f:
        for i in f:
            res_dict = ast.literal_eval(i)
            if (res_dict.get('ID') == data or
                res_dict.get('surname') == data or
                res_dict.get('name') == data
                ):
                flag = True
            else:
                res_dict['ID'] = str(count)
                tmp_list.append(res_dict)
                count += 1
                
    with open(var.file_base, 'w', encoding="utf-8") as f:
        for i in tmp_list:
            print(i, file = f)
    print('The record was deleted successfully!\n' if flag else 'Wrong number\n')
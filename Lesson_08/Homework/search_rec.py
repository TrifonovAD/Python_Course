import var

def search_record():
    find_text = input('Input search text: ').lower()
    flag = False
    for i in var.all_data:
        if find_text in i.lower():
            print(i)
            flag = True
    if not flag:
        print('Data not found!')
    print()
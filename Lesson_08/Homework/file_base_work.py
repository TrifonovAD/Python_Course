import os
import var


def open_phonebook():
    name = input('Input name file phonebook: ') + '.txt'
    if not os.path.exists(name):
        print('File not found\n\n')
    else:
        var.file_base = name

def create_phonebook():
    name = input('Input file name phonebook: ') + '.txt'
    if not os.path.exists(name):
        with open(name, "w", encoding="utf-8") as _:
            pass
        var.id = 0
        var.file_base = name
    else:
        print('Error! File exist\n\n')
  
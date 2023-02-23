import os
import var
import file_base_work as fbw
import work_rec as wr
import edit_rec as er
import search_rec as sr
import export_file as exf
import import_file as imf

def main_menu ():
    play = True
    while play:
        wr.read_records()
        answer = input(f"PHONE BOOK {var.file_base}\n"
                       "1. Create new phonebook\n"
                       "2. Open phonebook\n"
                       "3. Export phonebook\n"
                       "4. Import data\n"
                       "5. Show all records\n"
                       "6. Add new record\n"
                       "7. Edit record\n"
                       "8. Delete record\n"
                       "9. Search record\n"
                       "0. Exit\n\n"
                       )
        match answer:
            case "1":
                fbw.create_phonebook()
            case "2":
                fbw.open_phonebook()
            case "3":
                exf.export_data()
            case "4":
                imf.import_data()
            case "5":
                wr.show_all_rec()
            case "6":
                wr.add_record()
            case "7":
                er.edit_record()
            case "8":
                wr.del_record()
            case "9":
                sr.search_record()
            case "0":
                print('\nBye! Bye!')
                play = False
            case _:
                print("Try again!\n")
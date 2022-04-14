import write_file as wf
import write_in_json as wij

def hello_user(): 
    print("Добро пожаловать в телефонную книгу.")
    print("""Выберете команду: 
    * list - чтобы посмотреть список контактов.
    * find - найти контакт по имени
    * add  - добавить контакт
    * del  - удаление контакта
    * edit - изменение контакта 
    * exit - выход""")
    choice = input('Insert your choice')
    if choice == 'add':
        wf.write()
        wij.write_json(wij.Create_Dict())
    elif choice == 'del':
         wf.deleted_contact(wij.Create_Dict())
    elif choice == 'edit': 
        wf.edit_contact(wij.Create_Dict())                  
    else:
        print("Неизвестная команда")
# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def Create_List():
    '''This function generate list'''
    return ['qwe', 'qwe', 'asd', 'qwert', 'asd', 123, 123, 'qwert', 87]

def input_user():
    '''Function is returning inserted user's number or string'''
    return input('Insert string for searching')

def checking_insert(row):
    '''Function have one argument - what user inserted. Here argument will be checking, is it integer or string value. And return string or integer value'''
    if row.isdigit():
        return int(row)
    else:
        return row

def search_in_list(list, string):
    '''Function take two arguments. First is generated list and second 'string' was inserted by user'''
    times = 0
    for i in range(0, len(list)):
        if list[i] == string:
            times += 1
            if times == 2:
                return i
    if times == 0 or times == 1:
        return -1

def main():
    '''Main function is contain from all other function and give result to user in the console'''
    user_insert = checking_insert(input_user())
    result = search_in_list(Create_List(), user_insert)
    if result < 0:
        print("Your string doesn't have second entry in the list")
    else:
        print(f"Second entry was getting in position #{result}")

main()

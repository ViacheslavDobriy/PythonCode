import receive_data as rd

def write():
    inserted = rd.add_new()
    with open('contacts.txt', 'a') as data:
        data.write(f'{inserted[0]} {inserted[1]} {inserted[2]} {inserted[3]}')
        data.write('\n')
    return inserted

def edit_contact(dict):
    which_contact=input("Insert id: ")
    id = input("Insert new id: ")
    name = input("Insert new name: ")
    surname = input("Insert new surname: ")
    phone_number = int(input("Insert new phone number: "))
    for i in range(0, len(dict['ID'])):
        if dict['ID'][i] == which_contact:
            dict['ID'][i] = id
            dict['Name'][i] = name
            dict['Surname'][i] = surname
            dict['Phone Number'][i] = phone_number
        else:
            print('There is not this ID')
    print(dict)

def deleted_contact(dict):
    which_contact=input("Insert id: ")
    for i in range(0, len(dict['ID'])):
        if dict['ID'][i] == which_contact:
            dict['ID'][i] = ' '
            dict['Name'][i] = ' '
            dict['Surname'][i] = ' '
            dict['Phone Number'][i] = ' '
        else:
            print('There is not this ID')
    print(dict)
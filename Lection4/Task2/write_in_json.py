import json

def write_json(dict):
    with open('contacts.json', 'w') as data:
            json.dump(dict, data)

def Create_Dict():
    dict = {}
    constant = ['ID','Name', 'Surname', 'Phone Number']
    dict = {
        constant[0]:{
            constant[1]: [],
            constant[2]: [],
            constant[3]: []}
    }
    with open('contacts.txt', 'r') as data:
        for line in data:
            dict['ID']['Name'].append(line.split(' ')[1])
            dict['ID']['Surname'].append(line.split(' ')[2])
            dict['ID']['Phone Number'].append(line.split(' ')[3].replace('\n', ''))
        print(dict)
    return dict


        
        
    
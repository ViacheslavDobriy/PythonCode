# Определить, присутствует ли в заданном списке строк, некоторое число

list = ['cds', 'sldc', 'ugc', '7gcsid','201x','09k','1872g',' x8hccewc','98hc8cb7', '123']
searching = input('Input number what do u want find here')
print(list)
str = 'no'
for i in list:
    if i == searching:
        print(f'There is {searching} here')
        str = 'yes'
if str == 'no':
    print(f'There is no {searching} here')


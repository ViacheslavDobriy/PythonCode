# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

userRandom = int(input('Enter number from 1 to 7 for succesful exetution programm'))
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if 1 <= userRandom <= 7:
    count = 0
    while count < 7:
        if count+1 == userRandom:
            print('it is - {0}'.format(weekdays[count]))
        count = count + 1
else:
    print('Error. Enter correct number!')
# По заданному номеру дня недели вывести его название

listOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('Input the day number:')
userNumber = int(input())

count = 0
illegalNumber = True
while count < 7:
    if(count+1 == userNumber):
        print('{0} day of the week is {1}'.format(userNumber,listOfWeek[count]))
        illegalNumber = False
    count = count + 1
if(illegalNumber == True):
    print('You entered illegal value')


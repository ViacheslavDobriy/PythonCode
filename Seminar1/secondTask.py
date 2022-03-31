# Вывести на экран числа от -N до N


from Ask_User_To_Input import Input_User_Number


userNumber = Input_User_Number()
count = -userNumber
while(count<=userNumber):
    print('{0} '.format(count))
    count = count + 1


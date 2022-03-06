# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

numberOfQuarter = int(input('Enter the quarter number'))

if 0 < numberOfQuarter < 5:
    if numberOfQuarter == 1:
        print('Possible values: X > 0 and Y > 0')
    if numberOfQuarter == 2:
        print('Possible values: X < 0 and Y > 0')
    if numberOfQuarter == 3:
        print('Possible values: X < 0 and Y < 0')
    if numberOfQuarter == 4:
        print('Possible values: X > 0 and Y < 0')
else:
    print('Error! Enter legal number. Possible values: 1, 2, 3 and 4.')
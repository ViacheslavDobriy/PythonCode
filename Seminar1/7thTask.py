# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

coordinateX = int(input('Enter X coordinate'))
coordinateY = int(input('Enter Y coordinate'))

if coordinateX == coordinateY == 0:
    print('Point with coordinate ({},{}) is located at the point of contact of the X and Y axes'.format(coordinateX, coordinateY))
elif coordinateY == 0:
    if coordinateX > 0:
        print('Point with coordinate ({},{}) is located on the right side of the Y axes'.format(coordinateX, coordinateY))
    else:
        print('Point with coordinate ({},{}) is located on the left side of the Y axes'.format(coordinateX, coordinateY))
elif coordinateX == 0:
    if coordinateY > 0:
        print('Point with coordinate ({},{}) is located above the X-axes'.format(coordinateX, coordinateY))
    else:
        print('Point with coordinate ({},{}) is located under the X-axes'.format(coordinateX, coordinateY))
elif coordinateX > 0 and coordinateY > 0:
    print('The point with coordinate ({},{}) is located is in the quarter #1'.format(coordinateX, coordinateY))
elif coordinateX > 0 and coordinateY < 0:
    print('The point with coordinate ({},{}) is located is in the quarter #4'.format(coordinateX, coordinateY))
elif coordinateX < 0 and coordinateY > 0:
    print('The point with coordinate ({},{}) is located is in the quarter #2'.format(coordinateX, coordinateY))
elif coordinateX < 0 and coordinateY < 0:
    print('The point with coordinate ({},{}) is located is in the quarter #3'.format(coordinateX, coordinateY))
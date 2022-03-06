# Найти расстояние между двумя точками пространства

print('Enter coordinates of First point')
point1X = int(input('Enter X coordinate of point'))
point1Y = int(input('Enter Y coordinate of point'))
print('Enter coordinates of Second point')
point2X = int(input('Enter X coordinate of point'))
point2Y = int(input('Enter Y coordinate of point'))

long = point1X-point2X
width = point1Y-point2Y
distance = pow(long*long + width*width,0.5)
print('{} is distance between first point ({},{}) and second point ({},{})'.format(distance, point1X, point1Y, point2X, point2Y))
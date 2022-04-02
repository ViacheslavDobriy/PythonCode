# Найти корни квадратного уравнения Ax² + Bx + C = 0
# a) Математикой
# b) Используя дополнительные библиотеки*

user_rate_A = 0
while user_rate_A==0:
    user_rate_A = int(input('Insert ratio A'))
    user_rate_B = int(input('Insert ratio B'))
    user_rate_C = int(input('Insert ratio C'))
    if user_rate_A == 0:
        print('Insert correct ratio A')

print(f'Your equation looks like: {user_rate_A}x^2 + {user_rate_B}x + {user_rate_C} = 0')

def Discriminant(user_rate_A, user_rate_B, user_rate_C):
    result = user_rate_B**2 - 4*user_rate_A*user_rate_C
    return result

def The_Only_One_Solution(user_rate_A, user_rate_B):
    result = round(- user_rate_B / 2*user_rate_A, 2)
    return result

def The_Two_Solutions(user_rate_A, user_rate_B, discriminant):
    result = []
    x1 = round(- (user_rate_B + discriminant**0.5)/2*user_rate_A,3)
    x2 = round(- (user_rate_B - discriminant**0.5)/2*user_rate_A,3)
    result.append(x1)
    result.append(x2)
    return result

discriminant = Discriminant(user_rate_A, user_rate_B, user_rate_C)

if discriminant < 0:
    print('There is no solution because discriminant is negative')
elif discriminant == 0:
    print('There is only one solution:')
    print(f'{The_Only_One_Solution(user_rate_A, user_rate_B)} is solution of your equation')
else:
    print('There are two solutions of this equation')
    list_of_solutions = The_Two_Solutions(user_rate_A, user_rate_B, discriminant)
    print(f'x1 = {list_of_solutions[0]}, x2 = {list_of_solutions[1]}')

# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

#                                                  TRUTH TABLE
#   X   Y   Z   X \/ Y  X \/ Y \/ Z     no (X \/ Y \/ Z)    X   Y   Z   no X    no Y    no Z    no X /\ no Y    no X /\ no Y /\ no Z 
# | 0 | 0 | 0 |   0   |      0       |         1         || 0 | 0 | 0 |  1   |   1   |    1   |      1        |          1           |
# | 0 | 0 | 1 |   0   |      1       |         0         || 0 | 0 | 1 |  1   |   1   |    0   |      1        |          0           |
# | 0 | 1 | 0 |   1   |      1       |         0         || 0 | 1 | 0 |  1   |   0   |    1   |      0        |          0           |
# | 0 | 1 | 1 |   1   |      1       |         0         || 0 | 1 | 1 |  1   |   0   |    0   |      0        |          0           |
# | 1 | 0 | 0 |   1   |      1       |         0         || 1 | 0 | 0 |  0   |   1   |    1   |      0        |          0           |
# | 1 | 0 | 1 |   1   |      1       |         0         || 1 | 0 | 1 |  0   |   1   |    0   |      0        |          0           |
# | 1 | 1 | 0 |   1   |      1       |         0         || 1 | 1 | 0 |  0   |   0   |    1   |      0        |          0           |
# | 1 | 1 | 1 |   1   |      1       |         0         || 1 | 1 | 1 |  0   |   0   |    0   |      0        |          0           |

from asyncio.windows_events import NULL


print('Enter X, Y and Z')
UserX = int(input())
UserY = int(input())
UserZ = int(input())
leftSide = NULL
rightSide = NULL
if 0 <= UserX <=1 and 0 <= UserY <=1 and 0 <= UserZ <=1:
    if UserX + UserY + UserZ > 0:
        leftSide = 1
        print('{} \/ {} \/ {} = {}'.format(UserX, UserY, UserZ, leftSide))
        leftSide = 0
        print('NO {} \/ {} \/ {} = {}'.format(UserX, UserY, UserZ, leftSide))
    else:
        leftSide = 0
        print('{} \/ {} \/ {} = {}'.format(UserX, UserY, UserZ, leftSide))
        leftSide = 1
        print('NO({} \/ {} \/ {}) = {}'.format(UserX, UserY, UserZ, leftSide))
    if UserX==0 and UserY==0 and UserZ == 0:
        rightSide = 1
        print('NO {} /\ NO {} /\ NO {} = {}'.format(UserX, UserY, UserZ, rightSide))
    else:
        rightSide = 0
        print('NO{} /\ NO {} /\ NO {} = {}'.format(UserX, UserY, UserZ, rightSide))
    print('Left side is {}'.format(leftSide))
    print('Right side is {}'.format(rightSide))
    print('It means the logical statement is true')
else:
    print('Error, enter the legal values for X, Y and Z')
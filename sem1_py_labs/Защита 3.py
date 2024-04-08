from math import *

# Начинаем программу с ввода координат точек треугольника
print('Введите координаты x и y точки A через пробел:', end=' ')
Ax,Ay = map(int, input().split())
print('Введите координаты x и y точки B через пробел:', end=' ')
Bx,By = map(int, input().split())
print('Введите координаты x и y точки C через пробел:', end=' ')
Cx,Cy = map(int, input().split())

# Далее производим расчёт длин сторон треугольнка ABC
AB = sqrt(((Ax-Bx)**2)+((Ay-By)**2))
BC = sqrt(((Bx-Cx)**2)+((By-Cy)**2))
CA = sqrt(((Cx-Ax)**2)+((Cy-Ay)**2))

# Узнаём, существует ли треуголбник и является ли он равнобедренным
if AB + BC > CA and CA + BC > AB and AB + CA > BC:

    if ((AB==BC and CA!=BC and CA!=AB)
        or (CA==BC and AB!=BC and CA!=AB) or (CA==AB and CA!=BC and BC!=AB)):
        print('Треугольник равнобедренный')

    else:
        print('Треугольник не является равнобедренным')

else:
    print('Такого треугольника не сущетсвует')

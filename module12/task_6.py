print('Задача 6. Монетка')

# Практиканту дали задание
# найти старую металлическую монетку по заданным координатам.
#
# Металлоискатель сканирует местность вокруг пользователя
# и при обнаружении/отсутствии металла прибор отображает на экране соответствующее сообщение.
#
#
# Даны два действительных числа x и y.
# Напишите функцию, которая проверяет,
# принадлежит ли точка с координатами (x,y) заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату,
# выведите сообщение “Монетка где-то рядом”,
# иначе выведите сообщение “Монетки в области нет”.
#
# На рисунке сетка проведена с шагом 1.
#
# P.S - Смотри рисунок на сайте :)
#         ^
#         |
#        *|*
# ========+=======>
#        *|*
#         |


def scanner(x: int, y: int):
    if (-1 <= x <= 1) and (-1 <= y <= 1):
        return "Монетка где-то рядом"
    else:
        return "Монетки в области нет"


if __name__ == '__main__':
    x = int(input("Введите координату X: "))
    y = int(input("Введите координату Y: "))
    print(scanner(x, y))

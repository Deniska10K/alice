print('Задача 8. НОД')

# Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def nod(x: int, y: int):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


if __name__ == '__main__':
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    print(f"Наименьший общий делитель: {nod(x, y)}")

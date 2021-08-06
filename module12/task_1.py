print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15


def summa_n(n: int):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa


if __name__ == '__main__':
    n = int(input("Введите число: "))
    print(f"Я знаю, что сумма чисел от 1 до {n} равна {summa_n(n)}")

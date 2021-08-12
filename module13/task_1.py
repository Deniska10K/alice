print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
#
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
#
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
#
# Пример 1:
#
# Введите число: 92345
#
# Формат плавающей точки: x = 9.2345 * 10 ** 4
#
# Пример 2:
#
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3


def float_converter(n):
    k = 0
    if n < 1:
        while n < 1:
            n = round(n * 10, len(str(n)))
            k -= 1
    elif n >= 10:
        while n >= 10:
            n = round(n / 10, len(str(n)))
            k += 1
    return f"Формат плавающей точки: x = {n} * 10 ** {k}"


if __name__ == '__main__':
    print(float_converter(float(input("Введите число: "))))

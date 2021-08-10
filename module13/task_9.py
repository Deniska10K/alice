print('Задача 9. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709


def the_sum_of_the_series(precision, x):
    now = 1
    prev = 0
    fact_n = 1
    x_n = 1
    i = 0
    while abs(now - prev) > precision:
        prev = now
        x_n *= x * x
        i += 1
        fact_n *= 2 * i * (2 * i - 1)
        now += (-1 if i % 2 else 1) * x_n / fact_n
    return now

print(f"Сумма ряда =  {the_sum_of_the_series(float(input('Введите точность: ')), float(input('Введите x: ')))}")

print('Задача 5. Число Эйлера')


# Напишите программу, которая находит сумму  ряда с точностью до 1e-5.

# P.S: Формулу смотреть на сайте :)

# Пример:

# Точность: 1e-20
# Результат: 2.7182818284590455

import math


precision = float(input("Точность: "))
result = 0
i = 0
members = 1

while members > precision:
    members = 1 / math.factorial(i)
    result += members
    i += 1
print(f"Результат: {result}")

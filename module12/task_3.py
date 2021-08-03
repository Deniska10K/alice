print('Задача 3. Апгрейд калькулятора')

# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
#
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
#
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
#
# Напишите программу,
# которая спрашивает у пользователя число и действие,
# которое нужно с ним сделать:
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру.
#
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.


def calculator():
    n = input("\nВведите число: ")
    action = input("Какое действие нужно произвести?\n"
                   "1) Вывести сумму цифр\n"
                   "2) Вывести минимальную цифру\n"
                   "3) Вывести максимальную цифру\n"
                   "Выберите действие: ")
    if action == '1':
        print(f"Сумма цифр числа {n} = {digits_sum(n)}")
    if action == '2':
        print(f"Минимальная цифра числа {n} = {min_digit(n)}")
    if action == '3':
        print(f"Максимальная цифра числа {n} = {max_digit(n)}")


def digits_sum(n: str):
    return sum((int(i) for i in n))


def min_digit(n: str):
    return min((int(i) for i in n))


def max_digit(n: str):
    return max((int(i) for i in n))


if __name__ == '__main__':
    while True:
        calculator()

print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225


def rotate_digit(n):
    n = str(n)
    while n[-1] == '0':
        n = n[:-1]
    return int(n[::-1])


if __name__ == '__main__':
    digit1 = input("Введите первое число: ")
    digit2 = input("Введите второе число: ")

    digit1_rotated = rotate_digit(digit1)
    digit2_rotated = rotate_digit(digit2)
    summa = digit1_rotated + digit2_rotated
    summa_rotated = rotate_digit(summa)

    print()
    print(f"Первое число наоборот: {digit1_rotated}")
    print(f"Второе число наоборот: {digit2_rotated}")
    print()
    print(f"Сумма: {summa}")
    print(f"Сумма наоборот: {summa_rotated}")

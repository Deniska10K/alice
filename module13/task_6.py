print('Задача 6. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.


def digit_replacer(digit1: str, digit2: str):
    if len(digit1) >= 3 and len(digit2) >= 4:
        digit1 = f"{digit1[-1]}{digit1[1:-1]}{digit1[0]}"
        digit2 = f"{digit2[-1]}{digit2[1:-1]}{digit2[0]}"
    else:
        return
    return int(digit1), int(digit2)


if __name__ == '__main__':
    first_n = input("Введите первое число: ")
    second_n = input("Введите второе число: ")
    value = None
    if digit_replacer(first_n, second_n):
        first_n_modified, second_n_modified = digit_replacer(first_n, second_n)
        value = first_n_modified + second_n_modified

    print((f"Измененное первое число: {first_n_modified}\n"
           f"Измененное второе число: {second_n_modified}\n"
           f"Сумма измененных чисел равна: {value}") if value else "Ошибка")
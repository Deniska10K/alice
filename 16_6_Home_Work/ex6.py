first_list = [int(x) for x in input("Введите три числа через пробел: ").split()]
second_list = [int(x) for x in input("Введите семь чисел через пробел: ").split()]

print(f"Первый список: {first_list}\nВторой список: {second_list}")

first_list.extend(second_list)
first_list = list(set(first_list))

print(f"Новый первый список с уникальными элементами: {first_list}")
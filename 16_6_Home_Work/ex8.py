index = 0
peoples = [x for x in range(1, int(input("Кол-во человек: "))+1)]
number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number} человек\n")

while len(peoples) > 1:
    print(f"Текущий круг людей: {peoples}")
    print(f"Начало счёта с номера {peoples[index]}")
    index = (index + number - 1) % len(peoples)

    if peoples[index] == peoples[-1]:
        print(f"Выбывает человек под номером {peoples[index]}\n")
        peoples.pop(index)
        index = 0

    else:
        print(f"Выбывает человек под номером {peoples[index]}\n")
        peoples.pop(index)

print(f"Остался игрок под номером {peoples[0]}")
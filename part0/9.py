total_milk = 0
string = input("Введите строку: ")

for index, item in enumerate(string):
    if item == "b":
        total_milk += (index + 1) * 2

print(f"Всего произведено молока: {total_milk}")

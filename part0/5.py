coords = [8, 10]

while True:
    print(f"[Программа]: Марсоход находится на позиции {coords[0]}, {coords[1]}, введите команду:")
    key = input("[Оператор]: ")
    if key == 'W' and coords[1] < 20:
        coords[1] += 1
    if key == 'A' and coords[0] > 0:
        coords[0] -= 1
    if key == 'S' and coords[1] > 0:
        coords[1] -= 1
    if key == 'D' and coords[0] < 15:
        coords[0] += 1

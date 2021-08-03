while True:
    x = int(input('Введите число: '))
    if x in [2, 4, 8, 16, 32, 64]:
        print("division by zero")
    else:
        print("Результат:    ", round(((x - 1) * (x - 3) * (x - 7) * (x - 15) * (x - 31) * (x - 63)) /
                                      ((x - 2) * (x - 4) * (x - 8) * (x - 16) * (x - 32) * (x - 64)), 2))

n = int(input("Введите диагональ квадрата: "))

for i in range(n):
    for ii in range(n):
        if i == ii or ii == (n - i - 1):
            print('^', end='')
        else:
            print(' ', end='')
    print()

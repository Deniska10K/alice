n = int(input("Введите число: "))

for i in range(n):
    print(f"{' ' * (n - 1 - i)}{'#' * ((i + 1) * 2 - 1)}{' ' * (n - 1 - i)}")

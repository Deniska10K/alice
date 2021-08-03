n = int(input("Введите колличество уровней пирамиды: "))
tab = '\t'
d = 1

for i in range(n):
    print(f"{tab * (n - (i + 1))}", end='')
    for _ in range(i + 1):
        print(f"{d}{tab * 2}", end='')
        d += 2
    print()

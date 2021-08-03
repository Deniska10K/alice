n = int(input("Введите число: "))
value = 0

for i in range(1, n + 1):
    fact = 1
    for ii in range(1, i + 1):
        fact *= ii
    value += fact

print(value)

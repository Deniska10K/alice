digits_sum = 0
old_sum = 0
print('Чтобы остановить вычисление, введите "0"')

while True:
    n = input("Введите число: ")
    if n != '0':
        for i in n:
            digits_sum += int(i)
        if digits_sum > old_sum:
            old_sum = digits_sum
            digits_sum = 0
    else:
        print(old_sum)
        quit()

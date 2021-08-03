import math
n = int(input("Введите кол-во чисел: "))

for _ in range(n):
    num = float(input("Введите число: "))
    if num > 0:
        num = math.ceil(num)
        print(f"x = {num}\tlog(x) = {math.log(num)}")
    else:
        num = math.floor(num)
        print(f"x = {num}\texp(x) = {math.exp(num)}")

n = int(input("Введите длинну последовательности: "))
prime_numbers = 0


def is_prime(n):
    is_prime = True
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            is_prime = False
            break
    return is_prime


for num in range(2, n + 1):
    if is_prime(num):
        prime_numbers += 1

print(f"В последовательности чисел до {n} ==> {prime_numbers} простых чисел")

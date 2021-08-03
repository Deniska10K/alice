for i in range(10, 101):
    first_digit, second_digit = int(str(i)[0]), int(str(i)[1])
    if first_digit * second_digit * 3 == i:
        print(i)

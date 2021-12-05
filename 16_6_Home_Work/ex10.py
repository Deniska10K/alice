numbers_count = int(input("Кол-во чисел: "))
numbers_list = [int(input("Число: ")) for _ in range(numbers_count)]
print("Последовательность:", *numbers_list)

# palindrome = True if (numbers_list == numbers_list[::-1]) else False
#
# print(palindrome)

# while numbers_list[:(numbers_count // 2 + 1)] != numbers_list[(numbers_count // 2 + 1):]:
print(numbers_list[:(numbers_count // 2)], numbers_list[(numbers_count // 2):])

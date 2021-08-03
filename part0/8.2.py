colon_len = int(input("Введите длинну колонтикула: "))
count = int(input("Введите колличество знаков восклицания: "))

print(((colon_len - count) // 2) * '~' + count * '!' + ((colon_len - count) // 2) * '~')

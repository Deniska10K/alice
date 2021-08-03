string = input('Введите  строку: ')
count, max_count = 1, 1

for item in range(1, len(string)):
    if string[item - 1] == string[item] == 's':
        count += 1
    else:
        count = 1
    if count > max_count:
        max_count = count

print(max_count)

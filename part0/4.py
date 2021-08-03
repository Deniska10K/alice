# row = int(input('Введите кол-во рядов: '))
# seats_in_a_row = int(input('Введите кол-во сидений в ряду: '))
# space = int(input('Введите кол-во метров между рядами: '))
#
# for i in range(row):
#     print('=' * seats_in_a_row, '*' * space, '=' * seats_in_a_row)
#
#
row = int(input('Введите кол-во рядов: '))
col = int(input('Введите кол-во сидений в ряду: '))
margin = int(input('Введите кол-во метров между рядами: '))
for i in range(row):
    rows = f"{'=' * col} {'*' * margin} {'=' * col}"
    print(rows)

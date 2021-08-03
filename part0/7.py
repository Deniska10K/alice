educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы: '))
costs = 0
income = 0

for i in range(10):
    income += educational_grant
    costs += expenses
    expenses *= 1.03
    outcome = costs - income

print('У родителей попросить:', round(outcome, 2))

count_of_friends = int(input("Кол-во друзей: "))
arrears = int(input("Долговых расписок: "))
friends = {f"{x}": 0 for x in range(1, count_of_friends + 1)}

def debt(index):
    print(f"\n{index} расписка")
    to_whom = input("Кому: ")
    from_whom = input("От кого: ")
    value = int(input("Сколько: "))
    friends[from_whom] += value
    friends[to_whom] -= value

for i in range(arrears):
    debt(i+1)

print("Баланс друзей:")
for friend in friends:
    print(f"{friend}: {friends[friend]}")
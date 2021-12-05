rollers_sizes = []
foot_sizes = []
people_with_rollers = 0

count_of_rollers = int(input("Кол-во коньков: "))
for i in range(count_of_rollers):
    rollers_sizes.append(int(input(f"Размер {i+1} пары: ")))
rollers_sizes.sort()

people_count = int(input("\nКол-во людей: "))
for i in range(people_count):
    foot_sizes.append(int(input(f"Размер ноги {i + 1} человека: ")))
foot_sizes.sort()

rollers_sizes = list(filter(lambda x: x >= min(foot_sizes), rollers_sizes))

while True:
    try:
        foot_size = foot_sizes[0]
        rollers_size = rollers_sizes[0]
        if foot_size <= rollers_size:
            people_with_rollers += 1
        rollers_sizes.pop(0)
        foot_sizes.pop(0)
    except:
        break

print(f"Наибольшее кол-во людей, которые могут взять ролики: {people_with_rollers}")

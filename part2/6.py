minimum = int(input("Ввод:\nНижняя граница: "))
maximum = int(input("Верхняя граница: "))
step = int(input("Шаг: "))

print(f"\nВывод:\nC\tF")
for c in range(minimum, maximum, step):
    print(f"{c}\t{int(32 + c * 1.8)}")
print(f"{maximum}\t{int(32 + maximum * 1.8)}")
width = int(input("Введите ширину: "))
height = int(input("Введите высоту: "))

print(f"|{'-' * (width - 2)}|")
for i in range(height - 2):
    print(f"|{' ' * (width - 2)}|")
print(f"|{'-' * (width - 2)}|")

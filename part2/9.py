a = int(input("Введите коэффициент A: "))
b = int(input("Введите коэффициент B: "))
c = int(input("Введите коэффициент C: "))
print()

equations_root_1 = None
equations_root_2 = None
discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    equations_root_1 = (-b - discriminant ** .5) / (2 * a)
    equations_root_2 = (-b + discriminant ** .5) / (2 * a)
    print(f"Первый корень уравнения: {min(equations_root_1, equations_root_2)}\n"
          f"Второй корень уравнения: {max(equations_root_1, equations_root_2)}")
elif discriminant == 0:
    equations_root_1 = -b / (2 * a)
    print(f"Первый корень уравнения: {equations_root_1}")

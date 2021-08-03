import math

horse_coords = []
point_coords = []

print("Введите местоположение коня:")
horse_coords.append(math.trunc(float(input()) * 10))
horse_coords.append(math.trunc(float(input()) * 10))

print("Введите местоположение точки на доске:")
point_coords.append(math.trunc(float(input()) * 10))
point_coords.append(math.trunc(float(input()) * 10))

print(f"Конь в клетке ({horse_coords[0]}, {horse_coords[1]}). Точка в клетке ({point_coords[0]}, {point_coords[1]}).")

delta1, delta2 = abs(point_coords[0] - horse_coords[0]), abs(point_coords[1] - horse_coords[1])

if ((delta1 == 1) and (delta2 == 2)) or ((delta1 == 2) and (delta2 == 1)):
    print("Да, конь может ходить в эту точку.")
else:
    print("Нет, конь не может ходить в эту точку.")

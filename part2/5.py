r = float(input("Введите радиус случайной планеты: "))
earth_volume = 10.8321 * 10 ** 11
planet_volume = 4 / 3 * 3.141592653589793 * r ** 3

if earth_volume > planet_volume:
    print(f"Объем планеты Земля больше в {round(earth_volume / planet_volume, 3)} раз")
else:
    print(f"Объем планеты Земля меньше в (1/{round(earth_volume / planet_volume, 3)}) ="
          f" {round(1 / (earth_volume / planet_volume), 3)} раз")

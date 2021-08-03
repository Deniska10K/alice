euro = int(input("Стоимость в EUR: "))
print(f"Стоимость в USD: {euro * 1.25}\nСтоимость в RUB: {round(euro * 1.25 * 60.87, 2)}")
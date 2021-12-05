guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

def main():
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришёл или ушёл? ")

    if action == 'Пора спать':
        print("Вечеринка закончилась, все легли спать.")
        exit()

    guest_name = input("Имя гостя: ")

    if action == 'пришёл':
        if len(guests) == 6:
            print(f"Прости, {guest_name}, но мест нет.\n")
        else:
            guests.append(guest_name)
            print(f"Привет, {guest_name}!\n")

    elif action == 'ушёл':
        guests.remove(guest_name)
        print(f"Пока, {guest_name}!\n")

if __name__ == '__main__':
    while True:
        main()

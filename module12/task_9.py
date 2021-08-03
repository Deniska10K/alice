print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random


def rock_paper_scissors():
    print("Вы выбрали игру «Камень, ножницы, бумага»")
    while True:
        user_action = input("\nВыберите ход: (камень / ножницы / бумага)\nИли напишите 'exit' чтобы выйти из игры\n"
                            "Ваш выбор: ")
        if user_action == 'exit':
            main_menu()
        else:
            game_action = random.choice(("камень", "ножницы", "бумага"))

            if game_action == "камень":
                if user_action == "камень":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Ничья")
                elif user_action == "ножницы":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Поражение")
                elif user_action == "бумага":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Победа")

            elif game_action == "ножницы":
                if user_action == "камень":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Победа")
                elif user_action == "ножницы":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Ничья")
                elif user_action == "бумага":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Поражение")

            elif game_action == "бумага":
                if user_action == "камень":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Поражение")
                elif user_action == "ножницы":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Победа")
                elif user_action == "бумага":
                    print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> Ничья")


def guess_the_number():
    print("\nВы выбрали игру «Угадай число»")
    while True:
        user_action = int(input("Введите число: (от 0 до 100)\nИли напишите 'exit' чтобы выйти из игры\nВаш выбор: "))
        if user_action == 'exit':
            main_menu()
        else:
            game_action = str(random.randrange(0, 101))
            while user_action != game_action:
                user_action = input("Вы не угадали, попробуйте снова: ")
                if user_action == 'exit':
                    main_menu()
            else:
                print("Вы победили!")
                end_action = input("\nСыграем еще?\n1) Да\n2) Нет\nВаш выбор: ")
                if end_action == '1':
                    guess_the_number()
                else:
                    main_menu()


def main_menu():
    game = input("\nВыберите игру:\n"
                 "1) Камень, ножницы, бумага\n"
                 "2) Угадай число\n"
                 "Ваш выбор: ")
    if game == '1':
        rock_paper_scissors()
    elif game == '2':
        guess_the_number()


if __name__ == '__main__':
    main_menu()

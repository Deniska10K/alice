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
    winning = {"камень": "ножницы", "бумага": "камень", "ножницы": "бумага"}
    while True:
        user_action = input("\nВыберите ход: (камень / ножницы / бумага)\nИли напишите 'exit' чтобы выйти из игры\n"
                            "Ваш выбор: ")
        if user_action == 'exit':
            return
        else:
            game_action = random.choice(("камень", "ножницы", "бумага"))
            if game_action == user_action:
                result = "Ничья"
            elif winning[game_action] == user_action:
                result = "Поражение"
            else:
                result = "Победа"
            print(f"Вы выбрали {user_action}, игра выбрала {game_action} ==> {result}")


def guess_the_number():
    print("\nВы выбрали игру «Угадай число»")
    while True:
        user_action = int(input("Введите число: (от 0 до 100)\nИли напишите 'exit' чтобы выйти из игры\nВаш выбор: "))
        if user_action == 'exit':
            return
        else:
            game_action = str(random.randrange(0, 101))
            while user_action != game_action:
                user_action = input("Вы не угадали, попробуйте снова: ")
                if user_action == 'exit':
                    return
            else:
                print("Вы победили!")
                end_action = input("\nСыграем еще?\n1) Да\n2) Нет\nВаш выбор: ")
                if end_action == '1':
                    guess_the_number()
                else:
                    return


def main_menu():
    while True:
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

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
violator_songs_dict = {x[0]: x[1] for x in violator_songs}
total_time = 0

count_of_songs = int(input("Сколько песен выбрать? "))
for i in range(count_of_songs):
    song_name = input(f"Название {i+1} песни: ")
    total_time += violator_songs_dict[song_name]

print(f"Общее время звучания песен: {format(total_time, '.2f')} минут")
file_size = int(input("Размер файла? "))
connection_speed = int(input("Скорость загрузки? "))
downloaded = 0

for i in range((file_size // connection_speed) + 1):
    downloaded += connection_speed
    if downloaded < file_size:
        print(f"Секунда {i + 1}: Загружено {downloaded} из {file_size} ({int(downloaded / file_size * 100)}%)")
    elif downloaded > file_size:
        print(f"Секунда {i + 1}: Загружено {file_size} из {file_size} (100%)")

from random import *
import json
films = []


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Наша библиотека была успешно сохранена в файле films.json")


def load():
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Наша библиотека была успешно загруженна")


try:
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Наша библиотека была успешно загруженна")
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта Барбара")


while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Привет, я бот-фильмотека, начал выполнять все Ваши пожелания. Что прекажите, О ВЕЛИКИЙ?")
    elif command == "/stop":
        print("Я бот-фильмотека и я завершил свою работу в Вашей реалии. Приходите еще, я буду Вам максимально рад!")
        break
    elif command == "/all":
        print("Вот текущий список фильмов")
        print(films)
    elif command == "/add":
        f = input("Введите название фильма ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию!")
    elif command == "/delete":
        f = input("Введите название фильма, который нужно удалить ")
        if f in films:
            films.remove(f)
            print("Фильм был успешно удален из коллекции!")
        else:
            print("Этого фильма нет в нашем списке!")
    elif command == "/random":
        # rnd = randint(0, len(films)-1)
        # print("Фильм на вечерок: " + films[rnd])
        print("Фильм на вечерок: " + choices(films))
    elif command == "/save":
        save()
    elif command == "/load":
        with open("films.json", "r", encoding="utf-8") as fh:
            films = json.load(fh)
        print("Наша библиотека была успешно загруженна")

    elif command == "/help":
        print("/start - запуск бота")
        print("/stop - остановка бота")
        print("/all - вывод полного списка фильмов")
        print("/add - добавление фильма в список")
        print("/delete - удаление фильма из списка")
        print("/random - случайный фильм из нашего списка")
        print("/save - сохранение списка фильмов")
        print("/load - загрузка сохраненного списка фильмов")
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help")

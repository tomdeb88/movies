import random
import datetime

current_date = datetime.datetime.today().strftime("%d.%m.%Y")


class Films:
    films_series = []

    def __init__(self, title, released, type, views):
        self.title = title
        self.released = released
        self.type = type
        self.views = views
        self.films_series.append(self)

    def __str__(self):
        return f"'{self.title}' ({self.released})"

    def play(self):
        self.views += 1


class Series(Films):
    def __init__(self, title, released, type, views, series_num, season_num):
        super().__init__(title, released, type, views)
        if series_num < 10:
            self.series_num = f"0{series_num}"
        else:
            self.series_num = series_num
        if season_num < 10:
            self.season_num = f"0{season_num}"
        else:
            self.season_num = season_num

    def __str__(self):
        return f"'{self.title} S{self.season_num}E{self.series_num}'"


def get_series():
    list = []
    for obj in Films.films_series:
        if isinstance(obj, Series):
            list.append(obj)
    by_name = sorted(list, key=lambda obj: obj.title)
    return by_name


def get_movies():
    list = []
    for obj in Films.films_series:
        if not isinstance(obj, Series):
            list.append(obj)
    by_name = sorted(list, key=lambda obj: obj.title)
    return by_name


# for i in get_series():
#     print(i)


def search(name):
    for obj in Films.films_series:
        if name in obj.title:
            print("We've got it")
            return obj

    print("We do not have this position")


# search("Django")


def generate_views():
    random_position = Films.films_series[random.randint(0, len(Films.films_series) - 1)]
    random_position.views += random.randint(1, 100)


def multiplying_views():
    for i in range(10):
        generate_views()


def top_titles(index):
    views_sorted = sorted(Films.films_series, key=lambda obj: obj.views, reverse=True)[
        :index
    ]

    return views_sorted


print("Biblioteka filmow")

film1 = Films("RamboBambo", "1988", "comedy", 457)
film2 = Films("Django", "2000", "thriller", 800)
film3 = Films("Braveheart", "1988", "historic", 998)
film4 = Films("Zombie", "1906", "historic", 546)
serial1 = Series("Office", "2000", "horror", 700, 15, 45)
serial2 = Series("Californication", "2004", "Comedy", 1478, 1, 12)
serial3 = Series("Vikings", "2015", "historic", 500, 3, 8)
serial4 = Series("Klan", "1999", "horror", 124, 45, 23)

generate_views()

print(f"Najpopularniejsze filmy i seriale dnia {current_date}:")

for i in top_titles(3):
    print(i.title, i.views)

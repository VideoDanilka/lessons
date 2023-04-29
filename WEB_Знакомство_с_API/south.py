import requests
import json


# Запрос координат города по его названию
def get_coordinates(city):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "format": "json",
        "geocode": city
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        pos = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"][
            "pos"]
        lon, lat = map(float, pos.split())
        return lat, lon
    else:
        return None


# Получение списка городов от пользователя
cities = input("Введите названия городов через запятую: ").split(",")

# Поиск самого южного города
min_lat = float("inf")
southernmost_city = None
for city in cities:
    coordinates = get_coordinates(city.strip())
    if coordinates is not None:
        lat, lon = coordinates
        if lat < min_lat:
            min_lat = lat
            southernmost_city = city.strip()

# Вывод результата
if southernmost_city is not None:
    print("Самый южный город: ", southernmost_city)
else:
    print("Не удалось определить координаты городов.")

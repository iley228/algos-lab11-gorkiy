import requests
def search_movies(title):
    params = {
        "apikey": API_KEY,
        "s": title,
        "r": "json"
    }
    try:
        response = requests.get(API_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "True":
            return data.get("Search", [])
        else:
            print(f"Ошибка: {data.get('Error', 'Фильмы не найдены')}")
            return []
    except requests.RequestException:
        print("Ошибка: не удалось получить данные с сервера OMDb API.")
        return []

def main():
    while True:
        user_input = input("Введите название фильма (или напишите 'выход' чтобы завершить работу): ").strip()
        if user_input.lower() == "выход":
            print("Завершение работы...")
            break
        if not user_input:
            continue
        movies = search_movies(user_input)
        for movie in movies:
            title = movie.get("Title", "N/A")
            year = movie.get("Year", "N/A")
            mtype = movie.get("Type", "N/A")
            print(f"Название: {title}, Год: {year}, Тип: {mtype}")

if __name__ == "__main__":
    main()

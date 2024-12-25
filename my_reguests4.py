import requests

headers = {
    "User-Agent": "MyApp/1.0"
}

response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)

if response.status_code == 200:
    print("Получены данные с пользовательским заголовком:")
    posts = response.json()
    print(posts[:5])
else:
    print("Ошибка при запросе:", response.status_code)

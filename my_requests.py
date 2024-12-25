import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    print("Запрос выполнен успешно!")

    posts = response.json()

    for post in posts[:5]:
        print(f"ID: {post['id']}, Title: {post['title']}, Body: {post['body']}")
else:
    print("Ошибка запроса:", response.status_code)


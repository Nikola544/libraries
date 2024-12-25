import requests

params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

if response.status_code == 200:
    print("Получены данные с параметром userId=1:")
    posts = response.json()
    for post in posts:
        print(f"ID: {post['id']}, Title: {post['title']}")

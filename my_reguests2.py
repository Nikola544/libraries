import requests

data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

if response.status_code == 201:
    print("Данные успешно отправлены!")
    print(response.json())
else:
    print("Ошибка при отправке данных:", response.status_code)

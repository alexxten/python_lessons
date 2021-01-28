import requests

response = requests.get(url='https://jsonplaceholder.typicode.com/todos/1')
print(response)
print(response.json())

response2 = requests.post(
    url="https://jsonplaceholder.typicode.com/posts",
    json={
        "userId": 1,
        "id": 1,
        "title": "hello world",
        "body": "343355"
    },
)
print(response2.json())  # ответ в формате json
print(response2.status_code)  # статус запроса



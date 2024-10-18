import requests

response = requests.get('https://api.github.com/events')
print(response.status_code)  # Статус ответа
print(response.text)  # Текст ответа
print(response.encoding)  # Кодировка ответа
print(response.content)  # Содержание ответа байт
print(response.json())  # Содержание ответа JSON
response = requests.get('https://api.github.com/events', stream=True)
print(response.raw)  # Содержание ответа байт

# работа с заголовками
print(response.headers)
print(response.headers['content-type'])

# работа с методом POST
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.text)

# работа с cookies
response = requests.get('https://github.com')
print(list(response.cookies))

try:
    response = requests.get('https://api.github.com/events', timeout=1)
except requests.exceptions.Timeout:
    print('timeout')

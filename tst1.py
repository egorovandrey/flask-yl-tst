from requests import get

print(get('http://127.0.0.1/api/v2/news').json())

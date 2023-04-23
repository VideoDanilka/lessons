import requests

url = input()
port = input()
a = input()
b = input()

params = {'a': a, 'b': b}
response = requests.get(f'{url}:{port}', params=params)

data = response.json()
result = sorted(data['result'])
check = data['check']

print(*result)
print(check)

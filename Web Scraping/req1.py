import requests
url = "https://meet.google.com/"
response = requests.get(url)
print(response)
print(response.content)
print(response.headers)
print(response.text)
print(response.json)
print(response.headers['Content-Type'])
print(response.links)
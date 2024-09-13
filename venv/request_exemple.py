import requests

url = "https://www.kostrub.online/2020/05/osnovni-roli-v-it.html"

response = requests.get(url)

print(response.text)
import requests

url = "https://vpu29.lviv.ua/wp-content/uploads/2023/11/%D0%9F%D0%9F-2024-%D0%92%D0%9F%D0%A329.pdf"

response = requests.get(url)

print(response.text)
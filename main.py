import requests
import streamlit

api_key = "0tzSXf5cJWNk5IujXy3LDIUKPgbOnpcwsbhVvei2"
url = ("https://api.nasa.gov/planetary/apod?"
       f"{api_key}")

response = requests.get(url)
content = response.json()

#Заголовок
streamlit.header(content["title"])

#Картинка
url_image = content["hdurl"]
response_image = requests.get(url_image)
image = response_image.content

with open("image.jpg", "wb") as file:
    file.write(image)

streamlit.image("image.jpg")

#Описание
streamlit.write(content["explanation"])

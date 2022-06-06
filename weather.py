# Імпорт модулів
import requests, json

# URL запит
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# Назва міста
CITY = str(input("Введіть назву міста англійськими літерами:"))

# API
API_KEY = "ae2e7230cfaa7cfc7890b0c434f8c109"

# Кінцевий API запит 
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric" + "&lang=ua"

response = requests.get(URL)

if response.status_code == 200:
    
   data = response.json()
   main = data['main']
   temperature = main['temp']
   temp_feels_like = main['feels_like']  
   humidity = main['humidity']
   pressure = main['pressure']
   weather = data['weather']
   wind = data['wind']
   
   print(f"{CITY:-^35}")   
   print(f"Температура повітря: {temperature} °C")
   print(f"Відчувається: {temp_feels_like} °C")    
   print(f"Вологість повітря: {humidity} %")
   print(f"Тиск: {pressure} мм")
   print(f"Погода: {weather[0]['description']}")
   print(f"Швидкість вітру: {wind['speed']} м/с")
else:
   print("Помилка HTTP запиту")
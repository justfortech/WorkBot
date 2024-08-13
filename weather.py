import requests
from bs4 import BeautifulSoup
import random




def get_weather_today():
    try:
        user_agent_list = (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        )

        headers = {'accept': '*/*',
                   'User-agent': random.choice(user_agent_list)}
        url = 'https://www.gismeteo.ru/weather-moscow-4368/'

        res=requests.get(url=url, headers=headers)
        soup=BeautifulSoup(res.text, "html.parser")
        weather = soup.find(class_="weathertab is-active")

        weather = soup.find(class_="weathertab is-active")["data-tooltip"]
        temp = soup.find_all("temperature-value")[1]["value"]
        prec = soup.find_all(class_="precipitation")[1].text.strip()

        return f"По данным Gismeteo в Москве {weather}\nОсадки: {prec}\nСейчас по ощущению: {temp}"
    except:
        return f"Сервер не доступен"


from bs4 import BeautifulSoup
import requests

#get the current weather from weather.com using css selectors (inspect element, then copy css selector to soup.select)

def get_weather():
    url = 'https://weather.com/weather/tenday/l/Navarre+FL?canonicalCityId=d6912362c8a9d47f8e8d740994e137a76af65d4e8e1bcf8d0c6cad35256ca659'
    request_res = requests.get(url)
    soup = BeautifulSoup(request_res.text, 'html.parser')
    return soup

def get_temperature():
    soup = get_weather()
    temperature = soup.select('#detailIndex0 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')[0].text
    return temperature

def get_weather_description():
    soup = get_weather()
    description = soup.select('#detailIndex0 > div:nth-child(2) > div:nth-child(1) > p:nth-child(3)')[0].text
    return description
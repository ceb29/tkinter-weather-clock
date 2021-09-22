from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup()
url = "https://weather.com/weather/today/l/f2a3ee265a27f9e5dfd62c6c239be80bb82347f20264827e8bd63e44a104382a"
request_res = requests.get(url)
soup = BeautifulSoup(request_res.text, "html.parser")
print(soup.select(".CurrentConditions--tempValue--3a50n")[0].text)
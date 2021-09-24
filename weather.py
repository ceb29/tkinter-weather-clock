from bs4 import BeautifulSoup
import requests

#get the current weather from weather.com using css selectors (inspect element, then copy css selector)

class Weather():
    def __init__(self):
        self.soup_temperature = BeautifulSoup()
        self.soup_description = BeautifulSoup()
        self.temperature_selector = ".CurrentConditions--tempValue--3a50n"
        self.description_selector = "#detailIndex0 > div:nth-child(2) > div:nth-child(1) > p:nth-child(3)"
        self.internet_status = True

    #update soup object
    def get_soup(self, url):
        try:
            request_res = requests.get(url)
            soup = BeautifulSoup(request_res.text, "html.parser")
            self.internet_status = True
            return soup
        except requests.exceptions.RequestException as ex:
            #print(ex)
            self.internet_status = False
            return " "

    def update_temperature(self):
        url_temp = "https://weather.com/weather/today/l/f2a3ee265a27f9e5dfd62c6c239be80bb82347f20264827e8bd63e44a104382a"
        self.soup_temperature = self.get_soup(url_temp)

    def update_description(self):
        url_desc = "https://weather.com/weather/tenday/l/f2a3ee265a27f9e5dfd62c6c239be80bb82347f20264827e8bd63e44a104382a"
        self.soup_description = self.get_soup(url_desc)

    def update(self):
        self.update_temperature()
        self.update_description()

    #get text using css selector
    def selector_text(self, soup, selector):
        return soup.select(selector)[0].text

    def temperature(self):
        if self.internet_status == False:
            return " "
        return self.selector_text(self.soup_temperature, self.temperature_selector)

    def description(self):
        if self.internet_status == False:
            return " "
        return self.selector_text(self.soup_description, self.description_selector)
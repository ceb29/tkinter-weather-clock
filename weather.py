from bs4 import BeautifulSoup
import requests

#get the current weather from weather.com using css selectors (inspect element, then copy css selector)

class Weather():
    def __init__(self):
        self.soup = BeautifulSoup()
        self.url = "https://weather.com/weather/today/l/f2a3ee265a27f9e5dfd62c6c239be80bb82347f20264827e8bd63e44a104382a"
        self.temperature_selector = ".CurrentConditions--tempValue--3a50n"
        self.phrase_selector = ".CurrentConditions--phraseValue--2Z18W"
        self.precip_selector = ".CurrentConditions--precipValue--3nxCj > span:nth-child(1)"
        self.internet_status = True

    #update soup object
    def update(self):
        print("1")
        try:
            request_res = requests.get(self.url)
            self.soup = BeautifulSoup(request_res.text, "html.parser")
            self.internet_status = True
        except requests.exceptions.RequestException as ex:
            #print(ex)
            self.internet_status = False

    #get text using css selector
    def selector_text(self, selector):
        return self.soup.select(selector)[0].text

    def temperature(self):
        if self.internet_status == False:
            return " "
        temperature = self.selector_text(self.temperature_selector)
        return temperature

    def description(self):
        if self.internet_status == False:
            return " "
        description = self.selector_text(self.phrase_selector) + ". " + self.selector_text(self.precip_selector) + ". "
        return description
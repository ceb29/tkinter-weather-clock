import tkinter
from tkinter.constants import END
import threading
import weather
import time

class Display():
    def __init__(self):
        self.win = tkinter.Tk()
        self.weather = weather.Weather()
        self.clock_dict = self.get_clock_dict()
        self.date_text = tkinter.Text(self.win, bg="black", bd=0, highlightthickness=0, font="freesansbold, 36", fg="white", height=2, width=15)
        self.time_text = tkinter.Text(self.win, bg="black", bd=0, highlightthickness=0, font="freesansbold, 120", fg="white", height=1, width=15)
        self.temperature_text = tkinter.Text(self.win, bg="black", bd=0, highlightthickness=0, font="freesansbold, 36", fg="white", height=1, width=15)
        self.weather_description_text = tkinter.Text(self.win, bg="black", bd=0, highlightthickness=0, font="freesansbold, 24", fg="white", height=3, width=50)
        self.delay_time = 1000 * 60 * 15
        self.last_time = self.get_time_millis()
        self.weather_update_flag = 0
        self.time_flag = 0
        self.weather_flag = 0

    def setup_win(self):
        self.win.attributes("-fullscreen", True)
        self.win.configure(bg="black", cursor="none")

    def setup_date_text(self):
        self.setup_text(self.date_text, self.clock_dict["month"] + " " + self.clock_dict["day_date"] + " " + self.clock_dict["year"])
        self.date_text.pack()

    def setup_time_text(self):
        self.setup_text(self.time_text, self.clock_dict["hour"] + ":" + self.clock_dict["min"] + ":" + self.clock_dict["sec"])
        self.time_text.pack()

    def setup_temperature_text(self):
        self.setup_text(self.temperature_text, " ")
        self.temperature_text.pack()

    def setup_weather_description_text(self):
        self.setup_text(self.weather_description_text, " ")
        self.weather_description_text.pack()
    
    def setup_weather(self):
        self.setup_temperature_text()
        self.setup_weather_description_text()

    def setup_exit_button(self):
        exit_button = tkinter.Button(self.win, bg="black", fg="black",  activebackground="black", bd=0, highlightthickness=0, command=self.win.destroy)
        exit_button.place(x=0,y=0)

    def twelve_hour_clock(self, hour):
        if hour > 12:
            hour -= 12
        if hour == 0:
            hour = 12
        return str(hour)

    def get_time_millis(self):
        return int(time.time()*1000)

    def delete_text(self,tk_text):
        tk_text.delete("1.0", END)

    def insert_text(self, tk_text, text_string):
        tk_text.insert("1.0", text_string)

    def refresh_text(self, tk_text, text_string):
        self.delete_text(tk_text)
        self.insert_text(tk_text, text_string)

    def setup_text(self, tk_text, text_string):
        tk_text.tag_configure("tag_name", justify='center')
        self.insert_text(tk_text, text_string)
        tk_text.tag_add("tag_name", "1.0", "end")
        tk_text.config(cursor="none")

    def update_text(self, tk_text, text_string):
        tk_text.tag_configure("tag_name", justify='center')
        self.refresh_text(tk_text, text_string)
        tk_text.tag_add("tag_name", "1.0", "end")

    def update_date_time(self):
        self.clock_dict = self.get_clock_dict()
        self.update_text(self.date_text, self.clock_dict["month"] + " " + self.clock_dict["day_date"] + " " + self.clock_dict["year"])
        self.update_text(self.time_text, self.clock_dict["hour"] + ":" + self.clock_dict["min"] + ":" + self.clock_dict["sec"])
        self.win.after(500, self.update_date_time)

    def update_weather(self):
        self.weather.update()
        self.update_text(self.temperature_text, " " + self.weather.temperature())
        self.update_text(self.weather_description_text, self.weather.description())
        self.win.after(15*60*1000, self.update_weather)

    def remove_spaces(self, list):
        list_copy = list[:]
        for element in list_copy:
            if element == "":
                list.remove(element)
        return list

    def get_clock_dict(self):
        date_time_string = time.ctime()
        date_time_list = self.remove_spaces(list(date_time_string.split(" ")))
        time_list = list(date_time_list[3].split(":"))
        clock_dict = {"day_week":date_time_list[0],
                    "month":date_time_list[1], 
                    "day_date":date_time_list[2], 
                    "year":date_time_list[4], 
                    "hour":self.twelve_hour_clock(int(time_list[0])), 
                    "min":time_list[1], 
                    "sec":time_list[2]}
        return clock_dict

    def setup(self):
        self.clock_dict = self.get_clock_dict()
        self.setup_win()
        self.setup_date_text()
        self.setup_time_text()
        self.setup_weather()
        self.setup_exit_button()

    def update(self):
        self.update_date_time()
        self.update_weather()
        
    def run(self):
        self.update()
        self.win.mainloop()
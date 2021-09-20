import tkinter
from tkinter.constants import END, INSERT
import weather
import time

#code will be cleaned up eventually, right now I'm just learning

def get_time_millis():
    return int(time.time()*1000)

def refresh_text(tk_text, text_string):
    tk_text.delete("1.0", END)
    tk_text.insert("1.0", text_string)

def main():
    #setup window
    win = tkinter.Tk()
    win.geometry("550x250")
    win.title = "Test"
    win.configure(bg="black")
    #setup widgets
    i = 1
    #clock text
    date_time = time.localtime(time.time())
    print(date_time)
    date_time_text = tkinter.Text(win, bg="black", bd=0, font="freesansbold, 24", fg="white", height=2, width=22)
    date_time_text.insert("1.0", date_time)
    date_time_text.pack()
    #weather text
    temperature = "temp = " + weather.get_weather()
    temperature_text = tkinter.Text(win, bg="black", bd=0, font="freesansbold, 12", fg="white", height=2, width=10)
    temperature_text.insert("1.0", temperature)
    temperature_text.pack()
    #number of weather lookups text
    lookup_amount = "lookups = " + str(i)
    lookup_text = tkinter.Text(win, bg="black", bd=0, font="freesansbold, 12", fg="white", height=1, width=10)
    lookup_text.insert("1.0", lookup_amount)
    lookup_text.pack()
    #variables for delay
    delay_time = 1000 * 60 #update every minute
    last_time = get_time_millis()
    #start window
    win.update()

    #main loop
    while True:
        current_time = int(get_time_millis())
        if current_time - last_time > delay_time:
            i += 1
            #update temperature text
            temperature = "temp = " + weather.get_weather()
            refresh_text(temperature_text, temperature)
            #update lookup amount text
            lookup_amount = "lookups = " + str(i)
            refresh_text(lookup_text, str(i))
            last_time = int(get_time_millis())
        #update clock text
        date_time = time.localtime(time.time())
        refresh_text(date_time_text, date_time)
        win.update()

if __name__ == "__main__":
    main()

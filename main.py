import tkinter
import weather
import time

#code will be cleaned up eventually, right now I'm just learning

def get_time_millis():
    return int(time.time() * 1000)

def main():
    i = 1
    win = tkinter.Tk()
    win.geometry("500x250")
    win.title = "Test"
    date_time = tkinter.StringVar()
    date_time.set(time.ctime())
    date_time_label = tkinter.Label(win, width = 40, textvariable = date_time)
    date_time_label.pack()
    temperature = tkinter.StringVar()
    temperature.set("temp = " + weather.get_weather() + " lookups = " + str(i))
    temperature_label = tkinter.Label(win, width = 25, textvariable = temperature)
    temperature_label.pack()
    delay_time = 10000
    last_time = get_time_millis()
    win.update()

    while True:
        current_time = int(get_time_millis())
        if current_time - last_time > delay_time:
            i+=1
            temperature.set("temp = " + weather.get_weather() + " lookups = " + str(i))
            last_time = int(get_time_millis())
        date_time.set(time.ctime())
        win.update()

if __name__ == "__main__":
    main()

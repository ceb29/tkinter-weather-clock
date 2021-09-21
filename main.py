import tkinter
from tkinter.constants import END, INSERT
import weather
import time

#code will be cleaned up eventually, right now I'm just learning

def get_time_millis():
    return int(time.time()*1000)

def delete_text(tk_text):
    tk_text.delete("1.0", END)

def insert_text(tk_text, text_string):
    tk_text.insert("1.0", text_string)

def refresh_text(tk_text, text_string):
    delete_text(tk_text)
    insert_text(tk_text, text_string)

def setup_text(tk_text, text_string):
    tk_text.tag_configure("tag_name", justify='center')
    insert_text(tk_text, text_string)
    tk_text.tag_add("tag_name", "1.0", "end")

def update_text(tk_text, text_string):
    tk_text.tag_configure("tag_name", justify='center')
    refresh_text(tk_text, text_string)
    tk_text.tag_add("tag_name", "1.0", "end")

def get_clock_dict():
    date_time_string = time.ctime()
    date_time_list = list(date_time_string.split(" "))
    clock_dict = {"day_week":date_time_list[0], "month":date_time_list[1], "day_date":date_time_list[2], 
                  "time":date_time_list[3], "year":date_time_list[4]}
    return clock_dict

def main():
    #setup window
    win = tkinter.Tk()
    win.geometry("550x250")
    win.title = "Test"
    win.configure(bg="black")

    #clock text
    clock_dict = get_clock_dict()
    time_text = tkinter.Text(win, bg="black", bd=0, font="freesansbold, 36", fg="white", height=1, width=15)
    setup_text(time_text, clock_dict["time"])
    time_text.pack()
    date_text = tkinter.Text(win, bg="black", bd=0, font="freesansbold, 12", fg="white", height=1, width=15)
    setup_text(date_text, clock_dict["month"] + " " + clock_dict["day_date"] + " " + clock_dict["year"])
    date_text.pack()

    #weather text
    temperature_text = tkinter.Text(win, bg="black", bd=0, font="freesansbold, 24", fg="white", height=1, width=15)
    setup_text(temperature_text, " " + weather.get_weather())
    temperature_text.pack()

    #number of weather lookups text
    i = 1
    lookup_text = tkinter.Text(win, bg="black", bd=0, font="freesansbold, 12", fg="white", height=1, width=15)
    setup_text(lookup_text, "lookups = " + str(i))
    lookup_text.pack()

    #variables for delay
    delay_time = 1000 * 60 * 15 #update every minute
    last_time = get_time_millis()

    #start window
    win.update()

    #main loop
    while True:
        #update clock text
        clock_dict = get_clock_dict()
        update_text(time_text, clock_dict["time"])
        update_text(date_text, clock_dict["month"] + " " + clock_dict["day_date"] + " " + clock_dict["year"])
        current_time = int(get_time_millis())
        if current_time - last_time > delay_time:
            i += 1
            update_text(temperature_text, " " + weather.get_weather())
            update_text(lookup_text, "lookups = " + str(i))
            last_time = int(get_time_millis())
        win.update()

if __name__ == "__main__":
    main()

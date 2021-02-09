from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import requests, json
import time
from datetime import datetime
import blpapi


def test_news():
    type = 'sports'
    apiKey = '0aa18f0aee7a40d18225c0ed63656d68'
    BASE_URL = f'http://newsapi.org/v2/top-headlines?country=in&category={type}&apiKey='+apiKey




class Mirror_GUI():
    def __init__(self):
        self.mirror_gui = Tk()
        self.mirror_gui.title("Mirror GUI")

        self.mirror_gui.geometry('1920x1080')
        self.mirror_gui.configure(bg='black')

        self.largeFont = font.Font(family="Times New Roman CE", size=70)
        self.mediumFont = font.Font(family="Times New Roman CE", size=40)
        self.normalFont = font.Font(family="Times New Roman CE", size=20)

    def base_GUI(self):

        # Weather frame

        # Time
        self.weather_frame = Frame(self.mirror_gui, borderwidth=5, relief="ridge", width=400,
                                   height=200, bg='black', highlightbackground="gray")

        # Weather
        self.label_time = Label(self.weather_frame, text="City", fg='white', bg='black',
                       font=self.normalFont, justify=LEFT)
        self.label_city = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                       font=self.normalFont, justify=CENTER)
        self.label_temperature = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                        font=self.normalFont, justify=LEFT)
        self.label_humidity = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                        font=self.normalFont, justify=LEFT)
        self.label_preassure = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                        font=self.normalFont, justify=LEFT)
        self.label_condition = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                        font=self.normalFont, justify=LEFT)

        self.label_city.grid(row=0, column=1, sticky=W, pady=2)
        self.label_time.grid(row=1, column=1, sticky=W, pady=2)
        self.label_temperature.grid(row=2, column=1, sticky=W, pady=2)
        self.label_humidity.grid(row=3, column=1, sticky=W, pady=2)
        self.label_preassure.grid(row=4, column=1, sticky=W, pady=2)
        self.label_condition.grid(row=5, column=1, sticky=W, pady=2)

        # News frame
        self.news_frame = Frame(self.mirror_gui, borderwidth=5, relief="ridge", width=400,
                                   height=200, bg='black', highlightbackground="gray")

        self.mid_frame = Frame(self.mirror_gui, borderwidth=5, relief="ridge", width=1050,
                                height=200, bg='black', highlightbackground="gray")


        # Frame grids
        self.weather_frame.grid(row=0, column=1, sticky=W, padx=20, pady=20)

        self.mid_frame.grid(row=0, column=2, sticky=W, padx=20, pady=20)
        self.news_frame.grid(row=0, column=3, sticky=W, padx=20, pady=20)



    @staticmethod
    def get_weather_data(city, units):
        weather_url = "https://api.openweathermap.org/data/2.5/weather?"
        weather_api = "3860a5e3975d1317258172dd2623ac4d"
        url = weather_url + "q=" + city + "&units=" + units + "&appid=" + weather_api
        response = requests.get(url)
        if response.status_code == 200:
            print("Getting weather data...")
            data = response.json()
            main = data['main']
            weather = data['weather']

            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            condition = weather[0]['main']

            # print(f"{city:-^30}")
            # print(f"Temperature: {temperature}")
            # print(f"Humidity: {humidity}")
            # print(f"Pressure: {pressure}")
            # print(f"Weather Report: {condition}")
            return city, temperature, humidity, pressure, condition
        else:
            # showing the error message
            print("Error in the HTTP request")

    def update_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time_ = "Current time is : " + current_time
        self.label_time.configure(text=current_time_)
        self.mirror_gui.after(1000, self.update_time)

    def update_weather(self):
        city, temp, hum, pres, cond = self.get_weather_data("Chicago", "metric")
        current_temp = "Temperature: " + str(temp) + " °C"
        current_hum = "Humudity: " + str(hum)
        current_press = "Pressure: " + str(pres)
        current_cond = "Condition: " + cond
        self.label_city.configure(text=city)
        self.label_temperature.configure(text=current_temp)
        self.label_humidity.configure(text=current_hum)
        self.label_preassure.configure(text=current_press)
        self.label_condition.configure(text=current_cond)
        self.mirror_gui.after(5000000, self.update_weather)

    def update_news_feed(self):
        pass



    def display(self):
        self.mirror_gui.mainloop()


GUI = Mirror_GUI()
GUI.base_GUI()
GUI.update_time()
GUI.update_weather()
GUI.display()


# root = tk.Tk()
# fonts = list(font.families())
# fonts.sort()
# print(fonts)
# root.destroy()







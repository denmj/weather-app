from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import requests, json
import time
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image
import os
import pygame


class Mirror_GUI():
    def __init__(self):
        self.mirror_gui = Tk()
        self.mirror_gui.title("Mirror GUI")

        self.mirror_gui.geometry('1920x1080')
        self.mirror_gui.configure(bg='black')

        self.largeFont = font.Font(family="Times New Roman CE", size=70)
        self.mediumFont = font.Font(family="Times New Roman CE", size=40)
        self.normalFont = font.Font(family="Times New Roman CE", size=20)
        self.smallFont = font.Font(family="Times New Roman CE", size=15)
        self.mirror_gui.grid_propagate(False)
        self.date = datetime.now()
        self.year = self.date.year
        self.month = self.date.month
        self.day = self.date.day

        pygame.init()
        pygame.mixer.init()

        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()

    def base_GUI(self):
        # Weather frame
        # Time
        self.weather_frame = Frame(self.mirror_gui, borderwidth=0, relief="ridge", width=400,
                                   height=0, bg='black', highlightbackground="gray")

        # Weather
        self.label_time = Label(self.weather_frame, text="City", fg='white', bg='black',
                                font=self.normalFont, justify=LEFT)
        self.label_city = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                                font=self.normalFont, justify=LEFT)
        self.label_temperature = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                                       font=self.normalFont, justify=LEFT)
        self.label_humidity = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                                    font=self.normalFont, justify=LEFT)
        self.label_preassure = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                                     font=self.normalFont, justify=LEFT)
        self.label_condition = Label(self.weather_frame, text="Loading...", fg='white', bg='black',
                                     font=self.normalFont, justify=LEFT)

        # Calendar area
        self.calendar_frame = Frame(self.mirror_gui, borderwidth=0, relief="ridge", width=400,
                                    height=50, bg='black', highlightbackground="gray")
        self.cal = Calendar(self.calendar_frame, font=self.smallFont, selectmode='day', locale='en_US', year=self.year,
                            month=self.month, day=self.day, background="black", disabledbackground="black", bordercolor="black",
                            headersbackground="black", normalbackground="black", foreground='white',
                            normalforeground='white', headersforeground='white', selectbackground='black',
                            weekendbackground='black', othermonthbackground='black', othermonthwebackground='black')



        self.label_city.grid(row=0, column=1, sticky=W, pady=2)
        self.label_time.grid(row=1, column=1, sticky=W, pady=2)
        self.label_temperature.grid(row=2, column=1, sticky=W, pady=2)
        self.label_humidity.grid(row=3, column=1, sticky=W, pady=2)
        self.label_preassure.grid(row=4, column=1, sticky=W, pady=2)
        self.label_condition.grid(row=5, column=1, sticky=W, pady=2)
        self.cal.grid(row=0, column=1, sticky=W, pady=2)

        # News frame
        self.news_frame = Frame(self.mirror_gui, borderwidth=0, relief="ridge", width=200, height=200, bg='black',
                                highlightbackground="gray")
        # Sport area
        self.label_sport_news = Label(self.news_frame, text="Loading...", fg='white', bg='black', font=self.normalFont,
                                      justify=RIGHT)
        self.txtarea_sport_news = Text(self.news_frame, font=self.smallFont, bg='black',
                                       fg='white', height=5, width=40, borderwidth=0)

        # Entertainment area
        self.label_entert_news = Label(self.news_frame, text="Loading...", fg='white', bg='black', font=self.normalFont,
                                       justify=RIGHT)
        self.txtarea_entert_news = Text(self.news_frame, font=self.smallFont, bg='black',
                                        fg='white', height=5, width=40, borderwidth=0)

        # Busisness
        self.label_business_news = Label(self.news_frame, text="Loading...", fg='white', bg='black',
                                         font=self.normalFont,
                                         justify=RIGHT)
        self.txtarea_business_news = Text(self.news_frame, font=self.smallFont, bg='black',
                                          fg='white', height=5, width=40, borderwidth=0)

        # technology
        self.label_tech_news = Label(self.news_frame, text="Loading...", fg='white', bg='black',
                                     font=self.normalFont,
                                     justify=RIGHT)
        self.txtarea_tech_news = Text(self.news_frame, font=self.smallFont, bg='black',
                                      fg='white', height=5, width=40, borderwidth=0)

        # Player Area
        trackframe = LabelFrame(self.mirror_gui, text="Song Track", font=self.smallFont, bg="black",
                                fg="white", bd=5, relief="ridge", borderwidth=1)
        trackframe.place(x=20, y=400, width=600, height=100)

        # Inserting Song Track Label
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=self.smallFont,
                          bg="Gray", fg="white").grid(row=0, column=0, padx=10, pady=5)
        # # Inserting Status Label
        trackstatus = Label(trackframe, textvariable=self.status, font=self.smallFont, bg="Gray",
                            fg="white").grid(row=0, column=1, padx=10, pady=5)

        # Creating Button Frame
        buttonframe = LabelFrame(self.mirror_gui, text="Control Panel", font=self.smallFont, bg="black",
                                 fg="white", bd=5, relief="ridge", borderwidth=1)
        buttonframe.place(x=20, y=500, width=600, height=100)

        # Inserting Play Button
        playbtn = Button(buttonframe, text="PLAY", command=self.playsong, width=10, height=1,
                         font=self.smallFont, fg="white", bg="black").grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        # Inserting Pause Button
        playbtn = Button(buttonframe, text="PAUSE", command=self.pausesong, width=8, height=1,
                         font=self.smallFont, fg="white", bg="black").grid(row=0, column=1, padx=10,
                                                                                              pady=5)
        # Inserting Unpause Button
        playbtn = Button(buttonframe, text="UNPAUSE", command=self.unpausesong, width=10, height=1,
                         font=self.smallFont, fg="white", bg="black").grid(row=0, column=2, padx=10,
                                                                                              pady=5)
        # Inserting Stop Button
        playbtn = Button(buttonframe, text="STOP", command=self.stopsong, width=10, height=1,
                         font=self.smallFont, fg="white", bg="black").grid(row=0, column=3, padx=10,
                                                                                              pady=5)



        self.label_sport_news.grid(row=0, column=1, sticky=W, pady=2)
        self.txtarea_sport_news.grid(row=1, column=1, sticky=W, pady=2)

        self.label_entert_news.grid(row=2, column=1, sticky=W, pady=2)
        self.txtarea_entert_news.grid(row=3, column=1, sticky=W, pady=2)

        self.label_business_news.grid(row=4, column=1, sticky=W, pady=2)
        self.txtarea_business_news.grid(row=5, column=1, sticky=W, pady=2)

        self.label_tech_news.grid(row=6, column=1, sticky=W, pady=2)
        self.txtarea_tech_news.grid(row=7, column=1, sticky=W, pady=2)

        # Frame grids
        self.weather_frame.place(x=20, y=20)
        self.calendar_frame.place(x=20, y=700)
        self.news_frame.place(x=1450, y=20)

    def playsong(self):
        # Loading Selected Song
        pygame.mixer.music.load('D:/pink_floyd_w_y_w_h.mp3')
        # Playing Selected Song
        pygame.mixer.music.play()

    def pausesong(self):
        pygame.mixer.music.pause()

    def unpausesong(self):
        pass

    def stopsong(self):
        pass

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

    @staticmethod
    def get_news_data(self):
        news_type = ["sports", "entertainment", "business",
                     "technology"]
        apiKey = '0aa18f0aee7a40d18225c0ed63656d68'
        news = []

        for t in news_type:
            BASE_URL = f'http://newsapi.org/v2/top-headlines?country=us&category={t}&apiKey=' + apiKey
            response = requests.get(BASE_URL)
            if response.status_code == 200:
                data = response.json()
                news_type = data['articles']
                news.append(news_type)
        return news

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

    def update_news(self):
        news_data = self.get_news_data(self)

        self.label_sport_news.configure(text=news_data[0][0]['source']['name'])
        self.txtarea_sport_news.insert(END, news_data[0][0]['title'])

        self.label_entert_news.configure(text=news_data[1][0]['source']['name'])
        self.txtarea_entert_news.insert(END, news_data[1][0]['title'])

        self.label_business_news.configure(text=news_data[2][0]['source']['name'])
        self.txtarea_business_news.insert(END, news_data[2][0]['title'])

        self.label_tech_news.configure(text=news_data[3][0]['source']['name'])
        self.txtarea_tech_news.insert(END, news_data[3][0]['title'])

        # print(news['source']['name'])
        #     print(news['title'])

    def display(self):
        self.mirror_gui.mainloop()




GUI = Mirror_GUI()
GUI.base_GUI()
GUI.update_time()
GUI.update_weather()
GUI.update_news()
GUI.display()
#


# f = 'D:/pink_floyd_w_y_w_h.mp3'
# print(os.path.exists('D://Projects//weather-app//pics//play.png'))

# def pmusic(file):
#     pygame.init()
#     pygame.mixer.init()
#     clock = pygame.time.Clock()
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         print("Playing...")
#         clock.tick(1000)
# pmusic(f)

# news_list = test_news()
# print(news_list[3][0]['source']['name'])
# print(news_list[3][0]['title'])


# root = tk.Tk()
# img = tk.PhotoImage(file="D://Projects//weather-app//pics//play.png")
#
# label = tk.Label(root, image=img)
# label.pack()
#
# root.mainloop()

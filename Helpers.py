from datetime import datetime
import pyodbc
import requests, json


def connect(driver, server_name, db_name):
    try:
        conn = pyodbc.connect(DRIVER=driver,
                                SERVER=server_name,
                                DATABASE=db_name)
        print("Connection to SQL Server DB successful")
        return conn

    except Error as e:
        print(f"The error '{e}' occurred")


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


def get_weather_data_json(city, units):
    weather_url = "https://api.openweathermap.org/data/2.5/weather?"
    weather_api = "3860a5e3975d1317258172dd2623ac4d"
    url = weather_url + "q=" + city + "&units=" + units + "&appid=" + weather_api
    try:
        response = requests.get(url)
        print("Connected and retrived data")
        if response.status_code == 200:
            print("Getting weather data...")
            data = response.json()
        return data

    except Error as e:
        print(f"The error '{e}' occurred")


# d = get_weather_data_json("Los Angeles", "metric")

def parse_weather_data(d):
    one_dim_dict = {}
    for key_i in d:
        if isinstance(d[key_i], dict):
            for key_j in d[key_i]:
                one_dim_dict[key_i+"_"+key_j] = d[key_i][key_j]

        elif isinstance(d[key_i], list):
            for list_element in d[key_i]:
                if isinstance(list_element, dict):
                    for key_k in list_element:
                        one_dim_dict[key_i + "_" + key_k] = list_element[key_k]
        else:
            one_dim_dict[key_i] = d[key_i]
    return one_dim_dict

# print(parse_weather_data(d))


def load_weather_to_SQL(dict):
    dr = '{SQL Server}'
    server = 'DENIS'
    db = 'weather_DW'
    connection = connect(dr, server, db)
    cursor = connection.cursor()

    current_date = datetime.today()
    date_strip = current_date.strftime("%d/%m/%Y")
    time_strip = current_date.strftime("%H:%M:%S")


    inser_into_coord = "INSERT  INTO Coordinates (Coord_lon, Coord_lat, City, Country, TimeZone)" \
                       "SELECT t.lon, t.lat, t.city, t.country, t.tzone " \
                       "from (VALUES (?, ?, ?, ?, ?)) as t(lon, lat, city, country, tzone)" \
                       "WHERE NOT EXISTS (SELECT 1 FROM Coordinates " \
                       "WHERE Coordinates.Coord_lon = t.lon AND Coordinates.Coord_lat = t.lat )"

    inser_into_weather = "INSERT INTO Weather (MainWeather, WeatherDesc, WeatherDate, WeatherTime, CoordID) " \
                         "SELECT t.mainw, t.wdesc, t.date, t.time, c.CoordID from(VALUES(?, ?, ?, ?))" \
                         " as t(mainw, wdesc, date, time)" \
                         "JOIN Coordinates as c ON c.Coord_lon = ? AND c.Coord_lat = ? "

    insert_into_temperature = "INSERT INTO Temperature(Temp, Feels_like, TempMin, TempMax, Preasure," \
                              " Humidity, Visibility, WindSpeed, WindDeg, WeatherDate, WeatherTime, CoordID)" \
                              "SELECT t.temp, t.feel, t.tempmin, t.tempmax, t.pres," \
                              " t.hum, t.vis, t.ws, t.wd, t.date, t.time, c.CoordID from (VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)) as " \
                              "t(temp, feel, tempmin, tempmax, pres, hum, vis, ws, wd, date, time) " \
                              "JOIN Coordinates as c ON c.Coord_lon = ? AND c.Coord_lat = ?"

    try:

        cursor.execute(inser_into_coord, [dict["coord_lon"],
                                          dict["coord_lat"],
                                          dict["name"],
                                          dict["sys_country"],
                                          dict["timezone"]])

        cursor.execute(inser_into_weather, [dict["weather_main"],
                                            dict["weather_description"],
                                            date_strip,
                                            time_strip,
                                            dict["coord_lon"],
                                            dict["coord_lat"]])

        cursor.execute(insert_into_temperature, [dict["main_temp"],
                                                 dict["main_feels_like"],
                                                 dict["main_temp_min"],
                                                 dict["main_temp_max"],
                                                 dict["main_pressure"],
                                                 dict["main_humidity"],
                                                 dict["visibility"],
                                                 dict["wind_speed"],
                                                 dict["wind_deg"],
                                                 date_strip,
                                                 time_strip,
                                                 dict["coord_lon"],
                                                 dict["coord_lat"]])
        print("Weather data loaded successfully")
    except pyodbc.IntegrityError as e:
        print(e)

    cursor.commit()


# d = datetime.today()
# print( d.strftime("%d/%m/%Y"))
# print( d.strftime("%H:%M:%S"))

#
# print(datetime.today())
# print(datetime.today())
# print(datetime.month)
# print(datetime.year)
#
# print(datetime.now())



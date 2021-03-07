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


def parse_weather_data(d):
    one_dim_dict = {}
    for key_i in d:
        if isinstance(d[key_i], dict):
            for key_j in d[key_i]:
                # print("{}, {}".format(key_i+"_"+key_j, d[key_i][key_j]))
                one_dim_dict[key_i+"_"+key_j] = d[key_i][key_j]

        elif isinstance(d[key_i], list):
            for list_element in d[key_i]:
                if isinstance(list_element, dict):
                    for key_k in list_element:
                        # print("{}, {}".format(key_i + "_" + key_k, list_element[key_k]))
                        one_dim_dict[key_i + "_" + key_k] = list_element[key_k]
        else:
            # print("{}, {}".format(key_i, d[key_i]))
            one_dim_dict[key_i] = d[key_i]
    return one_dim_dict

# weather_json = get_weather_data_json("Chicago", "metric")
#
# print(weather_json)

d = {'coord': {'lon': -93.2638, 'lat': 44.98}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'base': 'stations', 'main': {'temp': 6.47, 'feels_like': 1.29, 'temp_min': 6, 'temp_max': 7, 'pressure': 1025, 'humidity': 42}, 'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 120}, 'clouds': {'all': 40}, 'dt': 1615076966, 'sys': {'type': 1, 'id': 4984, 'country': 'US', 'sunrise': 1615034500, 'sunset': 1615075626}, 'timezone': -21600, 'id': 5037649, 'name': 'Minneapolis', 'cod': 200}
c = {'coord': {'lon': -87.65, 'lat': 41.85}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 0.24, 'feels_like': -3.54, 'temp_min': -1.67, 'temp_max': 1.67, 'pressure': 1027, 'humidity': 69}, 'visibility': 10000, 'wind': {'speed': 1.71, 'deg': 55}, 'clouds': {'all': 1}, 'dt': 1615093002, 'sys': {'type': 1, 'id': 4861, 'country': 'US', 'sunrise': 1615033032, 'sunset': 1615074400}, 'timezone': -21600, 'id': 4887398, 'name': 'Chicago', 'cod': 200}
e = {'coord': {'lon': -93.9994, 'lat': 44.1636}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 1.91, 'feels_like': -4.92, 'temp_min': 1.67, 'temp_max': 2.22, 'pressure': 1022, 'humidity': 80}, 'visibility': 10000, 'wind': {'speed': 6.69, 'deg': 130}, 'clouds': {'all': 1}, 'dt': 1615096238, 'sys': {'type': 1, 'id': 4917, 'country': 'US', 'sunrise': 1615034643, 'sunset': 1615075836}, 'timezone': -21600, 'id': 5036420, 'name': 'Mankato', 'cod': 200}
z = {'coord': {'lon': -87.65, 'lat': 41.85}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': -0.13, 'feels_like': -3.63, 'temp_min': -1.67, 'temp_max': 1.11, 'pressure': 1027, 'humidity': 80}, 'visibility': 10000, 'wind': {'speed': 1.57, 'deg': 62}, 'clouds': {'all': 1}, 'dt': 1615098106, 'sys': {'type': 1, 'id': 4861, 'country': 'US', 'sunrise': 1615119332, 'sunset': 1615160869}, 'timezone': -21600, 'id': 4887398, 'name': 'Chicago', 'cod': 200}


l = [d, c, e, z]
l_1 = []
for i in l:
    one_dim_dict = parse_weather_data(i)
    l_1.append(one_dim_dict)


print(l_1)
print(l_1[0]["coord_lon"])
print(l_1[0]["coord_lat"])
print(l_1[0]["weather_main"])
print(l_1[0]["weather_description"])



# print(isinstance(d['weather'], list))
# print("Coord_lon", d['coord']['lon'])
# print("Coord_lat", d['coord']['lat'])
# print("weather_id", d['weather'][0]['id'])
# print("Coord_lat", d['coord']['lat'])


# w_data = parse_weather_data(d)
# print(w_data['coord_lon'])
# print(w_data['coord_lat'])
# c_data = parse_weather_data(c)
# print(c_data['coord_lon'])
# print(c_data['coord_lat'])

# print("----"*100)
# print(d)



# d_list =  [[w_data['coord_lon'], w_data['coord_lat']], [c_data['coord_lon'], c_data['coord_lat']], [w_data['coord_lon'], w_data['coord_lat']]  ]

# print(d_list[0])


def test_sql(data_list):
    dr = '{SQL Server}'
    server = 'DENIS'
    db = 'weather_DW'
    connection = connect(dr, server, db)
    cursor = connection.cursor()

    inser_into_coord = "INSERT  INTO Coordinates (Coord_lon, Coord_lat)  SELECT t.lon, t.lat from (VALUES (?, ?)) as t(lon, lat)" \
                       "WHERE NOT EXISTS (SELECT 1 FROM Coordinates WHERE Coordinates.Coord_lon = t.lon AND Coordinates.Coord_lat = t.lat )"

    inser_into_weather = "INSERT INTO Weather (MainWeather, WeatherDesc, CoordID) SELECT t.mainw, t.wdesc, c.CoordID from(VALUES(?, ?)) as t(mainw, wdesc)" \
                         "JOIN Coordinates as c ON c.Coord_lon = ? AND c.Coord_lat = ? "

    insert_into_temperature = "INSERT INTO Temperature(Temp, Feels_like, TempMin, TempMax, Preasure, Humidity, Visibility, WindSpeed, WindDeg, CoordID)" \
                              "SELECT t.temp, t.feel, t.tempmin, t.tempmax, t.pres, t.hum, t.vis, t.ws, t.wd, c.CoordID from (VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)) as " \
                              "t(temp, feel, tempmin, tempmax, pres, hum, vis, ws, wd) JOIN Coordinates as c ON c.Coord_lon = ? AND c.Coord_lat = ?"

    for dict in data_list:
        try:

            cursor.execute(inser_into_coord, [dict["coord_lon"],
                                              dict["coord_lat"]])

            cursor.execute(inser_into_weather, [dict["weather_main"],
                                                dict["weather_description"],
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
                                                     dict["coord_lon"],
                                                     dict["coord_lat"]])
        except pyodbc.IntegrityError as e:
            print(e)

        cursor.commit()

test_sql(l_1)

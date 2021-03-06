import pyodbc


conn_to_weather_db = pyodbc.connect('Driver={SQL Server};'
                      'Server=DENIS;'
                      'Database=weather_DW;'
                      'Trusted_Connection=yes;')


conn_to_bike_store = pyodbc.connect('Driver={SQL Server};'
                      'Server=DENIS;'
                      'Database=bike_store;'
                      'Trusted_Connection=yes;')


cursor = conn_to_bike_store.cursor()
cursor.execute('SELECT * FROM production.brands')

for row in cursor:
    print(row)
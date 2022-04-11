from datetime import datetime as dt
def temperature_logger(data):
    time = dt.now().strftime(%H:H)
    with open('log.csv', 'a') as file:
        file.write(f'{}; temperature; {}')
def pressure_logger():

def wind_speed_logger():


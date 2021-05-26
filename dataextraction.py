import requests
from pandas import DataFrame 
from datetime import datetime

def get_data(api):
    r = requests.get(api)

    data = r.json()

    return data

def import_data(dataframe):
    df.to_csv('~/Data.csv', index=False, mode='a', header=False)
    return 

if __name__ == "__main__":
    #API's
    #Antarctica - http://api.openweathermap.org/data/2.5/weather?q=Ushuaia,ar&APPID=${API_Key}
    #GreenLand - http://api.openweathermap.org/data/2.5/weather?q=nuuk,gl&APPID=${API_Key}
    #Indonesia - http://api.openweathermap.org/data/2.5/weather?q=Jakarta,id&APPID=${API_Key}
    #Rochester - http://api.openweathermap.org/data/2.5/weather?q=rochester,us&APPID=${API_Key}
    
    data = get_data("http://api.openweathermap.org/data/2.5/weather?q=Jakarta,id&APPID=${API_Key}")
    ts = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    k = data['main']['temp']
    temp = round(((9/5)*(k - 273)) + 32)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    
    df = DataFrame({'TimeStamp': [ts],'Location':['Indonesia'] , 'Temperature': [temp], 'Pressure': [pressure], 'Humidity': [humidity], 'wind': [wind]})
    print(df)
    import_data(df)
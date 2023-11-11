import requests
from datetime import date, timedelta, datetime


def get_data(place, days, option):
    # get the forecast from the API
    url = 'https://api.openweathermap.org/data/2.5/forecast?' \
    f'q={place}' \
    '&appid={ENTER YOUR API KEY}''
    
    response = requests.get(url)
    data = response.json()

    # get today and last day to forecast
    current_day = date.today()
    date_format = '%Y-%m-%d %H:%M:%S'
    last_day = current_day + timedelta(days=days - 1)

    weather = []
    date_time = []
    # if the request return successfully
    if data['cod'] == '200':
        # get timestamp
        date_time = [datetime.strptime(dt['dt_txt'], date_format) for dt in data['list']]

        match option:
            case 'Temperature':
                # get temperature
                weather = [temp['main']['temp'] / 10 for temp in data['list']]
            case 'Sky':
                # get weather description
                weather = [icon['weather'][0]['main'] for icon in data['list']]
            case _:
                raise Exception('Need to select one of those options: [Temperature, Sky]')

    # reorganize the data to return
    for index, dt in enumerate(date_time):
        current_day = dt

        # return only the forecast for the days argument
        if current_day.date() > last_day:
            date_time = date_time[:index]
            # change date formate
            date_time = [dt.strftime('%a ,%b %d %H:%M') for dt in date_time]
            weather = weather[:index]
            break

    return weather, date_time

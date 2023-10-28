from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# get data instructions
specified_lines = list(range(10, 17))
data = []
with open('data/stations.txt', 'rb') as file:
    for index, line in enumerate(file):
        if index in specified_lines:
            data.append(line.decode())

# get the data frame
stations = pd.read_csv('data/stations.txt', skiprows=17)

error_dict = {'Error': 'station ID not found, Please follow the instruction page'}


# render main page
@app.route('/')
def home():
    return render_template('home.html', data=data, stations=stations.to_html())


@app.route('/api/v1/<station>/<date>')
def get_temp(station, date):
    """ Get the specific temperature for each date for any station """
    # get data frame
    df = get_df(station)
    if not df:
        return error_dict

    # adjust the date parameter to a string
    date = f'{date[:4]}-{date[4:6]}-{date[6:]}'

    # search for the correct date and get the temperature
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {'station': station,
            'data': date,
            'temperature': temperature}


@app.route('/api/v1/<station>')
def get_all_temp(station):
    """ Get all the temperatures for the given station """
    # get data frame
    df = get_df(station)
    if not df:
        return error_dict

    # adjust the data
    df['TG'] = df['   TG'] / 10
    df = df.loc[df['   TG'] != -9999]

    return df[['    DATE', 'TG']].to_dict(orient='records')


@app.route('/api/v1/yearly/<station>/<year>')
def get_all_year_temp(station, year):
    """ Get all the temperatures for the given station in a given year"""
    # get data frame
    df = get_df(station)
    if not df:
        return error_dict

    # adjust the data
    df['TG'] = df['   TG'] / 10
    df = df.loc[df['   TG'] != -9999]
    df = df.loc[df['    DATE'].dt.year == int(year)]

    return df[['    DATE', 'TG']].to_dict(orient='records')


def get_df(station):
    """ Get the data frame from a txt file"""
    # pad with zeros for a correct file name
    station = station.zfill(6)

    # try to read the file of a station, if it doesn't exist, return an error message
    try:
        # get the data frame
        filename = f'data/TG_STAID{station}.txt'
        return pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    except FileNotFoundError:
        return None


if __name__ == '__main__':
    app.run(debug=True)

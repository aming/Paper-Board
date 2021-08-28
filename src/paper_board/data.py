import csv
import pyowm
import yfinance
import urllib
from datetime import datetime
from . import config
from . import gsheet

DATA_FILE_PATH = config.config_dir + '/data'
DELIMITER = ','

def write_csv_data(data = [], index = 0):
    with open(DATA_FILE_PATH + "-" + str(index), 'w+') as file:
        writer = csv.writer(file, delimiter=DELIMITER)
        for d in data:
            writer.writerow([d])

def read_csv_data(index = 0):
    data = []
    with open(DATA_FILE_PATH + "-" + str(index), 'r') as file:
        reader = csv.reader(file, delimiter=DELIMITER)
        for row in reader:
            data.append(' '.join(row))
    return data

def get_data(index = 0):
    return read_csv_data(index)

def get_price(ticker):
    close = ticker.info['previousClose']
    last = ticker.info['regularMarketPrice']
    change = last - close
    return '{}: {} ({:.2f} {:.2f}%)'.format(
        ticker.info['symbol'],
        last,
        change,
        change / close * 100,
    )

def get_gsheet_data():
    if not 'gsheet' in config.config:
        return "No GSheet data"
    gsheet_config=config.config['gsheet']
    gsheet.init(gsheet_config['credentials_file'])
    return gsheet.get_cell(
            gsheet_config['spreadsheet_id'],
            gsheet_config['sheet_name'],
            gsheet_config['cell_id'],
            )

def get_weather(index = 0):
    filename = DATA_FILE_PATH + "-" + str(index)
    urllib.request.urlretrieve('https://wttr.in/?0ATmQ', filename=filename)

def update():
    place=config.config['weather']['location']
    OpenWMap=pyowm.OWM(config.config['weather']['api_token'])
    manager=OpenWMap.weather_manager()
    weather=manager.weather_at_place(place)
    forecast = manager.forecast_at_place(place, 'daily')
    data0 = [
        'data-pull',
        datetime.now().strftime("%b-%d %H:%M:%S"),
        '{}C.'.format(weather.weather.temperature(unit='celsius')['temp']),
        '{}'.format(weather.weather.detailed_status),
        'Tomorrow: {}'.format(forecast.get_weather_at(pyowm.utils.timestamps.tomorrow()).detailed_status),
    ]
    write_csv_data(data0, 0)
    get_weather(1)
    tickers = yfinance.Tickers('^IXIC ^DJI ^SPX')
    data2 = [
        get_price(tickers.tickers['^IXIC']),
        get_price(tickers.tickers['^DJI']),
        get_price(tickers.tickers['^SPX']),
        get_gsheet_data(),
    ]
    write_csv_data(data2, 2)

import csv, os
import pyowm
import yfinance
from datetime import datetime
from . import config

DATA_FILE_PATH = os.path.expanduser("~") + '/paper_board_data'
DELIMITER = ','

def write_csv_data(data = []):
    with open(DATA_FILE_PATH, 'w') as file:
        writer = csv.writer(file, delimiter=DELIMITER)
        for d in data:
            writer.writerow([d])

def read_csv_data():
    data = []
    with open(DATA_FILE_PATH, 'r') as file:
        reader = csv.reader(file, delimiter=DELIMITER)
        for row in reader:
            data.append(' '.join(row))
    return data

def get_data():
    return read_csv_data()

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

def update():
    place=config.config['weather']['location']
    OpenWMap=pyowm.OWM(config.config['weather']['api_token'])
    manager=OpenWMap.weather_manager()
    weather=manager.weather_at_place(place)
    forecast = manager.forecast_at_place(place, 'daily')
    tickers = yfinance.Tickers('^IXIC ^DJI ^SPX')
    data = [
        '"data-pull" @{}'.format(datetime.now().strftime("%b-%d %H:%M:%S")),
        '',
        'Current temperature is {}C.'.format(weather.weather.temperature(unit='celsius')['temp']),
        'It is {} now.'.format(weather.weather.detailed_status),
        'Tomorrow is {}'.format(forecast.get_weather_at(pyowm.utils.timestamps.tomorrow()).detailed_status),
        '',
        '',
        get_price(tickers.tickers['^IXIC']),
        get_price(tickers.tickers['^DJI']),
        get_price(tickers.tickers['^SPX']),
        '',
        '',
        '',
        '',
        '',
    ]
    write_csv_data(data)

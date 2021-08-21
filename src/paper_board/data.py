import csv
import pyowm
import yfinance
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

def update():
    place=config.config['weather']['location']
    OpenWMap=pyowm.OWM(config.config['weather']['api_token'])
    manager=OpenWMap.weather_manager()
    weather=manager.weather_at_place(place)
    forecast = manager.forecast_at_place(place, 'daily')
    tickers = yfinance.Tickers('^IXIC ^DJI ^SPX')
    data = [
        '"data-pull" @{}'.format(datetime.now().strftime("%b-%d %H:%M:%S")),
        'Current temperature is {}C.'.format(weather.weather.temperature(unit='celsius')['temp']),
        'It is {} now.'.format(weather.weather.detailed_status),
        'Tomorrow is {}'.format(forecast.get_weather_at(pyowm.utils.timestamps.tomorrow()).detailed_status),
        get_price(tickers.tickers['^IXIC']),
        get_price(tickers.tickers['^DJI']),
        get_price(tickers.tickers['^SPX']),
        get_gsheet_data(),
    ]
    write_csv_data(data, 0)

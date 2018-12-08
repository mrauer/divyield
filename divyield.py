import statistics

import requests


def get_symbols():
    """Get symbols and overwrite input file."""
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    symbols = r.json()
    f = open('./symbols.dat', 'w')
    for symbol in symbols:
        if symbol['isEnabled']:
            f.write(''.join([symbol['symbol'], '\n']))
    f.close()
    return len(symbols)


def get_dividends(stock_symbol):
    """Get 5yr dividends when available."""
    api_url = '/'.join(['https://api.iextrading.com/1.0/stock',
                        stock_symbol, 'dividends/5y'])
    r = requests.get(api_url)
    response = r.json()
    history = len(response)
    records = []
    for record in response:
        records.append(record['amount'])
    avg = statistics.mean(records)
    stdev = statistics.stdev(records)
    return history, avg, stdev


def get_chart(stock_symbol):
    """Get stock info such as current valuation."""
    api_url = '/'.join(['https://api.iextrading.com/1.0/stock',
                        stock_symbol, 'chart/1m'])
    r = requests.get(api_url)
    response = r.json()
    records = []
    for record in response:
        records.append(record['close'])
    stock_price = records[-1]
    return stock_price
import statistics

import requests


def get_symbols():
    """
    Get the most recent set of existing symbols from the API.
    :returns:int: number of symbols found.
    """
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    symbols = r.json()
    f = open('./symbols.dat', 'w')
    for symbol in symbols:
        if symbol['isEnabled']:
            f.write(''.join([symbol['symbol'], '\n']))
    f.close()
    return len(symbols)


def get_dividends(stock_symbol, qualified):
    """
    Get 5yr dividends when available.
    :param stock_symbol: str. Symbol of the stock.
    :param qualified:str: 'Q' when qualified.
    :returns:history:int: number of records found.
    :returns:avg:float: avg stock amount value.
    :returns:stdev:float: standard deviation of the distribution.
    """
    api_url = '/'.join(['https://api.iextrading.com/1.0/stock',
                        stock_symbol, 'dividends/5y'])
    r = requests.get(api_url)
    response = r.json()
    history = len(response)
    records = []
    for record in response:
        # Break if the dividend is not qualified
        if qualified and record['qualified'] != 'Q':
            print '>> Not Qualified'
            break
        records.append(record['amount'])
    avg = statistics.mean(records)
    stdev = statistics.stdev(records)
    return history, avg, stdev


def get_chart(stock_symbol):
    """
    Get current valuation of a stock.
    :param stock_symbol: str. Symbol of the stock.
    :returns:stock_price:float: current valuation.
    """
    api_url = '/'.join(['https://api.iextrading.com/1.0/stock',
                        stock_symbol, 'chart/1m'])
    r = requests.get(api_url)
    response = r.json()
    records = []
    for record in response:
        records.append(record['close'])
    stock_price = float(records[-1])
    return stock_price


def ratio_from_all_time_high(stock_symbol):
    """
    Compute the current ratio from the all time high [0, 1]
    :param stock_symbol: str. Symbol of the stock.
    :returns:ratio:float: ratio from all time high.
    """
    api_url = '/'.join(['https://api.iextrading.com/1.0/stock',
                        stock_symbol, 'chart/5y'])
    r = requests.get(api_url)
    response = r.json()
    records = []
    for record in response:
        records.append(float(record['high']))
    ratio = records[-1] / max(records)
    return ratio

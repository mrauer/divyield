import json
import sys
import time

import divyield

invested = float(1000)

if sys.argv > 1:
    args = json.loads(sys.argv[1])
    # Update the list of symbols.
    if 'action' in args and args['action'] == 'update':
        print divyield.get_symbols()

    if 'action' in args and args['action'] == 'dividends':
        r = open('./symbols.dat', 'r')
        w = open('./output.dat', 'w')
        symbols = r.read().split('\n')
        qualified = None
        if 'qualified' in args:
            qualified = 'Q'

        for symbol in symbols:
            history = None
            avg = None
            stdev = None
            print ' '.join(['Computing', symbol])
            try:
                history, avg, stdev = divyield.get_dividends(symbol, qualified)
            except Exception, e:
                print e
                continue

            if history and avg and stdev:
                try:
                    stock_price = divyield.get_chart(symbol)
                    div_yield = float(avg)/stock_price
                    # Calculating the yearly gain.
                    num_stocks = invested/stock_price
                    per_stock = div_yield * stock_price
                    yearly_gain = num_stocks * per_stock
                    # Writing the output file.
                    a = open('./output.dat', 'a')
                    a.write(','.join([str(symbol), str(history),
                                      str(stdev), str(div_yield),
                                      str(stock_price), str(int(num_stocks)),
                                      str(int(per_stock)),
                                      str(yearly_gain)])+'\n')
                    a.close()
                    time.sleep(1)
                except Exception, e:
                    print e
                    continue
        r.close()
        w.close()

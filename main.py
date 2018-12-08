import json
import sys
import time

import divyield

if sys.argv > 1:
    args = json.loads(sys.argv[1])
    # Update the list of symbols.
    if 'action' in args and args['action'] == 'update':
        print divyield.get_symbols()

    if 'action' in args and args['action'] == 'dividends':
        f = open('./symbols.dat', 'r')
        f2 = open('./output.dat', 'w')
        symbols = f.read().split('\n')
        for symbol in symbols:
            history = None
            avg = None
            stdev = None
            print ' '.join(['Computing', symbol])
            try:
                history, avg, stdev = divyield.get_dividends(symbol)
            except Exception, e:
                print e
                continue

            if history and avg and stdev:
                try:
                    stock_price = divyield.get_chart(symbol)
                    dv = float(avg)/float(stock_price)
                    f3 = open('./output.dat', 'a')
                    f3.write(','.join([str(symbol), str(history),
                                       str(stdev), str(dv)])+'\n')
                    f3.close()
                    time.sleep(1)
                except Exception, e:
                    print e
                    continue
        f.close()
        f2.close()

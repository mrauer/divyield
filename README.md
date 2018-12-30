# DivYield

**DivYield** is a sofware designed to catch high payout dividends with low variability and long history.

Current version **0.1**

## Basics
We will be identifying the following attributes at the stock level:
* Number of dividend records (history).
* Standard deviation of the divident amount (variability).
* Average amount [A].
* Current Stock price [B].
* A/B

## Endpoints
* https://api.iextrading.com/1.0/ref-data/symbols (Symbols)
* https://api.iextrading.com/1.0/stock/mmm/chart/1m
* https://api.iextrading.com/1.0/stock/mmm/dividends/5y

## Commands
    python -m virtualenv env
    ./env/bin/python main.py '{"action": "update"}'
    ./env/bin/python main.py '{"action": "dividends"}'
    ./env/bin/python main.py '{"action": "dividends", "qualified": "Q"}' # About 12.7%
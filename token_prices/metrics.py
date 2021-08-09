import quantstats as qs
from pycoingecko import CoinGeckoAPI
import pandas as pd
from datetime import datetime

# import statistics

cg = CoinGeckoAPI()
date = []
eth_price = []

eth_price_history = cg.get_coin_market_chart_by_id(
    id="defipulse-index", vs_currency="usd", days="165"
)
eth_price_dict = eth_price_history["prices"]

for x in eth_price_dict:
    date.append(datetime.fromtimestamp(x[0] / 1000))
    eth_price.append(x[1])

## Parameter ##
total_yield = 0.28
daily_reduction = 0.00105
starting_value = 10000
days = 165
values = []

while days > 0:
    # print(starting_value)
    starting_value = starting_value + (starting_value * (total_yield / 365))
    total_yield = total_yield - daily_reduction
    values.append(starting_value)
    days = days - 1

list_returns_percent_a = [100 * (b - a) / a for a, b in zip(values[::1], values[1::1])]
# print(list_returns_percent_a)
# percents_list = statistics.pstdev(list_returns_percent_a)

# fetch the daily returns for a stock
# stock = qs.utils.download_returns('FB')
# print(stock)
# print(type(stock))
# show sharpe ratio
x = pd.Series(list_returns_percent_a)
from datetime import datetime

date_range = pd.date_range(end=datetime.today(), periods=100).to_pydatetime().tolist()

x.index = date_range
x = x / 100
print(x)
qs.plots.rolling_sharpe(x)

"""
x.index = pd.to_datetime(x.index)
print(x)
qs.reports.full(x)
"""

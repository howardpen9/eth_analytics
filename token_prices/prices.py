from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()
tokens = cg.get_coins_list()
print(tokens)
date = []
eth_price = []
sushi_price = []
dpi_price = []
solana_price = []
avalanche_price = []
binance_price = []
terrausd_price = []
sushi_price = []

# retreive JSONs
eth_price_history = cg.get_coin_market_chart_by_id(
    id="olympus", vs_currency="usd", days="60"
)
dpi_price_history = cg.get_coin_market_chart_by_id(
    id="defipulse-index", vs_currency="usd", days="30"
)

# get prices
eth_price_dict = eth_price_history["prices"]

dpi_price_dict = dpi_price_history["prices"]

for x in eth_price_dict:
    date.append(datetime.fromtimestamp(x[0] / 1000))
    eth_price.append(x[1])

for x in dpi_price_dict:
    date.append(datetime.fromtimestamp(x[0] / 1000))
    dpi_price.append(x[1])

print(date)
print(eth_price)

"""
eth_price = eth_price[::24]
dpi_price = dpi_price[::24]
total_yield = .28
daily_reduction = .00105
starting_value = 10000
days = 180 
values = []
while days > 0: 
    print(starting_value)
    starting_value = starting_value + (starting_value*(total_yield/365))
    total_yield = total_yield - daily_reduction
    values.append(starting_value)
    days = days - 1 

print(len(values))

import statistics
list_returns_percent_a = [100 * (b - a) / a for a, b in zip(dpi_price[::1], dpi_price[1::1])]
print(list_returns_percent_a)
print(statistics.pstdev(list_returns_percent_a))
"""
"""
solana_price_history = cg.get_coin_market_chart_by_id(id='defi-pulseindex', vs_currency='usd', days='30')
price_dict = solana_price_history['prices']
for x in price_dict: 
    solana_price.append(x[1])
"""


import plotly.graph_objects as go
from plotly.subplots import make_subplots


fig = make_subplots(specs=[[{"secondary_y": True}]])


fig.add_trace(
    go.Scatter(x=date, y=eth_price, mode="lines", name="OHM Price", line_color="blue")
)

""""
fig.add_trace(
    go.Scatter(x=date, y=solana_price, mode="lines", name="SOL Price", yaxis="y2")
)
fig.add_trace(
    go.Scatter(x=date, y=avalanche_price, mode="lines", name="AVAX Price", yaxis="y3")
)
fig.add_trace(
    go.Scatter(x=date, y=binance_price, mode="lines", name="BNB Price", yaxis="y4")
)

fig.add_trace(
    go.Scatter(
        x=date, y=terrausd_price, mode="lines", name="TerraUSD Price", line_color="blue"
    )
)
"""

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linewidth=2,
        zeroline=True,
        linecolor="#F4F4F4",
        ticks="outside",
        tickfont=dict(
            family="Arial",
            size=22,
            color="rgb(82, 82, 82)",
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor="#F4F4F4",
        tickfont=dict(
            family="Arial",
            size=22,
            color="blue",
        ),
    ),
    yaxis2=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor="#F4F4F4",
        tickfont=dict(
            family="Arial",
            size=22,
            color="blue",
        ),
    ),
    yaxis3=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor="#F4F4F4",
        tickfont=dict(
            family="Arial",
            size=22,
            color="blue",
        ),
    ),
    yaxis4=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor="#F4F4F4",
        tickfont=dict(
            family="Arial",
            size=22,
            color="blue",
        ),
    ),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    autosize=True,
    plot_bgcolor="white",
)


fig.add_layout_image(
    dict(
        source="https://images.plot.ly/language-icons/api-home/python-logo.png",
        xref="x",
        yref="y",
        x=0,
        y=3,
        sizex=2,
        sizey=2,
        sizing="stretch",
        opacity=0.5,
        layer="below",
    )
)

fig.show()

#!/usr/bin/env python3

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import pandas as pd
import sys
from heikinashi import HA

if len(sys.argv) < 3:
    print('Usage: {} [CryptoInscriber CSV] [Interval (eg. 1Min)]'.format(sys.argv[0]))
    exit(1)

# Sample: ID, Epoch Timestamp, Price, Amount, Side
# 12713989,1510506649000,696594.73102,0.1805,buy

"""Sample backtrader btfeed.GenericCSVData
data = btfeed.GenericCSVData(
    dataname='mydata.csv',

    fromdate=datetime.datetime(2000, 1, 1),
    todate=datetime.datetime(2017, 12, 31),

    nullvalue=0.0,

    dtformat=('%Y-%m-%d %H:%M:%S'),

    datetime=0,
    open=1,
    high=2,
    low=3,
    close=4,
    volume=-1,
    openinterest=-1
)
"""

# Load Raw Trade Feed CSV
df = pd.read_csv(
    sys.argv[1],
    names=['timestamp', 'price', 'amount', 'side'],
    usecols=[1, 2, 3, 4],
    index_col=0
)
print(df.head())

# Convert Epoch Timestampe to Datetime
df.index = pd.to_datetime(df.index, unit='ms')
print(df.head())

# Resample to Specific Interval and Convert to OHLC
ohlc = df['price'].resample(sys.argv[2]).ohlc()
ohlc.to_csv('out.csv')
print(ohlc.head())


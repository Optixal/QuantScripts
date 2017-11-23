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

# Convert OHLC bars to Heikin Ashi
ha = HA(ohlc)
print(ha.head())

# Prepare Plot Data by Converting OHLC
ohlcPlot = ha.reset_index()
ohlcPlot.columns = ['Date', 'Open', 'High', 'Low', 'Close']
ohlcPlot['Date'] = ohlcPlot['Date'].map(mdates.date2num)
print(ohlcPlot.head())

# Plot
fig = plt.figure()
ax1 = plt.subplot2grid((16, 1), (0, 0), rowspan=16, colspan=1)
ax1.xaxis_date()
candlestick_ohlc(
    ax1, ohlcPlot.values, width=0.01, colorup='g', colordown='k', alpha=0.75)
fig.autofmt_xdate()
fig.tight_layout()
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()


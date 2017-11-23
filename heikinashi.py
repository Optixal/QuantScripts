#!/usr/bin/env python3

# OHLC to Heikin Ashi Candlesticks
def HA(df):
    df['HA_close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4

    idx = df.index.name
    df.reset_index(inplace=True)
    for i in range(0, len(df)):
        if i == 0:
            df.at[i, 'HA_open'] = (df.at[i, 'open'] + df.at[i, 'close']) / 2
        else:
            df.at[i, 'HA_open'] = (df.at[i - 1, 'HA_open'] + df.at[i - 1, 'HA_close']) / 2
    if idx:
        df.set_index(idx, inplace=True)

    df['HA_high'] = df[['HA_open', 'HA_close', 'high']].max(axis=1)
    df['HA_low'] = df[['HA_open', 'HA_close', 'low']].min(axis=1)
    df.drop(['open', 'high', 'low', 'close'], 1, inplace=True)
    return df[['HA_open', 'HA_high', 'HA_low', 'HA_close']]


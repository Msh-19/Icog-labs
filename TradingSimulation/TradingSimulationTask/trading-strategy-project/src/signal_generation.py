import pandas as pd
import numpy as np

def detect_fvg(df):
    """
    Detects Fair Value Gaps in OHLC data.
    Parameters:
        df (pd.DataFrame): DataFrame with columns ['open', 'high', 'low', 'close']
    Returns:
        df with additional columns ['fvg_type', 'fvg_top', 'fvg_bottom']
    """
    df = df.copy()
    df['fvg_type'] = 'None'
    df['fvg_top'] = np.nan
    df['fvg_bottom'] = np.nan
    
    for i in range(2, len(df)):
        if df['low'].iloc[i] > df['high'].iloc[i-2]:
            df.at[df.index[i], 'fvg_type'] = 'Bullish'
            df.at[df.index[i], 'fvg_top'] = df['low'].iloc[i]
            df.at[df.index[i], 'fvg_bottom'] = df['high'].iloc[i-2]
        elif df['high'].iloc[i] < df['low'].iloc[i-2]:
            df.at[df.index[i], 'fvg_type'] = 'Bearish'
            df.at[df.index[i], 'fvg_top'] = df['low'].iloc[i-2]
            df.at[df.index[i], 'fvg_bottom'] = df['high'].iloc[i]
    
    return df

def generate_signals(df):
    """
    Generates buy/sell signals based on price interaction with FVGs.
    Parameters:
        df (pd.DataFrame): DataFrame with FVG data
    Returns:
        df with additional column ['signal']
    """
    df['signal'] = 'Hold'
    
    for i in range(1, len(df)):
        if df['fvg_type'].iloc[i-1] == 'Bullish' and not pd.isna(df['fvg_bottom'].iloc[i-1]):
            if df['low'].iloc[i] <= df['fvg_top'].iloc[i-1] and df['low'].iloc[i] >= df['fvg_bottom'].iloc[i-1]:
                df.at[df.index[i], 'signal'] = 'Buy'
        elif df['fvg_type'].iloc[i-1] == 'Bearish' and not pd.isna(df['fvg_top'].iloc[i-1]):
            if df['high'].iloc[i] >= df['fvg_bottom'].iloc[i-1] and df['high'].iloc[i] <= df['fvg_top'].iloc[i-1]:
                df.at[df.index[i], 'signal'] = 'Sell'
    
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/sample_data.csv', parse_dates=['date'], index_col='date')
    df = detect_fvg(df)
    df = generate_signals(df)
    print(df)

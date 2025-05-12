import pandas as pd
import matplotlib.pyplot as plt

def plot_signals(df):
    """
    Plots price data with buy/sell signals.
    Parameters:
        df (pd.DataFrame): DataFrame with OHLC and signal data
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['close'], label='Close Price', color='blue')
    buy_signals = df[df['signal'] == 'Buy']
    plt.scatter(buy_signals.index, buy_signals['close'], marker='^', color='green', label='Buy Signal', s=100)
    sell_signals = df[df['signal'] == 'Sell']
    plt.scatter(sell_signals.index, sell_signals['close'], marker='v', color='red', label='Sell Signal', s=100)
    plt.title('Trading Signals')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig('../outputs/signals_plot.png')
    plt.close()

def plot_performance(df):
    """
    Plots cumulative returns of the strategy.
    Parameters:
        df (pd.DataFrame): DataFrame with signal data
    """
    df['returns'] = 0.0
    for i in range(len(df)-1):
        if df['signal'].iloc[i] == 'Buy' and df['close'].iloc[i+1] > df['close'].iloc[i]:
            df.at[df.index[i], 'returns'] = 0.01
        elif df['signal'].iloc[i] == 'Sell' and df['close'].iloc[i+1] < df['close'].iloc[i]:
            df.at[df.index[i], 'returns'] = 0.01
    
    df['cumulative_returns'] = (1 + df['returns']).cumprod() - 1
    
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['cumulative_returns'], label='Cumulative Returns', color='purple')
    plt.title('Strategy Performance')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid(True)
    plt.savefig('../outputs/performance_plot.png')
    plt.close()

if __name__ == "__main__":
    df = pd.read_csv('../data/sample_data.csv', parse_dates=['date'], index_col='date')
    from signal_generation import detect_fvg, generate_signals
    df = detect_fvg(df)
    df = generate_signals(df)
    plot_signals(df)
    plot_performance(df)

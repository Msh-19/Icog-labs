import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib

def extract_features(df):
    """
    Extracts features for ML model.
    Parameters:
        df (pd.DataFrame): DataFrame with OHLC and signal data
    Returns:
        df with additional feature columns
    """
    df = df.copy()
    df['sma_10'] = df['close'].rolling(window=10).mean()
    df['trend'] = np.where(df['close'] > df['sma_10'], 1, -1)
    df['momentum'] = df['close'].pct_change(5)
    df['has_fvg'] = np.where(df['fvg_type'] != 'None', 1, 0)
    df['tr'] = np.maximum(df['high'] - df['low'], 
                          np.maximum(abs(df['high'] - df['close'].shift(1)), 
                                     abs(df['low'] - df['close'].shift(1))))
    df['atr'] = df['tr'].rolling(window=20).mean()
    return df

def train_signal_model(df):
    """
    Trains a Logistic Regression model to evaluate signal success.
    Parameters:
        df (pd.DataFrame): DataFrame with features and signals
    Returns:
        trained model, scaler, and accuracy
    """
    df['target'] = 0
    for i in range(len(df)-5):
        if df['signal'].iloc[i] == 'Buy' and df['close'].iloc[i+5] > df['close'].iloc[i]:
            df.at[df.index[i], 'target'] = 1
        elif df['signal'].iloc[i] == 'Sell' and df['close'].iloc[i+5] < df['close'].iloc[i]:
            df.at[df.index[i], 'target'] = 1
    
    features = ['trend', 'momentum', 'has_fvg', 'atr']
    df = df.dropna()
    
    X = df[features]
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    joblib.dump(model, '../outputs/model.pkl')
    joblib.dump(scaler, '../outputs/scaler.pkl')
    
    return model, scaler, accuracy

if __name__ == "__main__":
    df = pd.read_csv('../data/sample_data.csv', parse_dates=['date'], index_col='date')
    from signal_generation import detect_fvg, generate_signals
    df = detect_fvg(df)
    df = generate_signals(df)
    df = extract_features(df)
    model, scaler, accuracy = train_signal_model(df)
    print(f"Model Accuracy: {accuracy:.2f}")

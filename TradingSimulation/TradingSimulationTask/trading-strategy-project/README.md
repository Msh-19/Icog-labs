# Trading Strategy Project

This project implements a trading strategy based on Smart Money Concepts (SMC) for Group 6 trainees. It includes signal generation, AI-based signal evaluation, and visualization.

## Folder Structure

- `data/`: Contains OHLC data (replace `sample_data.csv` with real data).
- `src/`: Python scripts for the project.
  - `signal_generation.py`: Detects Fair Value Gaps (FVG) and generates buy/sell signals.
  - `signal_evaluation.py`: Trains a Logistic Regression model to evaluate signal success.
  - `visualization.py`: Plots trading signals and performance.
- `outputs/`: Stores charts and model files.
- `requirements.txt`: Python dependencies.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd trading-strategy-project
   ```

# Install dependencies:
```bash

pip install -r requirements.txt

Replace data/sample_data.csv with real OHLC data (e.g., from yfinance).
```

# Run the scripts:
```bash
python src/signal_generation.py
python src/signal_evaluation.py
python src/visualization.py
```

# Outputs
outputs/signals_plot.png: Chart of price data with buy/sell signals.

outputs/performance_plot.png: Chart of cumulative returns.

outputs/model.pkl: Trained Logistic Regression model.

outputs/scaler.pkl: Feature scaler for the model.

Notes
Use real market data for better results (e.g., via yfinance).

Extend the strategy by adding more SMC patterns (e.g., order blocks).

Experiment with different ML models or features in signal_evaluation.py


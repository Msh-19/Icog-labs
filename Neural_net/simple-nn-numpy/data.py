import numpy as np

def load_data():
    # Dummy dataset (batch of 3 samples, 4 features)
    X = np.array([[1, 2, 3, 2.5],
                  [2.0, 5.0, -1.0, 2.0],
                  [-1.5, 2.7, 3.3, -0.8]])
    y = np.array([0, 1, 1])
    return X, y

# simple-nn-numpy/
# Initial structure with modular files.
# We'll start implementing each module one by one.

# nn_main.py (will serve as the training script)

from layers import Layer_Dense
from activations import Activation_ReLU, Activation_Softmax
from loss import Loss_CategoricalCrossentropy
from optimizer import Optimizer_SGD
from data import load_data
import numpy as np


X, y = load_data()

# Create network architecture
layer1 = Layer_Dense(4, 1)
activation1 = Activation_ReLU()

layer2 = Layer_Dense(1, 1)
activation2 = Activation_ReLU()

layer3 = Layer_Dense(1, 3)
activation3 = Activation_Softmax()

loss_function = Loss_CategoricalCrossentropy()
optimizer = Optimizer_SGD(learning_rate=0.1)

# Training loop
for epoch in range(1000):
    # Forward pass
    layer1.forward(X)
    activation1.forward(layer1.output)

    layer2.forward(activation1.output)
    activation2.forward(layer2.output)

    layer3.forward(activation2.output)
    activation3.forward(layer3.output)

    loss = loss_function.forward(activation3.output, y)
    predictions = np.argmax(activation3.output, axis=1)
    accuracy = np.mean(predictions == y)

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, loss: {loss:.3f}, accuracy: {accuracy:.3f}")

    # Backward pass
    loss_function.backward(activation3.output, y)
    activation3.backward(loss_function.dinputs)
    layer3.backward(activation3.dinputs)

    activation2.backward(layer3.dinputs)
    layer2.backward(activation2.dinputs)

    activation1.backward(layer2.dinputs)
    layer1.backward(activation1.dinputs)

    # Update weights
    optimizer.update_params(layer1)
    optimizer.update_params(layer2)
    optimizer.update_params(layer3)

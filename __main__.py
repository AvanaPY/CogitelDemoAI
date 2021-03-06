import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def map(value, fmin, fmax, tmin, tmax):
    return (value - fmin) / (fmax - fmin) * (tmax - tmin) + tmin

def create_data(from_data, min_value, max_value):
    x = []
    y = []
    for data in from_data:
        x.append(np.array([map(data, min_value, max_value, 0, 1)]))
        if min_value <= data <= max_value:
            y.append(np.array([1, 0]))
        else:
            y.append(np.array([0, 1]))
    return np.array(x), np.array(y)

model = keras.Sequential([
    layers.Dense(1, input_shape=(1,), activation='sigmoid'),
    layers.Dense(15, activation='sigmoid'),
    layers.Dense(15, activation='sigmoid'),
    layers.Dense(2, activation='softmax'),
])

model.compile(
    optimizer=tf.optimizers.Adam(),
    loss=tf.keras.losses.CategoricalCrossentropy(),
    metrics=['acc']
)

s = np.random.normal(loc=25, scale=2.2, size=100000)
X, Y = create_data(s, 22, 28)

model.fit([X], Y, batch_size=64, validation_split=0.2, epochs=25)

import random
tests = np.random.normal(22, 2.2, 100)
for test in tests:
    t = np.array([[map(test, 22, 28, 0, 1)]])
    pred = model.predict(t)

    p_ok = pred[0][0]
    p_no = pred[0][1]
    ok = p_ok > p_no
    act = 22 <= test <= 28

    print(f'Testing on {test:.2f} ({t[0][0]:.2f}): {p_ok:.2f} / {p_no:.2f} => {"Right" if ok == act else "Wrong" }')

# plt.hist(s, 200)
# plt.show()
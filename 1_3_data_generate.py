import numpy as np


RANDOM_SEED = 5
b = 1
w = 2
n = 100

np.random.seed(RANDOM_SEED)
x = np.random.rand(n,1)
epsilon = (0.1 * np.random.randn(n,1))
y = b + w * x + epsilon

print(f"x: {x[:5]}")
print(f"y: {y[:5]}")

idx = np.arange(n)
np.random.shuffle(idx)
split = 0.8
train_idx = idx[:int(n*split)]
valid_idx = idx[int(n*split):]

x_train, y_train = x[train_idx], y[train_idx]
x_valid, y_valid = x[valid_idx], y[valid_idx]

print(f"x_train: {x_train[:5]}")
print(f"y_train: {y_train[:5]}")
print(f"x_valid: {x_valid[:5]}")
print(f"y_valid: {y_valid[:5]}")
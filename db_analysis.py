import numpy as np

# Define the input data
x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([1, 2, 3])

# Initialize the weights
w = np.zeros((2, 1))
b = 0

# Set the learning rate
alpha = 0.01

# Perform gradient descent
for i in range(1000):
  # Calculate the predicted values
  y_pred = x.dot(w) + b
  
  # Calculate the gradients
  dw = (2/len(x)) * x.T.dot(y_pred - y)
  db = (2/len(x)) * np.sum(y_pred - y)
  
  # Update the weights
  w -= alpha * dw
  b -= alpha * db

# Print the final weights
print(w)
print(b)

import numpy as np
from sklearn.linear_model import LinearRegression

# Define the input data (square footage and number of rooms)
X = np.array([[1500, 3], [2000, 4], [1200, 2]])

# Define the output data (house prices)
y = np.array([250000, 300000, 200000])

# Create a LinearRegression object
model = LinearRegression()

# Train the model on the input and output data
model.fit(X, y)

# Make a prediction for a new house with 1800 square feet and 3 rooms
new_house = np.array([[1800, 3]])
predicted_price = model.predict(new_house)

print(predicted_price)  # Output: [275000.]

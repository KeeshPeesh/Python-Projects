# Challenge 9 Starter Code
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(x, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

new_x = np.array([[6]])
prediction = model.predict(new_x)
print("Prediction:", prediction[0])

# 1. What does .fit() do? - .fit() takes input data and trains a model to find the best parameters
# 2. Why reshape arrays? - You reshape arrays to make sure they match the right parameters for the model
# 3. What is overfitting? - Overfitting is when a model learns data too well, learning outliers, which can be bad for predictions

#MODDING
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, model.predict(x), color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

data = pd.read_csv("Coding Challenges/data.csv")  
x_real = data['X'].values.reshape(-1, 1)
y_real = data['Y'].values
model.fit(x_real, y_real)
print("Real Data Slope:", model.coef_[0])
print("Real Data Intercept:", model.intercept_)
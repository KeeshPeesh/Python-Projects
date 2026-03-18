import numpy as np
from sklearn.linear_model import LogisticRegression

hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
pass_fail = [0, 0, 0, 0, 1, 1, 1, 1]

X = np.array(hours_studied).reshape(-1, 1)
y = np.array(pass_fail)

model = LogisticRegression()
model.fit(X, y)

predictions = model.predict(X)
probabilities = model.predict_proba(X)

print("Predictions:")
print(predictions)

print("Probabilities:")
print(probabilities)

new_hours = np.array([[4.5]])
new_prediction = model.predict(new_hours)
new_probability = model.predict_proba(new_hours)

print("New student study hours:", new_hours[0][0])
print("Predicted class:", new_prediction[0])
print("Prediction probabilities:", new_probability[0])
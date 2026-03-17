import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

study_time = np.array([1, 2, 3, 4, 5])
test_scores = np.array([50, 60, 70, 80, 90]) 

plt.scatter(study_time, test_scores)
plt.xlabel('Study Time (hours)')
plt.ylabel('Test Scores')
plt.title('Study Time vs Test Scores')
plt.show()

model = LinearRegression()
model.fit(study_time.reshape(-1, 1), test_scores)

new_study_time = np.array([[6]])
predicted_score = model.predict(new_study_time)
print(f'Predicted test score for {new_study_time[0][0]} hours of study: {predicted_score[0]}')

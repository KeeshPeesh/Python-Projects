import numpy as np
import matplotlib.pyplot as plt

scores = np.array([78, 85, 92, 65, 88, 71, 82, 77, 98])

average = np.mean(scores)
highest = np.max(scores)
lowest = np.min(scores)

plt.hist(scores, bins=5)
plt.title('Score distribution')
plt.xlabel('Score')
plt.ylabel('Count')
plt.show()
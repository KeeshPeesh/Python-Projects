import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(42)
age_cluster1 = np.random.normal(25, 5, 100)
spending_cluster1 = np.random.normal(60, 10, 100)
age_cluster2 = np.random.normal(45, 5, 100)
spending_cluster2 = np.random.normal(30, 10, 100)
ages = np.concatenate((age_cluster1, age_cluster2))
spending_scores = np.concatenate((spending_cluster1, spending_cluster2))
X = np.column_stack((ages, spending_scores))

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.legend()
plt.show()
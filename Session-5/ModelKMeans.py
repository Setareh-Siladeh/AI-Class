import numpy as np
import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = [
    [15, 30],
    [28, 45],
    [75, 65],
    [60, 20],
    [40, 85]
]


np.random.seed(42)
data = np.random.randint(0, 100, size=(30, 2))

model = KMeans(n_clusters=3, random_state=42)
model.fit(data)

print(model.labels_)
print(model.cluster_centers_)

plt.scatter(
    data[:, 0],
    data[:, 1],
    c=model.labels_,
    cmap='viridis',
    s=50
)

plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    color='red',
    marker='X',
    s=200,
    label='Cluster Centers'
)

plt.title('KMeans Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)

plt.show()
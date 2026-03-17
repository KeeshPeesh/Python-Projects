import sklearn
import os
import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("uciml/iris")

print("Path to dataset files:", path)

# Load the dataset
file_path = os.path.join(path, "Iris.csv")
df = pd.read_csv(file_path)

# Get feature names
feature_names = df.columns
print("Feature names:", feature_names)

print("First 5 records:", df.head())

X = df.drop("Species", axis=1)  # Features
y = df["Species"]  # Target variable

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X, y)

predictions = model.predict(X)
print("Predictions:", predictions)
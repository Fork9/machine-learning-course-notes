# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

#####----------EDA---------------#####
# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the keys and descriptions of the dataset
print(digits.keys())
print(digits['DESCR'])

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
# display image 
plt.imshow(digits.images[100], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

#####----------Train Model---------------#####

# Create feature and target arrays
X = digits.data # 8x8 pixel image each pixel representes integer 0 -> 16 
y = digits.target # 0 to 9 digits

print(y)

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors = 7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))


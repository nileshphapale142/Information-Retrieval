import time

start_time = time.time()
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import NearestCentroid, KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
import os
import matplotlib.pyplot as plt
data_folder = "20news-bydate-test"  # Dataset folder name

# Initialize empty lists for data and labels
data = []
labels = []
# Loop through the subdirectories (categories) in your "20news-bydate-test" folder
for category in os.listdir(data_folder):
    category_path = os.path.join(data_folder, category)
    
    if os.path.isdir(category_path):
        # For each category, read the text files
        for filename in os.listdir(category_path):
            file_path = os.path.join(category_path, filename)
            
            # Read the content of the text file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                text = file.read()
            
            data.append(text)
            labels.append(category)

# Step 3: Preprocess the Text Data
tfidf_vectorizer = TfidfVectorizer()
X = tfidf_vectorizer.fit_transform(data)
encoder = LabelEncoder()
y = encoder.fit_transform(labels)

# Step 4: Implement Classifiers
nb_classifier = MultinomialNB()
rocchio_classifier = NearestCentroid()
knn_classifier = KNeighborsClassifier()

# Step 5: Train and Evaluate Classifiers
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nb_classifier.fit(X_train, y_train)
rocchio_classifier.fit(X_train, y_train)
knn_classifier.fit(X_train, y_train)

y_pred_nb = nb_classifier.predict(X_test)
y_pred_rocchio = rocchio_classifier.predict(X_test)
y_pred_knn = knn_classifier.predict(X_test)

# Calculate F-scores
f1_nb = f1_score(y_test, y_pred_nb, average='weighted')
f1_rocchio = f1_score(y_test, y_pred_rocchio, average='weighted')
f1_knn = f1_score(y_test, y_pred_knn, average='weighted')

# Step 6: Compare Results
print("F-score (Naive Bayes):", f1_nb)
print("F-score (Rocchio):", f1_rocchio)
print("F-score (k-Nearest Neighbor):", f1_knn)

# F-scores for each classifier
classifiers = ['Naive Bayes', 'Rocchio', 'k-NN']
f_scores = [f1_nb, f1_rocchio, f1_knn]

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(classifiers, f_scores, color='skyblue')
plt.title('Classifier Comparison for Text Classification')
plt.xlabel('Classifier')
plt.ylabel('F-score')
plt.ylim(0, 1)  # Set the y-axis range (0 to 1)

# Display the F-scores on top of the bars
for i, f_score in enumerate(f_scores):
    plt.text(i, f_score, f'{f_score:.2f}', ha='center', va='bottom', fontsize=12)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")
plt.show()

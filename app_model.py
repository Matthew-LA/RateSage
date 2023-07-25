import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split, KFold
from joblib import dump

# Load the CSV file
data = pd.read_csv('100k_Movies_dataset.csv')

# Delete unwanted columns
columns_to_delete = ['id', 'released_year', 'movie_link']
data = data.drop(columns_to_delete, axis=1)

# Remove rows with NaN values in the 'ratings' column
data = data.dropna(subset=['ratings'])

# Remove rows with unusable descriptions 
data.drop(data[data['Description'] == "#NAME?"].index, inplace=True)
data.drop(data[data['Description'] == "Add a Plot"].index, inplace=True)
data['Description'] = data['Description'].replace(r'\s*\.\.\.\s*See full summary.*', '', regex=True)

# Reorder the columns by moving 'ratings' to the end
cols = list(data.columns)
cols.remove('ratings')
cols.append('ratings')
data = data[cols]

out_file = 'Movie_Data.csv'
data.to_csv(out_file, index=False)

# Load the dataset
data = pd.read_csv('Movie_Data.csv')

# Set the number of samples per rating bin
samples_per_bin = 10000

# Split the dataset into separate DataFrames based on the rating bins
data['bins'] = pd.cut(data['ratings'], bins=[0, 4, 7, 10], labels=[1, 2, 3], include_lowest=True)

# Create a balanced dataset using groupby and sample methods
data_balanced = data.groupby('bins').apply(lambda x: x.sample(samples_per_bin, random_state=42)).reset_index(drop=True)

# Save the modified data to a new CSV file
out_file = 'bal_movie_Data.csv'
data_balanced.to_csv(out_file, index=False)

unknowns = {
    'title': 'UNKNOWN_TITLE',
    'genre': 'UNKNOWN_GENRE',
    'director': 'UNKNOWN_DIRECTOR',
    'cast': 'UNKNOWN_CAST',
    'runtime': 'UNKNOWN_RUNTIME',
    'Description': 'UNKNOW_DESCRIPTION'
}
encoder = LabelEncoder()
# Create a list to hold all unique values and unknowns
all_values = []

for col in ['title', 'genre', 'director', 'cast', 'runtime', 'Description']:
    unique_values = data_balanced[col].unique()
    # Extend all_values with unique_values
    all_values.extend(unique_values)

# Add unknown values
all_values.extend(unknowns.values())

# Remove duplicates
all_values = list(set(all_values))

# Fit the encoder
encoder.fit(all_values)

for col in ['title', 'genre', 'director', 'cast', 'runtime', 'Description']:
    # Now transform the column using the updated encoder
    data_balanced[col] = encoder.transform(data_balanced[col])
    
# Save this updated encoder
dump(encoder, 'encoder.joblib')

# Separate features (X) and target (y)
X_ = data_balanced.drop('ratings', axis=1)
X = X_.drop('bins', axis=1)
y = data_balanced['bins']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
dump(X_train.columns, "feature_names.joblib")

from sklearn.metrics import accuracy_score, confusion_matrix
# Train the Logistic Regression model
lr_model = LogisticRegression(multi_class='ovr', solver='liblinear', max_iter=1000)
#lr_model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
lr_model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = lr_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy: ", accuracy)
print("Confusion Matrix: \n", conf_matrix)
dump(lr_model, 'trained_lr.joblib')
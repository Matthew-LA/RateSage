import pandas as pd
import numpy as np
import joblib 
import sklearn
from joblib import load
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

print(sklearn.__version__)

# Load the saved model and vectorizer
lr_model = joblib.load('trained_lr.joblib')
encoder = joblib.load('encoder.joblib')
feature_names = joblib.load('feature_names.joblib')

title = "The Dark Knight"
genre = "Action, Crime, Drama"
runtime = "152 min"
cast = "Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine, Maggie Gyllenhaal, Gary Oldman, Morgan Freeman"
director = "Christopher Nolan"
description = "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."

#Reorder the columns to match the feature names
input_df = pd.DataFrame({
        'title': [title],
        'genre': [genre],
        'director': [director],
        'cast': [cast],
        'runtime': [runtime],
        'Description': [description]
    })
input_df = input_df[feature_names]


unknowns = {
    'title': 'UNKNOWN_TITLE',
    'genre': 'UNKNOWN_GENRE',
    'director': 'UNKNOWN_DIRECTOR',
    'cast': 'UNKNOWN_CAST',
    'runtime': 'UNKNOWN_RUNTIME',
    'Description': 'UNKNOW_DESCRIPTION'
}

for col in ['title', 'genre', 'director', 'cast', 'runtime', 'Description']:
	labels = encoder.classes_
	input_df[col] = input_df[col].apply(lambda x: x if x in labels else unknowns[col])
	input_df[col] = encoder.transform(input_df[col])

predict_rating = lr_model.predict(input_df)

print(predict_rating)



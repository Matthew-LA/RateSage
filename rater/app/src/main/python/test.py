import pandas as pd
import numpy as np
import joblib
from joblib import load
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from os.path import dirname, join

# Load the saved model, encoder, and feature set
lr_file = join(dirname(__file__), "trained_lr.joblib")
enc_file = join(dirname(__file__), "encoder.joblib")
feat_file = join(dirname(__file__), "feature_names.joblib")

lr_model = joblib.load(lr_file)
encoder = joblib.load(enc_file)
feature_names = joblib.load(feat_file)

def out(title, genre, runtime, cast, director, description):
	s = "title: {} genre: {} runtime: {} cast: {} director: {} description: {}".format(title, genre, runtime, cast, director, description)
	return s

def predict(title, genre, runtime, cast, director, description):

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

    if predict_rating == 1:
        return "1-4"
    elif predict_rating == 2:
        return "5-7"
    elif predict_rating == 3:
        return "8-10"
    else:
        return "Unknown"

# app/model.py
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

def load_resources():
    """Load model, data, and metadata once at startup."""
    autoencoder = load_model('models/autoencoder_model.h5')
    user_item_matrix = np.load('app/user_item_matrix.npy')
    movies = pd.read_csv('app/movies.csv')
    return {
        'model': autoencoder,
        'user_item_matrix': user_item_matrix,
        'movies': movies
    }

def recommend_movies(resources, user_id, top_n=5):
    """Generate top N movie recommendations for a given user."""
    autoencoder = resources['model']
    user_item_matrix = resources['user_item_matrix']
    movies = resources['movies']

    if user_id < 0 or user_id >= user_item_matrix.shape[0]:
        return {"error": "Invalid user_id"}

    user_ratings = user_item_matrix[user_id]
    predicted_ratings = autoencoder.predict(user_ratings.reshape(1, -1))[0]

    unrated_indices = np.where(user_ratings == 0)[0]
    predicted_ratings = [(i, predicted_ratings[i]) for i in unrated_indices]
    top_movies = sorted(predicted_ratings, key=lambda x: x[1], reverse=True)[:top_n]

    recommendations = [
        {"movie_id": idx, "title": movies.loc[idx, 'title'], "score": round(score, 2)}
        for idx, score in top_movies
    ]
    return recommendations

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def extract(file_paths):

    # Load the ratings dataset
    ratings = pd.read_csv(file_paths['ratings'], sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
    
    # Load the movies dataset
    movies = pd.read_csv(file_paths['movies'], sep='|', encoding='latin-1', header=None,
                         names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
                                'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy',
                                'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
                                'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'])
    
    return {'ratings': ratings, 'movies': movies}


def transform(raw_data):

    ratings = raw_data['ratings']
    movies = raw_data['movies']

    # Merge ratings with movie titles
    merged_data = ratings.merge(movies[['movie_id', 'title']], on='movie_id', how='left')

    # Encode user_id and movie_id as sequential indices
    user_encoder = LabelEncoder()
    movie_encoder = LabelEncoder()

    merged_data['user_id'] = user_encoder.fit_transform(merged_data['user_id'])
    merged_data['movie_id'] = movie_encoder.fit_transform(merged_data['movie_id'])

    # Convert the release_date to datetime (optional)
    movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')

    return merged_data


def load(preprocessed_data, save_path=None):

    if save_path:
        preprocessed_data.to_csv(save_path, index=False)
        print(f"Preprocessed data saved to {save_path}")
    return preprocessed_data

# Main function to run the ETL pipeline
def run_etl(file_paths, save_path=None):

    # Extract
    raw_data = extract(file_paths)
    
    # Transform
    preprocessed_data = transform(raw_data)
    
    # Load
    return load(preprocessed_data, save_path)


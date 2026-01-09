# Movie Recommender System

This project explores various movie recommendation techniques, including:

- Content-Based Filtering
- User-Based Collaborative Filtering
- Item-Based Collaborative Filtering
- Neural Network Approaches such as Autoencoders and RNNs

After experimenting with these methods, the final system was implemented using an autoencoder-based model, which has been packaged as a ready-to-use application.

## Project Structure
```text
movie-recommender-system/    
│
├── app/                    <-- main application code
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── movie_id_map.npy
│   ├── movies.csv
│   ├── user_item_matrix.npy
│   └── preprocessed_movielens.csv
│
├── models/                 <-- trained ML models
│   └── autoencoder_model.h5
│
├── data/                  
│   └── ml_100k/            <-- original dataset files
│
├── notebooks/             
│   └── recommender_systems_exploration.ipynb
│
├── test/
│   ├── conftest.py   ← this fixes pytest imports
│   └── test_etl.py
│
├── docker/                
│   └── Dockerfile
│
├── requirements.txt        
├── README.md              
├── LICENSE                 
├── .gitignore       
└── .github/                <-- workflows (CI/CD)
    └── workflows/
        └── python-app.yml

*Note: The `data/ml_100k` folder does not include the dataset. You must download it from [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/) and place it in `data/ml_100k/`.
```

## Installation
```bash
git clone <repo-url>
cd movie-recommender-system
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Run
1. Run the application
```bash
python app/main.py
```

2. Optional: Using Docker
```bash
docker build -t movie-recommender docker/
docker run -p 8000:8000 movie-recommender
```

## CI/CD

This project uses GitHub Actions to automatically run tests on every push and pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

 

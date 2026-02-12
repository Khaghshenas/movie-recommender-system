# Movie Recommender System

This project explores various movie recommendation techniques, including:

- Content-Based Filtering
- User-Based Collaborative Filtering
- Item-Based Collaborative Filtering
- Neural Autoencoder

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

## Evaluation

#### Evaluation Setup

We evaluate the recommender systems under a Top-K recommendation setting using implicit feedback derived from user–item interactions.
All models are trained on the same training split and evaluated on a held-out test set.

For each user, the model produces a ranked list of unseen items. Already-interacted items are excluded from recommendation lists.

#### Metrics

The following ranking-based metrics are reported at cutoff K:

- Precision@K – proportion of recommended items that are relevant

- Recall@K – proportion of relevant items that are successfully recommended

- NDCG@K – normalized discounted cumulative gain, emphasizing top-rank accuracy

These metrics are standard for evaluating implicit-feedback recommender systems, where accurate ranking is more important than rating reconstruction.

#### Models Evaluated

- Item-Based Collaborative Filtering
A classical baseline using item–item similarity computed from user interaction patterns.

- Autoencoder-Based Recommender
A neural recommendation model trained to learn latent user preferences from implicit feedback and generate ranked item recommendations.

#### Results
```text
| Model           | Precision@10 | Recall@10 | NDCG@10 |
|-----------------|--------------|-----------|---------|
| Item-Based CF   | 0.0041       | 0.0035    | 0.0032  |
| Autoencoder     | 0.0307       | 0.0401    | 0.0328  |
```
### Discussion

The autoencoder-based model consistently outperforms Item-Based Collaborative Filtering across all Top-K metrics.

In particular:

- Recall@K shows a substantial improvement, indicating that the autoencoder is significantly better at retrieving relevant items for users.

- NDCG@K improvement demonstrate superior ranking quality, with relevant items appearing closer to the top of recommendation lists.

- Item-based CF struggles due to data sparsity and its reliance on pairwise similarity, which limits its ability to capture complex user preference patterns.

- All values are low because the dataset is sparse (most users rate only a small fraction of movies), which is common in real-world recommender systems.

## Further Improvements / Future Work
Future work could focus on improving recommendation quality by:

- Hybrid Approaches: Combining content-based and collaborative filtering methods to leverage both user preferences and movie features, which can help mitigate cold-start problems for new users or items.

- Advanced Collaborative Filtering: Using matrix factorization or neural collaborative filtering to capture more complex latent patterns in user–item interactions.

- Sequence-Aware Models: Incorporating temporal or sequential information with RNNs or Transformer-based architectures to model evolving user preferences over time.

## CI/CD

This project uses GitHub Actions to automatically run tests on every push and pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

 

import pandas as pd
from app.etl import run_etl

def test_run_etl():
    # Small mock input: create tiny CSVs for testing
    ratings_mock = "user_id\tmovie_id\trating\ttimestamp\n1\t1\t5\t874965758\n2\t2\t3\t875071561"
    movies_mock = "1|Toy Story (1995)|01-Jan-1995||http://example.com|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0\n2|GoldenEye (1995)|01-Jan-1995||http://example.com|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0"

    # Save to temporary files
    with open("tests/ratings_mock.csv", "w") as f:
        f.write(ratings_mock)
    with open("tests/movies_mock.csv", "w") as f:
        f.write(movies_mock)

    file_paths = {
        "ratings": "tests/ratings_mock.csv",
        "movies": "tests/movies_mock.csv"
    }

    # Run ETL
    df = run_etl(file_paths)

    # Check output type
    assert isinstance(df, pd.DataFrame)

    # Check expected columns
    expected_cols = ['user_id', 'movie_id', 'rating', 'timestamp', 'title']
    assert all(col in df.columns for col in expected_cols)

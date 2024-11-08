import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from ranking_methods import bm25_ranking
from preprocessing import preprocess_ingredients

# Load the processed dataset and TF-IDF model
recipes_df = pd.read_csv("processed_recipes.csv")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")

# Define the search function
def search_recipes(query, ranking_method='tf-idf'):
    query_processed = preprocess_ingredients(query.split())
    corpus = recipes_df['processed_ingredients'].tolist()

    if ranking_method == 'tf':
        # Use term frequency (TF) vectorizer
        tf_vectorizer = joblib.load("tf_vectorizer.pkl")
        query_vec = tf_vectorizer.transform([query_processed])
        matrix = joblib.load("tf_matrix.pkl")
        scores = cosine_similarity(query_vec, matrix).flatten()

    elif ranking_method == 'tf-idf':
        # Use TF-IDF vectorizer
        query_vec = vectorizer.transform([query_processed])
        scores = cosine_similarity(query_vec, tfidf_matrix).flatten()

    elif ranking_method == 'bm25':
        # Use BM25 ranking
        scores = bm25_ranking(corpus, query_processed)

    else:
        raise ValueError("Unsupported ranking method")

    # Add scores to the DataFrame and sort results
    recipes_df['score'] = scores
    results = recipes_df.sort_values(by='score', ascending=False).head(5)
    return results[['id', 'ingredients', 'score']].to_dict(orient='records')

# Test the search function
if __name__ == "__main__":
    query = "sugar milk flour"
    results = search_recipes(query, ranking_method='bm25')
    print("Search Results:", results)

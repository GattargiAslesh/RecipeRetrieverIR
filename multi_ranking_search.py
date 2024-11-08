import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from ranking_methods import bm25_ranking
from preprocessing import preprocess_text

# Load the processed dataset and TF-IDF model
recipes_df = pd.read_csv("processed_recipes.csv")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")

# Preprocess the entire corpus
recipes_df['processed_ingredients'] = recipes_df['processed_ingredients'].apply(preprocess_text)
corpus = recipes_df['processed_ingredients'].tolist()

# Define the search function
def search_recipes(query, ranking_method='tf-idf'):
    # Preprocess the query using preprocess_text
    query_processed = preprocess_text(query)

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
    # Test with BM25 ranking method
    query = "sugar milk flour"
    results_bm25 = search_recipes(query, ranking_method='bm25')
    print("BM25 Ranking Results:", results_bm25)

    # Test with TF ranking method
    results_tf = search_recipes("sugar milk flour", ranking_method='tf')
    print("TF Ranking Results:", results_tf)

    # Test with TF-IDF ranking method
    results_tfidf = search_recipes("vanilla extract sugar", ranking_method='tf-idf')
    print("TF-IDF Ranking Results:", results_tfidf)

    # Test with another query for BM25 ranking method
    results_bm25_2 = search_recipes("baking powder eggs", ranking_method='bm25')
    print("BM25 Ranking Results (second query):", results_bm25_2)

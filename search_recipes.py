import pandas as pd
import joblib
from preprocessing import preprocess_ingredients
from sklearn.metrics.pairwise import cosine_similarity

# Load the processed dataset and TF-IDF model
recipes_df = pd.read_csv("processed_recipes.csv")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")

# Define the search function
def search_recipes(query):
    query_processed = preprocess_ingredients(query.split())
    query_vec = vectorizer.transform([query_processed])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-5:][::-1]
    return recipes_df.iloc[top_indices][['id', 'ingredients']].to_dict(orient='records')

# Test the search function
if __name__ == "__main__":
    query = "sugar milk flour"
    results = search_recipes(query)
    print("Search Results:", results)

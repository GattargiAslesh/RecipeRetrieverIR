import pandas as pd
import joblib
from preprocessing import preprocess_ingredients
from sklearn.metrics.pairwise import cosine_similarity
from metrics import precision, recall, f1_score


# Load the processed dataset and TF-IDF model
recipes_df = pd.read_csv("processed_recipes.csv")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")

# Define the search function
def search_recipes(query, relevant_docs=None):
    query_processed = preprocess_ingredients(query.split())
    query_vec = vectorizer.transform([query_processed])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-5:][::-1]
    return recipes_df.iloc[top_indices][['id', 'ingredients']].to_dict(orient='records')

# Test the search function with evaluation
if __name__ == "__main__":
    query = "sugar milk flour"
    relevant_docs = [38948]  # Example relevant document ID
    results = search_recipes(query, relevant_docs=relevant_docs)
    print("Search Results:", results)
    
    # Print evaluation metrics
    from metrics import precision, recall, f1_score
    retrieved_docs = [res['id'] for res in results]
    p = precision(relevant_docs, retrieved_docs)
    r = recall(relevant_docs, retrieved_docs)
    f1 = f1_score(p, r)
    print(f"Evaluation Metrics - Precision: {p:.2f}, Recall: {r:.2f}, F1-Score: {f1:.2f}")

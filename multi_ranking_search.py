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
    query_processed = preprocess_text(query)

    if ranking_method == 'tf':
        tf_vectorizer = joblib.load("tf_vectorizer.pkl")
        query_vec = tf_vectorizer.transform([query_processed])
        matrix = joblib.load("tf_matrix.pkl")
        scores = cosine_similarity(query_vec, matrix).flatten()

    elif ranking_method == 'tf-idf':
        query_vec = vectorizer.transform([query_processed])
        scores = cosine_similarity(query_vec, tfidf_matrix).flatten()

    elif ranking_method == 'bm25':
        scores = bm25_ranking(corpus, query_processed)

    else:
        raise ValueError("Unsupported ranking method")

    # Add scores to the DataFrame and sort results
    recipes_df['score'] = scores
    results = recipes_df.sort_values(by='score', ascending=False).head(5)

    # Create a list of recipe details to display
    recipe_details = []
    for _, row in results.iterrows():
        recipe = {
            "id": row['id'],
            "name": row.get('name', 'Unknown Recipe'),
            "ingredients": row['ingredients'],
            "instructions": row.get('instructions', 'No instructions available'),
            "score": row['score']
        }
        recipe_details.append(recipe)

    return recipe_details

# Test the search function
if __name__ == "__main__":
    query = "chicken rice"
    results = search_recipes(query, ranking_method='bm25')
    for res in results:
        print(f"Recipe ID: {res['id']}")
        print(f"Recipe Name: {res['name']}")
        print(f"Ingredients: {res['ingredients']}")
        print(f"Instructions: {res['instructions']}")
        print(f"Score: {res['score']:.2f}")
        print("-" * 40)

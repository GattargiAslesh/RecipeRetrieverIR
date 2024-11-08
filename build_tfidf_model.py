import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load the processed dataset
recipes_df = pd.read_csv("processed_recipes.csv")

# Initialize the TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(recipes_df['processed_ingredients'])

# Save the vectorizer and the matrix
joblib.dump(tfidf_vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(tfidf_matrix, "tfidf_matrix.pkl")

print("TF-IDF model and matrix saved successfully.")

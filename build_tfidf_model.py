from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load the processed dataset
recipes_df = pd.read_csv("processed_recipes.csv")

# Build the TF-IDF vectorizer and fit the model
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(recipes_df['processed_ingredients'])

# Save the vectorizer and matrix using joblib
import joblib
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(tfidf_matrix, "tfidf_matrix.pkl")

print("TF-IDF model built and saved successfully.")


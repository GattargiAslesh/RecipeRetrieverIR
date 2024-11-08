import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Load the processed dataset
recipes_df = pd.read_csv("processed_recipes.csv")

# Prepare the corpus (list of processed ingredients)
corpus = recipes_df['processed_ingredients'].tolist()

# Step 1: Generate and Save TF Vectorizer and Matrix
print("Generating TF Vectorizer and Matrix...")
tf_vectorizer = CountVectorizer()
tf_matrix = tf_vectorizer.fit_transform(corpus)

# Save TF vectorizer and matrix
joblib.dump(tf_vectorizer, "tf_vectorizer.pkl")
joblib.dump(tf_matrix, "tf_matrix.pkl")
print("TF Vectorizer and Matrix saved successfully!")

# Step 2: Generate and Save TF-IDF Vectorizer and Matrix
print("Generating TF-IDF Vectorizer and Matrix...")
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# Save TF-IDF vectorizer and matrix
joblib.dump(tfidf_vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(tfidf_matrix, "tfidf_matrix.pkl")
print("TF-IDF Vectorizer and Matrix saved successfully!")

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load the cleaned dataset with explicit data types
dtype_spec = {
    'id': 'str',
    'title': 'str',
    'ingredients': 'str',
    'instructions': 'str',
    'cuisine': 'str',
    'processed_text': 'str'
}
print("Loading the cleaned dataset...")
cleaned_df = pd.read_csv('cleaned_combined_recipes_with_steps.csv', dtype=dtype_spec, low_memory=False)

# Initialize the TF-IDF Vectorizer
print("Building the TF-IDF model...")
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(cleaned_df['processed_text'])

# Save the vectorizer and matrix
joblib.dump(tfidf_vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(tfidf_matrix, "tfidf_matrix.pkl")
print("TF-IDF model and matrix saved successfully.")

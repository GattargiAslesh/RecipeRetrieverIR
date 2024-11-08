import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Initialize stopwords and stemmer
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

# Tokenization
def tokenize(text):
    if not text:
        return []
    return nltk.word_tokenize(text.lower())

# Remove Stopwords
def remove_stopwords(tokens):
    return [token for token in tokens if token.isalpha() and token not in stop_words]

# Apply Stemming
def apply_stemming(tokens):
    return [ps.stem(token) for token in tokens]

# Full Preprocessing Function
def preprocess_text(text):
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = apply_stemming(tokens)
    return " ".join(tokens)

# Preprocess a List of Ingredients
def preprocess_ingredients(ingredients_list):
    processed = []
    for ingredient in ingredients_list:
        processed_text = preprocess_text(ingredient)
        processed.append(processed_text)
    return processed

# Test the functions
if __name__ == "__main__":
    sample_ingredients = ["baking powder", "eggs", "all-purpose flour", "raisins", "milk", "white sugar"]
    print("Original Ingredients:", sample_ingredients)

    processed_text = preprocess_text("This is a sample recipe with tomatoes and onions.")
    print("Processed Text:", processed_text)

    processed_ingredients = preprocess_ingredients(sample_ingredients)
    print("Processed Ingredients:", processed_ingredients)

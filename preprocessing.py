import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def tokenize(text):
    return nltk.word_tokenize(text)

def remove_stopwords(tokens):
    return [token for token in tokens if token.lower() not in stop_words]

def apply_stemming(tokens):
    return [ps.stem(token) for token in tokens]

# Test the functions
if __name__ == "__main__":
    sample_text = "This is a sample recipe with tomatoes and onions."
    tokens = tokenize(sample_text)
    tokens_no_stopwords = remove_stopwords(tokens)
    stemmed_tokens = apply_stemming(tokens_no_stopwords)
    print("Tokens:", tokens)
    print("No Stopwords:", tokens_no_stopwords)
    print("Stemmed Tokens:", stemmed_tokens)

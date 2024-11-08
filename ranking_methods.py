import numpy as np
from rank_bm25 import BM25Okapi

# Function to implement BM25 ranking
def bm25_ranking(corpus, query):
    # Tokenize the corpus and query
    tokenized_corpus = [doc.split() for doc in corpus]
    tokenized_query = query.split()

    # Initialize BM25 model
    bm25 = BM25Okapi(tokenized_corpus)

    # Get BM25 scores for the query
    scores = bm25.get_scores(tokenized_query)
    return scores

# Example usage
if __name__ == "__main__":
    sample_corpus = [
        "sugar milk flour",
        "baking powder sugar milk",
        "egg sugar flour milk",
        "butter sugar vanilla",
        "flour sugar milk eggs"
    ]
    query = "sugar milk flour"
    scores = bm25_ranking(sample_corpus, query)
    print("BM25 Scores:", scores)

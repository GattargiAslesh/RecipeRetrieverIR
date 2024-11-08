import pandas as pd
from multi_ranking_search import search_recipes
from metrics import precision, recall, f1_score
from preprocessing import preprocess_text

# Define test queries and their relevant document IDs
test_queries = [
    {"query": "sugar milk flour", "relevant_docs": [38948, 40524]},
    {"query": "vanilla extract sugar", "relevant_docs": [11292, 35074]},
    {"query": "baking powder eggs", "relevant_docs": [19822, 23234]},
    {"query": "olive oil pasta sauce", "relevant_docs": [5436]},
    {"query": "chocolate chips cookies", "relevant_docs": [48059]}
]

# Define the ranking methods to compare
ranking_methods = ['tf', 'tf-idf', 'bm25']

def compare_methods():
    for method in ranking_methods:
        print(f"Evaluating {method.upper()} Ranking Method:")
        for test in test_queries:
            query = test['query']
            relevant_docs = test['relevant_docs']
            query_processed = preprocess_text(query)  # Use consistent preprocessing
            results = search_recipes(query_processed, ranking_method=method)
            retrieved_docs = [res['id'] for res in results]
            p = precision(relevant_docs, retrieved_docs)
            r = recall(relevant_docs, retrieved_docs)
            f1 = f1_score(p, r)
            print(f"Query: '{query}' - Precision: {p:.2f}, Recall: {r:.2f}, F1-Score: {f1:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    compare_methods()

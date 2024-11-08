import pandas as pd
from multi_ranking_search import search_recipes
from metrics import precision, recall, f1_score

# Define test queries and their relevant document IDs
test_queries = [
    {"query": "sugar milk flour", "relevant_docs": [38948]},
    {"query": "vanilla extract sugar", "relevant_docs": [11433]},
    {"query": "baking powder eggs", "relevant_docs": [6789]},
    {"query": "olive oil pasta sauce", "relevant_docs": [43969]},
    {"query": "chocolate chips cookies", "relevant_docs": [40524]}
]

# Define the ranking methods to compare
ranking_methods = ['tf', 'tf-idf', 'bm25']

def compare_methods():
    for method in ranking_methods:
        print(f"Evaluating {method.upper()} Ranking Method:")
        for test in test_queries:
            query = test['query']
            relevant_docs = test['relevant_docs']
            # Perform search using the specified ranking method
            results = search_recipes(query, ranking_method=method)
            # Extract the retrieved document IDs
            retrieved_docs = [res['id'] for res in results]

            # Calculate evaluation metrics
            p = precision(relevant_docs, retrieved_docs)
            r = recall(relevant_docs, retrieved_docs)
            f1 = f1_score(p, r)

            # Print the evaluation results
            print(f"Query: '{query}'")
            print(f"Precision: {p:.2f}, Recall: {r:.2f}, F1-Score: {f1:.2f}\n")
        print("-" * 40)

if __name__ == "__main__":
    compare_methods()

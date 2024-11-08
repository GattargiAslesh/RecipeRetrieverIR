import pandas as pd
from ranking_methods import bm25_ranking
from preprocessing import preprocess_ingredients

# Load the processed dataset
recipes_df = pd.read_csv("processed_recipes.csv")
recipes_df['processed_tokens'] = recipes_df['processed_ingredients'].apply(lambda x: x.split())

# Search function with BM25 option
def search_recipes(query, ranking_method='bm25'):
    query_processed = preprocess_ingredients(query.split())
    corpus = recipes_df['processed_ingredients'].tolist()

    if ranking_method == 'bm25':
        scores = bm25_ranking(corpus, query_processed)
        recipes_df['score'] = scores
    else:
        raise ValueError("Unsupported ranking method")

    # Sort results by score
    results = recipes_df.sort_values(by='score', ascending=False).head(5)
    return results[['id', 'ingredients', 'score']].to_dict(orient='records')

# Example test
if __name__ == "__main__":
    query = "sugar milk flour"
    results = search_recipes(query, ranking_method='bm25')
    print("Search Results:", results)

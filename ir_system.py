from dataset import load_recipes
from preprocessing import tokenize, remove_stopwords, apply_stemming
from ranking import calculate_idf, rank_recipes

recipes = load_recipes()
idf = calculate_idf(recipes)

def run_query(query):
    tokens = tokenize(query)
    tokens = remove_stopwords(tokens)
    tokens = apply_stemming(tokens)
    results = rank_recipes(tokens, recipes, idf)
    return results

# Test the system
if __name__ == "__main__":
    query = "tomato spaghetti"
    print("Query Results:", run_query(query))

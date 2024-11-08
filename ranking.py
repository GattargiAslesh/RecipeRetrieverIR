from collections import Counter
import math

def calculate_tf(tokens):
    tf = Counter(tokens)
    return {term: count / len(tokens) for term, count in tf.items()}

def calculate_idf(recipes):
    num_docs = len(recipes)
    idf = {}
    all_tokens = set(token for recipe in recipes for token in recipe["ingredients"])
    for token in all_tokens:
        containing_docs = sum(1 for recipe in recipes if token in recipe["ingredients"])
        idf[token] = math.log(num_docs / (1 + containing_docs))
    return idf

def rank_recipes(query_tokens, recipes, idf):
    ranked_recipes = []
    for recipe in recipes:
        recipe_tokens = recipe["ingredients"]
        tf = calculate_tf(recipe_tokens)
        tf_idf = {term: tf[term] * idf.get(term, 0) for term in tf}
        score = sum(tf_idf.get(token, 0) for token in query_tokens)
        ranked_recipes.append((recipe["name"], score))
    ranked_recipes.sort(key=lambda x: x[1], reverse=True)
    return [recipe[0] for recipe in ranked_recipes if recipe[1] > 0]

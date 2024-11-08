import json

def load_recipes():
    with open("recipes.json", "r") as file:
        return json.load(file)

# Test the function
if __name__ == "__main__":
    recipes = load_recipes()
    print(f"Loaded {len(recipes)} recipes.")

import json
import pandas as pd

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Load and combine train and test datasets
def load_recipe_ingredients_data():
    train_data = load_json("Datasets/Recipe Ingredients Dataset/train.json")
    test_data = load_json("Datasets/Recipe Ingredients Dataset/test.json")

    # Combine the datasets
    combined_data = train_data + test_data
    df = pd.DataFrame(combined_data)
    return df

# Test the function
if __name__ == "__main__":
    recipes_df = load_recipe_ingredients_data()
    print(f"Loaded {len(recipes_df)} recipes.")
    print(recipes_df.head())


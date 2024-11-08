from load_dataset import load_recipe_ingredients_data 
from preprocessing import preprocess_ingredients
import pandas as pd

# Load the dataset
recipes_df = load_recipe_ingredients_data()

# Apply preprocessing to the ingredients column
recipes_df['processed_ingredients'] = recipes_df['ingredients'].apply(preprocess_ingredients)

# Save the processed dataset for future use
recipes_df.to_csv("processed_recipes.csv", index=False)

# Print a sample of the processed data
if __name__ == "__main__":
    print("Sample of Processed Data:")
    print(recipes_df[['id', 'ingredients', 'processed_ingredients']].head())

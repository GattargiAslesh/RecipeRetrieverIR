import pandas as pd

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

if __name__ == "__main__":
    dataset = load_dataset("processed_recipes.csv")
    print(dataset.head())

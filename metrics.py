def precision(relevant, retrieved):
    return len(set(relevant) & set(retrieved)) / len(retrieved)

def recall(relevant, retrieved):
    return len(set(relevant) & set(retrieved)) / len(relevant)

def f1_score(precision, recall):
    return 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Example usage
if __name__ == "__main__":
    relevant = ["Spaghetti Bolognese", "Vegan Tacos"]
    retrieved = ["Spaghetti Bolognese", "Chicken Curry"]
    p = precision(relevant, retrieved)
    r = recall(relevant, retrieved)
    f1 = f1_score(p, r)
    print(f"Precision: {p}, Recall: {r}, F1-Score: {f1}")

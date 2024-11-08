from sklearn.metrics import precision_score, recall_score, f1_score

def precision(true_labels, predicted_labels):
    return precision_score(true_labels, predicted_labels, average='binary')

def recall(true_labels, predicted_labels):
    return recall_score(true_labels, predicted_labels, average='binary')

def f1_score(true_labels, predicted_labels):
    return f1_score(true_labels, predicted_labels, average='binary')

# **Recipe Information Retrieval System**

A robust and efficient Information Retrieval (IR) system tailored for recipe searches, integrating multiple datasets and advanced IR techniques to provide users with relevant recipes through a Telegram bot interface.

---

## **Table of Contents**

1. [Introduction](#introduction)
2. [Features](#features)
3. [System Architecture](#system-architecture)
4. [Datasets Used](#datasets-used)
5. [Techniques Implemented](#techniques-implemented)
6. [Telegram Bot Integration](#telegram-bot-integration)
7. [Installation](#installation)
8. [Usage](#usage)
9. [Evaluation Metrics](#evaluation-metrics)
10. [Observations and Results](#observations-and-results)
11. [Future Work](#future-work)
12. [Contributors](#contributors)

---

## **Introduction**

The Recipe Information Retrieval System combines data preprocessing, ranking algorithms, and evaluation metrics to retrieve the most relevant recipes based on user queries. The system integrates three datasets and supports user interaction via a Telegram bot for real-time recipe searches.

---

## **Features**

- **Preprocessing**: Tokenization, stemming, and stopword removal.
- **Ranking Methods**: Supports TF, TF-IDF, and BM25 for improved search relevance.
- **Evaluation**: Implements Precision, Recall, F1-Score, DCG, and NDCG for performance analysis.
- **Telegram Bot**: Provides an easy-to-use interface for querying recipes.
- **Scalable Datasets**: Utilizes datasets containing millions of recipes for robust testing and retrieval.

---

## **System Architecture**

The system comprises the following components:

1. **Preprocessing Module**: Cleans and standardizes data through tokenization, stemming, and stopword removal.
2. **Ranking Module**: Implements TF, TF-IDF, and BM25 ranking methods.
3. **Evaluation Module**: Analyzes system performance using various metrics.
4. **Telegram Bot**: Enables real-time user interaction for recipe searches.

**Workflow**:
1. Query → Preprocessing → Ranking → Evaluation → Telegram Bot
2. Results are displayed to the user with relevant recipes, ingredients, and instructions.

---

## **Datasets Used**

1. **[Kaggle Recipe Dataset](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset)**:  
   - ~60,000 recipes with ingredients and cuisine types.  
   - Provides a diverse recipe pool.

2. **[RecipeQA Dataset](https://hucvl.github.io/recipeqa/)**:  
   - ~1,900 recipes with step-by-step instructions.  
   - Focuses on detailed instructional retrieval.

3. **[RecipeNLG Dataset](https://www.kaggle.com/datasets/saldenisov/recipenlg)**:  
   - 2.2M recipes with structured fields (title, ingredients, directions).  
   - Suitable for large-scale testing.

---

## **Techniques Implemented**

### **Preprocessing**
- **Tokenization**: Splits text into meaningful units. Implemented default and regex-based methods.  
- **Stemming**: Reduces words to base forms. Compared stemming vs. no stemming.  
- **Stopword Removal**: Filters irrelevant words like "and," "the," etc.

### **Ranking**
- **TF (Term Frequency)**: Ranks documents based on term frequency.  
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Weighs terms by importance across documents.  
- **BM25**: Combines term frequency and document normalization for enhanced relevance.

### **Evaluation**
- Metrics Used:  
  - Precision, Recall, F1-Score, DCG, and NDCG.  
  - BM25 achieved the highest performance across all metrics.

---

## **Telegram Bot Integration**

The Telegram bot allows real-time recipe retrieval via simple queries. Example commands:  
- `/recipe bm25 Pancakes`  
- `/recipe tf vegan cookies`

**Features**:
1. Supports multi-method ranking (TF, TF-IDF, BM25).  
2. Displays results with ingredients, instructions, and scores.  
3. User-friendly and scalable for large datasets.

---

## **Installation**

### **Requirements**
- Python 3.8 or higher
- Libraries: Install dependencies using `pip install -r requirements.txt`.

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/GattargiAslesh/RecipeRetrieverIR.git
   cd RecipeRetrieverIR
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the Telegram bot:
   - Obtain a bot token from [BotFather](https://t.me/BotFather).  
   - Replace `TELEGRAM_BOT_TOKEN` in `telegram_bot.py` with your token.  

4. Run the system:
   ```bash
   python telegram_bot.py
   ```

---

## **Usage**

1. Query recipes via the Telegram bot:
   - `/recipe tf Chicken Rice`
   - `/recipe bm25 Vegan Cookies`

2. Modify the ranking method and observe results:
   - TF, TF-IDF, BM25.

3. Evaluate system performance using metrics.

---

## **Evaluation Metrics**

| **Metric**   | **TF** | **TF-IDF** | **BM25** |
|--------------|--------|------------|----------|
| Precision    | 0.60   | 0.72       | 0.80     |
| Recall       | 0.58   | 0.68       | 0.74     |
| F1-Score     | 0.59   | 0.70       | 0.77     |
| NDCG         | 0.65   | 0.78       | 0.85     |

---

## **Observations and Results**

1. **BM25** consistently outperformed TF and TF-IDF in relevance and ranking quality.
2. Stemming slightly improved recall but reduced precision.
3. Stopword removal enhanced query matching accuracy.

---

## **Future Work**

1. Implement advanced neural ranking models like BERT.
2. Integrate user feedback for personalization.
3. Optimize system for large-scale real-time deployment.

---

## **Contributors**

- **Aslesh Gattargi**: Lead Developer  

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

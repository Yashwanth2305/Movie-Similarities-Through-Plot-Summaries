# Movie Similarities Through Plot Summaries

This project analyzes movie plot summaries using **Natural Language Processing (NLP)** to find thematic and narrative similarities between films. It focuses on the storyline rather than ratings, cast, or crew, enabling unique and content-driven recommendations.

## Features
- Extracts key elements from plot summaries
- Measures similarity between movies using text processing
- Clusters movies with related themes and storylines
- Useful for recommendations, trend analysis, and creative research

## Technologies Used
- Python
- NLTK / spaCy
- Scikit-learn
- Pandas

## How It Works
1. Collect plot summaries from a dataset (e.g., IMDb, TMDb).
2. Preprocess text (tokenization, stopword removal, lemmatization).
3. Convert text to numerical vectors using TF-IDF or word embeddings.
4. Calculate similarities using cosine similarity.
5. Output recommendations or similarity clusters.

## Installation
```bash
git clone https://github.com/your-username/movie-similarities.git
cd movie-similarities
pip install -r requirements.txt
Usage
bash
Copy
Edit
python main.py
Example Output
diff
Copy
Edit
Movies similar to 'Inception':
- Shutter Island
- The Matrix
- Interstellar

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load the pre-trained model and vectorizer from the pickle file
with open('movie_recommendation_model.pkl', 'rb') as model_file:
    vectorizer, model, df = pickle.load(model_file)

def get_recommendations(plot_summary):
    # Transform the input plot summary
    plot_vec = vectorizer.transform([plot_summary])
    # Find the nearest neighbors
    distances, indices = model.kneighbors(plot_vec)
    # Get the movie titles for the closest matches
    recommendations = df.iloc[indices[0]]['title'].tolist()
    return recommendations

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    plot_summary = data['plot']
    recommendations = get_recommendations(plot_summary)
    return jsonify({'similarMovies': recommendations})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, request, jsonify
import numpy as np

import os
import pickle

# Obter o diretório atual do arquivo
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '../model/best_sentiment_model.pkl')
vectorizer_path = os.path.join(current_dir, '../model/vectorizer.pkl')

# Definição da Blueprint
api = Blueprint('api', __name__)

# Carregar modelo e vetorizador
with open(model_path, 'rb') as f:
    model = pickle.load(f)
with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

@api.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    print("Texto:", data)
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Vetorizar e prever
    vectorized_text = vectorizer.transform([text])
    probabilities = model.predict_proba(vectorized_text)[0]
    print("Prob: ", probabilities)
    labels = model.classes_  # ['negative', 'neutral', 'positive']
    print("labels: ", labels)
    # Formatar resposta com as chaves 'negative', 'neutral', 'positive'
    response = {
        'sentiment_percentages': {
            'negative': round(float(probabilities[0]), 2),
            'positive': round(float(probabilities[1]), 2)
        }
    }
    
    return jsonify(response)
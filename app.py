from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import torch

app = Flask(__name__)

# Initialize the emotion detection pipeline
emotion_analyzer = pipeline("text-classification", 
                          model="j-hartmann/emotion-english-distilroberta-base",
                          return_all_scores=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    text = request.json.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Get emotion predictions
    results = emotion_analyzer(text)[0]
    
    # Sort emotions by score
    emotions = sorted(results, key=lambda x: x['score'], reverse=True)
    
    return jsonify({
        'emotions': emotions,
        'dominant_emotion': emotions[0]['label'],
        'confidence': emotions[0]['score']
    })

if __name__ == '__main__':
    app.run(debug=True) 

#to run this python app.py
#to quit the server ctrl+c

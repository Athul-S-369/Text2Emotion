# AI-Powered Emotion Detector

This is a web application that uses artificial intelligence to detect emotions from text input. It uses the DistilRoBERTa model fine-tuned for emotion classification to analyze text and provide detailed emotion analysis.

## Features

- Real-time emotion analysis
- Modern, responsive UI
- Detailed emotion breakdown with confidence scores
- Support for various emotions including joy, sadness, anger, fear, surprise, and love

## Setup

1. Make sure you have Python 3.7+ installed on your system.

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Enter any text in the input field
2. Click "Analyze Emotion"
3. View the results showing:
   - Dominant emotion with confidence score
   - Detailed breakdown of all detected emotions
   - Visual representation of emotion intensities

## Technical Details

- Backend: Flask (Python)
- Frontend: HTML, JavaScript, TailwindCSS
- AI Model: DistilRoBERTa fine-tuned for emotion classification
- API: Hugging Face Transformers

## Note

The first time you run the application, it will download the required model files which might take a few minutes depending on your internet connection. 
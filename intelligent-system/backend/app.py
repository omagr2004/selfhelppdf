from flask import Flask, request, jsonify
from services.pdf_extraction import extract_text_from_pdf
from services.web_scraping import fetch_data
from services.nlp_tasks import analyze_sentiment, answer_question

app = Flask(__name__)

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    text = extract_text_from_pdf(file)
    return jsonify({'extracted_text': text})

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    scraped_data = fetch_data(url)
    return jsonify({'scraped_data': scraped_data})

@app.route('/analyze_sentiment', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    sentiment = analyze_sentiment(text)
    return jsonify({'sentiment': sentiment})

@app.route('/answer_question', methods=['POST'])
def answer():
    data = request.json
    question = data.get('question')
    context = data.get('context')
    if not question or not context:
        return jsonify({'error': 'Question and context are required'}), 400
    answer = answer_question(question, context)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
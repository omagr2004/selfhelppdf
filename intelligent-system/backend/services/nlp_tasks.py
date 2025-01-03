from transformers import pipeline, BertTokenizer, BertForSequenceClassification
import torch

# Initialize sentiment analysis and question answering pipelines with specific models
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
question_answerer = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Load custom sentiment analysis model
sentiment_tokenizer = BertTokenizer.from_pretrained('./sentiment_model')
sentiment_model = BertForSequenceClassification.from_pretrained('./sentiment_model')

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using the custom model.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing the sentiment label and score.
    """
    inputs = sentiment_tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    outputs = sentiment_model(**inputs)
    logits = outputs.logits
    sentiment = torch.argmax(logits, dim=1).item()
    return {'label': 'positive' if sentiment == 1 else 'negative', 'score': torch.softmax(logits, dim=1).max().item()}

def answer_question(question, context):
    """
    Answers a question based on the provided context.

    Args:
        question (str): The question to answer.
        context (str): The context in which to find the answer.

    Returns:
        dict: A dictionary containing the answer and its score.
    """
    return question_answerer(question=question, context=context)
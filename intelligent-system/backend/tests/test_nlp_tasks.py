import unittest
from backend.services.nlp_tasks import analyze_sentiment, answer_question

class TestNlpTasks(unittest.TestCase):

    def test_analyze_sentiment_positive(self):
        text = "I love this product! It's amazing."
        result = analyze_sentiment(text)
        self.assertEqual(result, 'positive')

    def test_analyze_sentiment_negative(self):
        text = "I hate this product. It's the worst."
        result = analyze_sentiment(text)
        self.assertEqual(result, 'negative')

    def test_analyze_sentiment_neutral(self):
        text = "This product is okay."
        result = analyze_sentiment(text)
        self.assertEqual(result, 'neutral')

    def test_answer_question(self):
        question = "What is the capital of France?"
        context = "The capital of France is Paris."
        result = answer_question(question, context)
        self.assertEqual(result, "Paris")

    def test_answer_question_no_answer(self):
        question = "What is the capital of Germany?"
        context = "The capital of France is Paris."
        result = answer_question(question, context)
        self.assertEqual(result, "I don't know.")

if __name__ == '__main__':
    unittest.main()
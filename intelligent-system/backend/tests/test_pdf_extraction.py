import unittest
from services.pdf_extraction import extract_text_from_pdf

class TestPDFExtraction(unittest.TestCase):

    def test_extract_text_from_valid_pdf(self):
        text = extract_text_from_pdf('tests/sample_valid.pdf')
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)

    def test_extract_text_from_empty_pdf(self):
        text = extract_text_from_pdf('tests/sample_empty.pdf')
        self.assertEqual(text, '')

    def test_extract_text_from_nonexistent_pdf(self):
        with self.assertRaises(FileNotFoundError):
            extract_text_from_pdf('tests/nonexistent.pdf')

    def test_extract_text_from_pdf_with_images(self):
        text = extract_text_from_pdf('tests/sample_with_images.pdf')
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)

if __name__ == '__main__':
    unittest.main()
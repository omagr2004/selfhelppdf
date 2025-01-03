import unittest
from backend.services.web_scraping import fetch_data

class TestWebScraping(unittest.TestCase):

    def test_fetch_data_valid_url(self):
        url = "https://example.com"
        data = fetch_data(url)
        self.assertIn("Example Domain", data)  # Check for expected content

    def test_fetch_data_invalid_url(self):
        url = "https://invalid-url.com"
        with self.assertRaises(Exception):  # Expecting an exception for invalid URL
            fetch_data(url)

    def test_fetch_data_empty_url(self):
        url = ""
        with self.assertRaises(ValueError):  # Expecting a ValueError for empty URL
            fetch_data(url)

if __name__ == '__main__':
    unittest.main()
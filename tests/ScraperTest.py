import unittest
from main.Scraper import Scraper

class ScraperTest(unittest.TestCase):
    def test_get_data(self):
        scraper = Scraper("Trustpilot")
        url = "https://www.trustpilot.com/review/www.monzo.com"
        data = scraper.get_data(url)
        self.assertIsNotNone(data)
if __name__ == '__main__':
    unittest.main()

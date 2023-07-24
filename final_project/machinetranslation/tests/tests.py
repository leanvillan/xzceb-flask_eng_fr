import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_english_to_french_hello(self):
        result = englishToFrench('Hello')
        self.assertEqual(result, 'Bonjour')

    def test_english_to_french_other_word(self):
        result = englishToFrench('Apple')
        self.assertEqual(result, 'Pomme')

    def test_french_to_english_bonjour(self):
        result = frenchToEnglish('Bonjour')
        self.assertEqual(result, 'Hello')

    def test_french_to_english_other_word(self):
        result = frenchToEnglish('Pomme')
        self.assertEqual(result, 'Apple')

if __name__ == '__main__':
    unittest.main()

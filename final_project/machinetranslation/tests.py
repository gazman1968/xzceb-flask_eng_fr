""" This is Translator Unittest Module """
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """ This is the start of the test sequence """

    def test_french_to_english_with_null_input(self):
        """ f2e null test follows """
        result = french_to_english(None)
        self.assertIsNone(result)

    def test_english_to_french_with_null_input(self):
        """ e2f null test follows """
        result = english_to_french(None)
        self.assertIsNone(result)

    def test_english_to_french_with_hello(self):
        """ Translation test Hello - Bonjour follows """
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

    def test_french_to_english_with_bonjour(self):
        """ Translation test Bonjour - Hello follows """
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

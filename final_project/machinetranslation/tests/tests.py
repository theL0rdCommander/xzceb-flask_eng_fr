import unittest
import translator

class TestMyModule(unittest.TestCase):
	
    def test_frenchToEnglish(self): # 'test_' is required
	    self.assertEqual(translator.frenchToEnglish('Bonjour'),'Hello')

    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench('Hello'),'Bonjour')

    def test_frenchToEnglishNull(self): # 'test_' is required
        self.assertEqual(translator.frenchToEnglish(''), '')

    def test_englishToFrenchNull(self):
        self.assertEqual(translator.englishToFrench(''), '')

if __name__ == '__main__':
    unittest.main()

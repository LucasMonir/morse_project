import unittest;
from modules.loader import load_morse

class TestMorseLoader(unittest.TestCase):

    def test_basic_loading(self):
        data = load_morse('mock_morse.json');
        self.assertIsInstance(data, dict);

if __name__ == 'main':
    unittest.main();
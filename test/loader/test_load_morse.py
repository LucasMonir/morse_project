import unittest;
from pathlib import Path;
from modules.loader import Loader;

class TestMorseLoader(unittest.TestCase):

    def test_basic_loading(self):
            path = Path(__file__).parent / "mock_morse.json"
            data = Loader.load_morse(path);
            self.assertIsInstance(data, dict);

if __name__ == 'main':
    unittest.main();
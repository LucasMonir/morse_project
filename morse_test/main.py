import json;
from pathlib import Path;

morse = {}

def load_morse():
    base_dir = Path(__file__).parent;
    morse_path = base_dir/"resources"/"morse.json";

    try:
        with open(morse_path, "r") as f:
            morse = json.load(f);
            print('Morse directory loaded');
    except:
        print(f'Failed loading morse dictionary at directory: {morse_path}');


def main():
    load_morse();

if __name__ == '__main__':
   main()
import json;
from pathlib import Path;


def load_morse(path):
    try:
        with open(path, "r") as morse_file:
            morse = json.load(morse_file)

            if not morse:          
                raise ValueError('Morse dictionary is empty or invalid')

            print('Morse dictionary loaded');

            return morse;
    except:
        print(f'Failed loading morse dictionary at directory: {path}');
 

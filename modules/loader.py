import json;
from pathlib import Path;

class Loader():

    def load_morse(path):

            with open(path, "r") as morse_file:
                morse = json.load(morse_file)

                if not morse:          
                    raise ValueError('Morse dictionary is empty or invalid')

                print('Morse dictionary loaded!');

                return morse;
            print(f'Failed loading morse dictionary at directory: {path}, error: {ex}');

    def load_text_to_convert(path):
            with open(path, "r") as text:
                content = text.read();

                if not content:
                    raise ValueError("Source text file is empty");
                
                print('Source text file loaded!')
                return content;
            

from pathlib import Path
from modules.loader import Loader;
from tkinter import Tk;
from tkinter.filedialog import askopenfilename;

base_dir = Path(__file__).parent;
morse_path = base_dir / "resources" / "morse.json";

def main():
    Tk().withdraw();
    morse_dict = Loader.load_morse(morse_path);

    source_file_path = askopenfilename();
    source_text = Loader.load_text_to_convert(source_file_path);

    convert(source_text, morse_dict)

def convert(text, morse_dict):
    for key in text:
        if morse_dict.get(key.lower()):
            print(morse_dict.get(key.lower()))
        else:
            print(f'not codifiable: "{key}"')


if __name__ == '__main__':
   main();
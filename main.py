from pathlib import Path
from modules.loader import  load_morse;

morse = {}
base_dir = Path(__file__).parent;
morse_path = base_dir / "resources" / "morse.json";

def main():
    morse = load_morse(morse_path);

if __name__ == '__main__':
   main()
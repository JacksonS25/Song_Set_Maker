import sys
from functions import generate_song_set
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <song_name> <song_name> ... <output_filename>")
        sys.exit(1)
    
    BASE_DIR = Path(__file__).resolve().parent
    SONGS_DIR = BASE_DIR / "songs"

    song_list = []
    for i in range(1, len(sys.argv) - 1):
        pdf_path = SONGS_DIR / f"{sys.argv[i]}.pdf"
        if pdf_path.exists():
            song_list.append(pdf_path)
        else:
            print(f"Song not found: {sys.argv[i]}")

    output_filepath = BASE_DIR / "set_lists" / f"{sys.argv[-1]}.pdf"
    generate_song_set(song_list, output_filepath)


main()
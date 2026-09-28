import sys
import io
from generate import generate_song_set
from pathlib import Path
from emailer import send_gmail_pdf

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 main.py <song name> <song name> ... <output_filename> <email_address>")
        sys.exit(1)
    
    BASE_DIR = Path(__file__).resolve().parent
    SONGS_DIR = BASE_DIR / "songs"

    song_list = []
    for i in range(1, len(sys.argv) - 2):
        pdf_path = SONGS_DIR / f"{sys.argv[i]}.pdf"
        if pdf_path.exists():
            print(f"Adding Song: {sys.argv[i]}")
            song_list.append(pdf_path)
        else:
            print(f"Song not found: {sys.argv[i]}")
            print("Please check the song name and try again.")
            sys.exit(1)

    output_filename = sys.argv[-2]
    email_address = sys.argv[-1]

    buffer = io.BytesIO()
    generate_song_set(song_list, buffer)

    send_gmail_pdf(buffer, email_address, output_filename)



main()
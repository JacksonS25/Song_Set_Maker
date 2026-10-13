import sys
import io
from pathlib import Path
from generate import generate_song_set
from emailer import send_gmail_pdf

USAGE = (
    "Usage: <song name>, <song name>, ..., <output name>, <email>\n"
    "Example: Amazing Grace, How Great Thou Art, Sunday Set, you@example.com\n"
    "Type 'list' to see available songs."
)

def find_song(songs_dir, name):
    wanted = name.strip().lower()
    for pdf in songs_dir.glob("*.pdf"):
        if pdf.stem.lower() == wanted:
            return pdf
    return None

def main():
    songs_dir = Path(__file__).resolve().parent / "songs"
    args = sys.argv[1:]

    if not args:
        print(USAGE)
        sys.exit(1)

    if args[0] in ("--help", "-h"):
        print(USAGE)
        sys.exit(0)

    if args[0] in ("--list", "-l"):
        print("Available songs:")
        for pdf in sorted(songs_dir.glob("*.pdf"), key=lambda p: p.stem.lower()):
            print(f"- {pdf.stem}")
        sys.exit(0)

    if len(args) < 3:  # at least one song + output name + email
        print(USAGE)
        sys.exit(1)

    *song_names, output_filename, email_address = args

    song_list = []
    for name in song_names:
        pdf_path = find_song(songs_dir, name)
        if pdf_path is None:
            print(f"Song not found: {name}")
            print("Type 'list' to see the exact song names.")
            sys.exit(1)
        print(f"Adding Song: {pdf_path.stem}")
        song_list.append(pdf_path)

    if not output_filename.lower().endswith(".pdf"):
        output_filename += ".pdf"

    buffer = io.BytesIO()
    generate_song_set(song_list, buffer)

    if not send_gmail_pdf(buffer, email_address, output_filename):
        sys.exit(1)

if __name__ == "__main__":
    main()
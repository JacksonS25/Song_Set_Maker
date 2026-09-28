from pypdf import PdfReader, PdfWriter

def generate_song_set(song_list, pdf_output):
    # Terminal Marker
    print("Generating song set...")

    # Create a new PDF writer
    writer = PdfWriter()

    for song in song_list:
        reader = PdfReader(song)  # Assuming each song has a corresponding PDF file
        writer.append(reader)

    writer.write(pdf_output)
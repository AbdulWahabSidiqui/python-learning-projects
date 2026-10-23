from pypdf import PdfReader
import pyttsx3
from pathlib import Path

pdf_path = Path(input("Enter the path of the pdf file: ").strip().strip('"'))
output_file = pdf_path.with_suffix(".mp3")

def extract_text(path):
    reader = PdfReader(path)
    print("Reading PDF...")
    text = ""

    if not path.exists():
        print("The pdf file does not exist")
        return

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text
    print("Extracting text from PDF...")
    return text

def text_to_voice(text):
    engine = pyttsx3.init()

    print("Converting text to voice...")
    voices = engine.getProperty('voices')
    voices = engine.getProperty('voices')

    choice = int(input('''
Available voices:

0. Microsoft David Desktop
1. Microsoft Zira Desktop

Choose a voice:
        
    '''))

    engine.setProperty('voice', voices[choice].id)

    rate = input("Enter speaking speed (default 180): ")

    if not rate:
        rate = 180

    else:
        rate = int(rate)

    engine.setProperty('rate', rate)
    engine.setProperty('volume', 1.0)

    print("Saving voices to file...")
    engine.save_to_file(text, output_file)
    print("Done!")
    engine.runAndWait()


text = extract_text(pdf_path)
text_to_voice(text)
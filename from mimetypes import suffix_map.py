from mimetypes import suffix_map
from tkinter import PAGES
from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        #return 'File exists!'
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)

        with open('text1.txt', 'w') as file:
            file.write(text)

        text = text.replace('\n', '')
        text = text.replace('\n', '')

        with open('text2.txt', 'w') as file:
            file.write(text)


    else:
        return 'File not exists, check the file path!'

def main():
    print(pdf_to_mp3(file_path='C:\\Users\\Denis\\.git\\good evening.pdf'))

if __name__ == '__main__':
    main()

    



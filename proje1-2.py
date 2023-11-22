import PyPDF2
import os

# PDF dosyasının yolunu al
dosya_yolu = "C:/Users/Gizem/PycharmProjects/pythonproject_01/pdf_path"

# Dosyaya okuma izinlerini eklemek için
os.chmod(dosya_yolu, 0o644)

# PDF dosyasını aç
with open(dosya_yolu, 'rb') as file:
    # PyPDF2'nin PdfFileReader sınıfını kullanarak PDF dosyasını oku
    pdf_reader = PyPDF2.PdfFileReader(file)

    # PDF dosyasındaki sayfa sayısını al
    sayfa_sayisi = pdf_reader.numPages

    # PDF dosyasındaki her bir sayfayı döngü ile oku
    for sayfa_numarasi in range(sayfa_sayisi):
        # Belirli bir sayfayı seç
        sayfa = pdf_reader.getPage(sayfa_numarasi)

        # Sayfadaki metni al
        metin = sayfa.extractText()

        # Metni ekrana yazdır
        print(metin)

        import tkinter as tk
        from tkinter import filedialog
        from PyPDF2 import PdfFileReader


        def open_file():
            file_path = filedialog.askopenfilename()
            if file_path:
                read_pdf(file_path)


        def read_pdf(file_path):
            with open(file_path, 'rb') as file:
                pdf_reader = PdfFileReader(file)
                num_pages = pdf_reader.numPages
                print(f'Total Pages: {num_pages}')

                # Extract text from each page
                for page_num in range(num_pages):
                    page = pdf_reader.getPage(page_num)
                    page_text = page.extractText()
                    lines = page_text.split('\n')
                    for line in lines:
                        if line.startswith('<</Title'):
                            print(f'Title: {line.split(">")[1]}')
                        elif line.startswith('<</Author'):
                            print(f'Author: {line.split(">")[1]}')
                        elif line.startswith('<</Subject'):
                            print(f'Subject: {line.split(">")[1]}')
                        elif line.startswith('<</Keywords'):
                            print(f'Keywords: {line.split(">")[1]}')


        # Create a GUI
        root = tk.Tk()
        root.geometry('400x200')

        # Create a button to open a file
        open_file_button = tk.Button(root, text='Open File', command=open_file)
        open_file_button.pack(pady=20)

        root.mainloop()
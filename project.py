import string

import PyPDF2
import string

reader = PyPDF2.PdfReader('King_S._Pod_Kupolom.a4.pdf')
print(len(reader.pages))
print(reader.pages[27].extract_text())

l = reader.pages[27].extract_text().lower()
print({b: l.count(b.lower()) for b in ("Младший", " Лживая сука", "Энджи", 'Овчарка', 'Литл-Битч')})
phrase = 'Лживая сука'
substituted_phrase = phrase.replace('Лживая сука', 'Обманщица')
print(phrase)
print(substituted_phrase)




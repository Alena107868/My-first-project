

import PyPDF2
import string

reader = PyPDF2.PdfReader('King_S._Pod_Kupolom.a4.pdf')
print(len(reader.pages))
print(reader.pages[27].extract_text())
print(reader.pages[37].extract_text())

l = reader.pages[27].extract_text().lower()
ll = reader.pages[37].extract_text().lower()
print({b: l.count(b.lower()) for b in ("Младший", " Лживая сука", "Энджи", 'Овчарка', 'Литл-Битч')})
print({b: ll.count(b.lower()) for b in ("шериф", "собака", "боль", 'Купол')})

phrase = 'Лживая сука'
substituted_phrase = phrase.replace('Лживая сука', 'Обманщица')
print('Заменить грубое слово:', phrase)
print('на более мягкое:', substituted_phrase)








import PyPDF2

reader = PyPDF2.PdfReader('King_S._Pod_Kupolom.a4.pdf')
print(len(reader.pages))
print(reader.pages[25].extract_text())
print(reader.pages[27].extract_text())

l = reader.pages[27].extract_text().lower().split()
print({b: l.count(b.lower()) for b in ("Младший", "закричал", " - Лживая сука! ")})







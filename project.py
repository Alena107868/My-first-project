
import PyPDF2

reader = PyPDF2.PdfReader('King_S._Pod_Kupolom.a4.pdf')
print(len(reader.pages))
print(reader.pages[25].extract_text())
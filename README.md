# My-first-project

## Цензор Книги Стивена Кинга "Под куполом".

### Вычленение оскорбительных слов, выражений.
### Замена оскорбительных слов выражениями более "мягкого звучания".
### Посчитать сколько раз в книге встречаются имена действующих персонажей, включая животных.


import PyPDF2

reader = PyPDF.PdfReader('King_S._Pod_Kupolom.a4.pdf')
print(len(reader.pages))
print(reader.pages[0].extract_text())
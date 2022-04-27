from pdf2docx import converter, parse

#problem

pdf_file = (r"C:\Users\Aadi\Desktop\maa photo edit\sample.pdf")
word_file = (r"C:\Users\Aadi\Downloads\sample.docx")

cv = converter.Converter(pdf_file);
cv.convert(word_file, start=0, end=None)
cv.close

parse(pdf_file, word_file)
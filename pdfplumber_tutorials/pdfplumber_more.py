import pdfplumber

# Open the PDF
file_path = 'DataSets/technical-pb-mini-split-inverter-60hz-4myw15-sn-07092021.pdf'

pdf = pdfplumber.open(file_path)
page_num=4

# print("text")
# print(pdf.pages[page_num-1].extract_text())

print("table")
table = pdf.pages[page_num-1].extract_table()
print(table)

#does not work
# print("images")
# im = pdf.pages[page_num-1].to_image(resolution=150)
# im.show()



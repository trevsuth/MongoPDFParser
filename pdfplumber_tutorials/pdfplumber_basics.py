import pdfplumber

file_path = 'DataSets/technical-pb-mini-split-inverter-60hz-4myw15-sn-07092021.pdf'

# open pdf
pdf = pdfplumber.open(file_path)

# select page
page = pdf.pages[3]

# get text from page
text = page.extract_text()

print(text)
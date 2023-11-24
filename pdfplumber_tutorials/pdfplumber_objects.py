import pdfplumber

# Open the PDF
file_path = 'DataSets/technical-pb-mini-split-inverter-60hz-4myw15-sn-07092021.pdf'

pdf = pdfplumber.open(file_path)
page_num=6
page = pdf.pages[page_num-1]
objects = page.objects
for object in objects:
    print(object)
    print("")
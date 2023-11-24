import pdfplumber
import pandas as pd 
# Open the PDF
file_path = 'DataSets/technical-pb-mini-split-inverter-60hz-4myw15-sn-07092021.pdf'

pdf = pdfplumber.open(file_path)

#regular table
# page_num=27
# table = pdf.pages[page_num-1].extract_table()
# print(table)
# df = pd.DataFrame(table[1:], columns=table[0])
# print(df)

# irregular table
# page_num=4
# table = pdf.pages[page_num-1].extract_table()
# print(table[:2])
# df = pd.DataFrame(table[1:], columns=table[0])
# print(df)

# iterate through tables
pages = pdf.pages
for page in pages:
    print("Page Num: ", page.page_number)
    tables = page.extract_tables()
    print("Num tables", len(tables))
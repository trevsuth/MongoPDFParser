import pdfplumber

# Open the PDF
file_path = 'DataSets/technical-pb-mini-split-inverter-60hz-4myw15-sn-07092021.pdf'

# print num pages
with pdfplumber.open(file_path) as pdf:
    metadata = pdf.metadata
    print("PDF Metadata:")
    print("Num pages: ", len(pdf.pages))
    for key, value in metadata.items():
        print(f"{key}: {value}")
    print("\n")
    
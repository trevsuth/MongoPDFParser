import pdfplumber

# Open the PDF
file_path = 'DataSets/technical-pb-mini-split-inverter-60hz-4myw15-sn-07092021.pdf'

pdf = pdfplumber.open(file_path)
page_num=4
page = pdf.pages[page_num-1]
rects = page.rects
# print(len(rects))
# for rect in rects:
#     print(rect)
#     print("")
rect = rects[0]
print(rect)
bbox = (rect['x0'], rect['y0'], rect['x1'], rect['y1'])
rect_crop = page.within_bbox(bbox)
rect_crop_image = rect_crop.to_image()
rect_crop_image.show()
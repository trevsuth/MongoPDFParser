import pdfplumber
import json
import base64
import os
from io import BytesIO
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_text(pdf_page):
    return pdf_page.extract_text()

def get_image(pdf_page):
    im = pdf_page.to_image(resolution=150)
    
    # Save the image to a BytesIO object
    img_buffer = BytesIO()
    im.save(img_buffer, format='PNG')  # PNG is used for better quality, JPEG is also an option
    img_buffer.seek(0)

    # Encode the image in base64
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def get_tables(pdf_page):
    table_data = []
    tables = pdf_page.extract_tables()
    for table in tables:
            table_data.append(table)
    num_tables = len(table_data)
    return (num_tables, table_data)

# Open the PDF
file_path = 'DataSets/technical-pb-mini-split-inverter-60hz-4myw15-sn-07092021.pdf'
output_json_path = 'output_data.json'

# List to hold each page's data
pages_data = []

with pdfplumber.open(file_path) as pdf:
    # Iterate through each page
    for page in pdf.pages:
        # Get page number and text
        page_num = page.page_number
        text = get_text(page)
        image = get_image(page)
        num_tables, tables = get_tables(page)
        # Add to the list
        pages_data.append({
            "page_num": page_num,
            "text": text,
            "image": image,
            "num_tables": num_tables,
            "tables": tables, 
        })

# Write to a JSON file
with open(output_json_path, 'w') as f:
    json.dump(pages_data, f, indent=4)

# Save to mongo cloud
load_dotenv()

# Set up mongo connection and navigate to collection
uri = os.getenv('MONGO_CONNECTION_STRING')
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['pdf']
collection = db.sample_pdf

# Insert data into collection
if isinstance(pages_data, list):
    collection.insert_many(pages_data)
else:
    collection.insert_one(pages_data)

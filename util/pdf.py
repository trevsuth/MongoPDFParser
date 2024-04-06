import pdfplumber
import os
from io import BytesIO
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import base64

def get_text(pdf_page):
    """
    Extracts and returns the text from a given PDF page.
    
    :param pdf_page: A pdfplumber PDF page object.
    :return: Extracted text from the page.
    """
    return pdf_page.extract_text()

def get_image(pdf_page):
    """
    Converts a PDF page to an image and encodes it in base64.
    
    :param pdf_page: A pdfplumber PDF page object.
    :return: A base64 encoded string of the page image.
    """
    im = pdf_page.to_image(resolution=150)
    img_buffer = BytesIO()
    im.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def get_tables(pdf_page):
    """
    Extracts tables from a given PDF page and returns the number of tables
    and the tables data.
    
    :param pdf_page: A pdfplumber PDF page object.
    :return: A tuple containing the number of tables and a list of the table data.
    """
    tables = pdf_page.extract_tables()
    return len(tables), tables

def parse_pdf(file_path):
    """
    Parses a PDF file, extracting text, base64 encoded images, and tables from each page,
    and then inserts this data into a MongoDB collection.
    
    :param file_path: Path to the PDF file to be parsed.
    """
    pages_data = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            pages_data.append({
                "page_num": page.page_number,
                "text": get_text(page),
                "image": get_image(page),
                "num_tables": get_tables(page)[0],
                "tables": get_tables(page)[1], 
            })

    # Environment variables for MongoDB connection
    load_dotenv()
    uri = os.getenv('MONGO_CONNECTION_STRING')
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['pdf']
    collection = db.sample_pdf

    # Insert parsed data into MongoDB
    if pages_data:
        collection.insert_many(pages_data)

# File path for the PDF to be parsed
# file_path = 'DataSets/technical-pb-mini-split-inverter-60hz-4myw15-sn-07092021.pdf'
# parse_pdf(file_path)

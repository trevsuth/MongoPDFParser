# Mongo_pdf
## Extract data from pdf documents and save it to Mongo Atlas

## Install
1. Set up a Mongo Atlas instance here <https://cloud.mongodb.com/>
1. Create a database called ```pdf``` and inside that a collection called ```sample_pdf```
1. Install all required python libraries using ```pip install -r requirements.txt```
1. Run ```pdf_to_mongo.py```
1. This will save the contents so the technical manual to the Altas instance

## Other files
The ```pdfplumber_tutorial``` folder holds the files that I used to figgure out the pdf_plumber library.  I've saved these in case I decide to invest more time into this library, particularly around the lines, curves, or rects object types

I've also added 2 files ```make_json_schema.py``` and ```json_test.py``` for utility and validation.  THe first does what it says on the box and creates a schema of the generated json file, while the second loads the json file saved locally by ```pdf_to_mongo.py``` and re-creates some tables as pandas dataFrames.  I used this to test the table loading and kept it since it represents a potentially common use case.

## TODO
1. Add logic to eliminate all tables that have only null (i.e. ```None```) or empty values
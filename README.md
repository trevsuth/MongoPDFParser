# MongoPDFParser
## Extract data from pdf documents and save it to Mongo Atlas

## Install
1. Set up a Mongo Atlas instance here <https://cloud.mongodb.com/>
1. Create a Mongo database called ```pdf``` and inside that a collection called ```sample_pdf```
1. Rename env.environment to .env and insert your Atlas collection string
1. Install all required python libraries using ```pip install -r requirements.txt```
1. Run ```main.py```
1. This will save the contents so the technical manual to the Altas instance

## TODO
1. Add logic to eliminate all tables that have only null (i.e. ```None```) or empty values
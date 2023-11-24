import json
from genson import SchemaBuilder

# Load JSON data
json_file_path = 'output_data.json'
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Generate schema
print('Data Loaded')
builder = SchemaBuilder()
builder.add_object(json_data)
json_schema = builder.to_schema()
print('done')
print(json_schema)
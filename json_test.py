import json
import pandas as pd

# Load the JSON file
json_file_path = 'output_data.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)

# Find the data for page 4
page_data = next((item for item in data if item['page_num'] == 4), None)

if page_data:
    # Iterate through each table in the page data
    for i, table in enumerate(page_data['tables']):
        # Convert the table to a DataFrame
        df = pd.DataFrame(table)
        print(f"Table {i+1} on Page 4:")
        print(df)
        print("\n")
else:
    print("No data found for page 4")

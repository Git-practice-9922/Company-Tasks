import pandas as pd
import json
import sys

# Read the input Excel file
input_file = sys.argv[1]
output_file = sys.argv[2]

# Load the Excel sheet into a DataFrame
df = pd.read_excel(input_file)

# Initialize the JSON object
json_data = {}

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    repo_name = row['Repository Name']
    classification = row['Classification']

    # Determine the organization based on the classification
    if classification == 'shared':
        organisation = 'Legal-and-General-Shared'
    elif classification == 'confidential':
        organisation = 'Legal-and-General-Confidential'
    else:
        organisation = 'Unknown-Classification'

    # Add the repository details to the JSON object
    json_data[repo_name] = {
        'repository': repo_name,
        'organisation': organisation
    }

# Write the JSON object to the output file
with open(output_file, 'w') as f:
    json.dump(json_data, f, indent=4)

print(f"JSON file created at {output_file}")

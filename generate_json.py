import pandas as pd
import json

# Define the input and output files
input_excel = "${{ github.workspace }}/source-repo/repositories.xlsx"
output_json = "${{ github.workspace }}/source-repo/output/repositories.json"

# Read the Excel file
df = pd.read_excel(input_excel)

# Create a dictionary to hold the JSON data
repositories_dict = {}

# Loop through the dataframe and construct the dictionary
for _, row in df.iterrows():
    repo_name = row['Repository Name']
    classification = row['Classification']
    
    # Determine the organization based on the classification
    if classification == 'shared':
        organisation = 'Legal-and-General-Shared'
    elif classification == 'confidential':
        organisation = 'Legal-and-General-Confidential'
    else:
        organisation = 'Unknown-Classification'
    
    # Add the entry to the dictionary
    repositories_dict[repo_name] = {
        'repository': repo_name,
        'organisation': organisation
    }

# Write the dictionary to a JSON file
with open(output_json, 'w') as json_file:
    json.dump(repositories_dict, json_file, indent=4)

print(f"JSON file created at {output_json}")

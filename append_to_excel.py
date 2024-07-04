import pandas as pd
import json

# Input JSON file
input_json = '${{ github.workspace }}/env_vars.json'

# Output Excel file
output_excel = '${{ github.workspace }}/env_vars.xlsx'

# Read JSON data
with open(input_json, 'r') as file:
    data = json.load(file)

# Convert JSON data to DataFrame
df = pd.json_normalize(data)

# Append to Excel file (or create if it doesn't exist)
try:
    # If the file exists, append the data
    existing_df = pd.read_excel(output_excel)
    final_df = pd.concat([existing_df, df], ignore_index=True)
except FileNotFoundError:
    # If the file does not exist, create it
    final_df = df

# Write the DataFrame to Excel
final_df.to_excel(output_excel, index=False)

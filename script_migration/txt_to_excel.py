import os
import re

directory = '/path/to/directory'
result_dict = {}

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as f:
            lines = f.readlines()
            for line in lines:
                match = re.search(r'Repository:\s*(.+)', line)
                if match:
                    repository = match.group(1)
                    result_dict[repository] = {}
                match = re.search(r'Size:\s*(.+)', line)
                if match:
                    size = match.group(1)
                    result_dict[repository]['Size'] = size

# Save the result to an excel file
import pandas as pd
df = pd.DataFrame(result_dict).T
df.to_excel('output.xlsx')
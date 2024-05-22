import pandas as pd
import re
from collections import defaultdict

# Read input and output file paths from Snakemake
input_scripts = snakemake.input.scripts
output_csv = snakemake.output.summary

# Initialize a list to hold DataFrames
dataframes = []

# Regular expression to match the line type comments
line_type_pattern = re.compile(r'#\s*(\w+)')

for script_path in input_scripts:
    line_counts = defaultdict(int)

    with open(script_path, 'r') as file:
        for line in file:
            match = line_type_pattern.search(line)
            if match:
                line_type = match.group(1)
                line_counts[line_type] += 1

    df = pd.DataFrame(list(line_counts.items()), columns=['LineType', 'Count'])

    library_name = script_path.split('/')[-2]
    df['Library'] = library_name

    dataframes.append(df)

consolidated_df = pd.concat(dataframes, ignore_index=True)

pivot_df = consolidated_df.pivot_table(index='Library', columns='LineType', values='Count', fill_value=0)
pivot_df = pivot_df.astype(int)

pivot_df.to_csv(output_csv)

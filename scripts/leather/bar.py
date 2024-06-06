import pandas as pd  # i
import leather  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

x_column = snakemake.config["x"]  # pd
y_column = snakemake.config["y"]  # pd
title = snakemake.config["title"]  # pd

data = list(zip(df[x_column], df[y_column]))  # pd

# Create a new Leather chart
chart = leather.Chart(title)  # pd

chart.add_columns(data)  # pd

chart.to_svg(output_svg)  # io

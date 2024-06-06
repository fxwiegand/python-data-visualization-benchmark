import pandas as pd  # i
import pygal  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

data_points = list(zip(df[snakemake.config["scatter_x"]], df[snakemake.config["y"]]))  # pd

bar_chart = pygal.XY(stroke=False)  # pd
bar_chart.title = snakemake.config["title"]  # pd

bar_chart.add('Data Points', data_points)  # pd

bar_chart.render_to_file(output_svg)  # io

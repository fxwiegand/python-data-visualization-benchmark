import pandas as pd  # i
import pygal  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

data = {make: list(group[snakemake.config["y"]]) for make, group in df.groupby(snakemake.config["x"])} # pd

bar_chart = pygal.Bar()  # pd
bar_chart.title = snakemake.config["title"]  # pd
for make, prices in data.items():  # pd
    bar_chart.add(make, prices)  # pd

bar_chart.render_to_file(output_svg)  # io

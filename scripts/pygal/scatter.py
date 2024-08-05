import pandas as pd  # i
import pygal  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

data_points = list(  # pd
    zip(
        df[snakemake.config["scatter_x"]],  # pd
        df[snakemake.config["y"]],  # pd
        df[snakemake.config["color"]],  # pd
    )  # pd
)  # pd

scatter_chart = pygal.XY(stroke=False)  # pd
scatter_chart.title = snakemake.config["title"]  # pd

for color in df[snakemake.config["color"]].unique():  # pd
    points = [(x, y) for x, y, c in data_points if c == color]  # pd
    scatter_chart.add(str(color), points)  # pd

scatter_chart.render_to_file(output_svg)  # io

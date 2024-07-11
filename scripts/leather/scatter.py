import pandas as pd  # i
import leather  # i

predefined_colors = [  # pd
    "rgb(255, 0, 0)",  # pd
    "rgb(0, 255, 0)",  # pd
    "rgb(0, 0, 255)",  # pd
    "rgb(255, 255, 0)",  # pd
    "rgb(0, 255, 255)",  # pd
    "rgb(255, 0, 255)",  # pd
    "rgb(128, 0, 0)",  # pd
    "rgb(0, 128, 0)",  # pd
    "rgb(0, 0, 128)",  # pd
    "rgb(128, 128, 0)",  # pd
]  # pd

color_map = {}  # pd


def colorizer(d):  # pd
    value = d[2]  # pd
    if value not in color_map:  # pd
        color_index = len(color_map) % len(predefined_colors)  # pd
        color_map[value] = predefined_colors[color_index]  # pd
    return color_map[value]  # pd


input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

x_column = snakemake.config["scatter_x"]  # pd
y_column = snakemake.config["y"]  # pd
color = snakemake.config["color"]  # pd
title = snakemake.config["title"]  # pd

data = list(zip(df[x_column], df[y_column], df[color]))  # pd

chart = leather.Chart(title)  # pd

chart.add_dots(data, fill_color=colorizer)  # pd

chart.to_svg(output_svg)  # io

import pandas as pd  # i
import plotly.graph_objects as go  # i
import plotly.io as pio  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

fig = go.Figure(data=[go.Scatter(x=df[snakemake.config["scatter_x"]], y=df[snakemake.config["y"]], mode="markers")])  # pd
fig.update_layout(  # pd
    title=snakemake.config["title"],  # pd
    xaxis_title=snakemake.config["scatter_x"],  # pd
    yaxis_title=snakemake.config["y"]  # pd
)  # pd

pio.write_image(fig, output_svg, format='svg')  # io

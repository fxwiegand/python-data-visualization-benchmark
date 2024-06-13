import pandas as pd  # i
import plotly.graph_objects as go  # i
import plotly.io as pio  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

fig = go.Figure(  # pd
    data=[go.Bar(x=df[snakemake.config["x"]], y=df[snakemake.config["y"]])]  # pd
)  # pd
fig.update_layout(  # pd
    title=snakemake.config["title"],  # pd
    xaxis_title=snakemake.config["x"],  # pd
    yaxis_title=snakemake.config["y"],  # pd
)  # pd

pio.write_image(fig, output_svg, format="svg")  # io

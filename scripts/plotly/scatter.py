import pandas as pd  # i
import plotly.express as px  # i
import plotly.io as pio  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

fig = px.scatter(  # pd
    df,  # pd
    x=snakemake.config["scatter_x"],  # pd
    y=snakemake.config["y"],  # pd
    title=snakemake.config["title"],  # pd
    color=snakemake.config["color"],  # pd
    labels={  # pd
        snakemake.config["scatter_x"]: snakemake.config["scatter_x"],  # pd
        snakemake.config["y"]: snakemake.config["y"],  # pd
    },  # pd
)  # pd

pio.write_image(fig, output_svg, format="svg")  # io

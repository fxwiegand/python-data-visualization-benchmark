import pandas as pd  # i
import altair as alt  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

bar_chart = (  # pd
    alt.Chart(df)  # pd
    .mark_circle(size=60)  # pd
    .encode(  # pd
        x=alt.X(snakemake.config["scatter_x"], sort=None),  # pd
        y=snakemake.config["y"],  # pd
        color=snakemake.config["color"],  # pd
    )  # pd
    .properties(title=snakemake.config["title"])  # pd
)  # pd

bar_chart.save(output_svg)  # io

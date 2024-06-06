import pandas as pd  # i
import altair as alt  # i
import vl_convert as vlc  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

bar_chart = alt.Chart(df).mark_bar().encode(  # pd
    x=alt.X(snakemake.config["x"], sort=None),  # pd
    y=snakemake.config["y"],  # pd
).properties(  # pd
    title=snakemake.config["title"]  # pd
)  # pd

bar_chart.save(output_svg) # io

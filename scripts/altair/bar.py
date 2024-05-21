import pandas as pd
import altair as alt
import vl_convert as vlc
import sys

input_csv = snakemake.input[0]
output_png = snakemake.output[0]

df = pd.read_csv(input_csv)

bar_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Make', sort=None),
    y='Price',
).properties(
    title='Car Prices by Make'
)

png_data = vlc.vegalite_to_png(vl_spec=bar_chart.to_json(), scale=2)
with open(output_png, "wb") as f:
    f.write(png_data)

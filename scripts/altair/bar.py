import pandas as pd  # i
import altair as alt  # i
import vl_convert as vlc  # i

input_csv = snakemake.input[0]  # io
output_png = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

bar_chart = alt.Chart(df).mark_bar().encode(  # pd
    x=alt.X('Make', sort=None),  # pd
    y='Price',  # pd
).properties(  # pd
    title='Car Prices by Make'  # pd
)  # pd

png_data = vlc.vegalite_to_png(vl_spec=bar_chart.to_json(), scale=2)  # io
with open(output_png, "wb") as f:  # io
    f.write(png_data)  # io

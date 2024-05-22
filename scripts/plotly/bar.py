import pandas as pd  # i
import plotly.graph_objects as go  # i
import plotly.io as pio  # i

input_csv = snakemake.input[0]  # io
output_png = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

fig = go.Figure(data=[go.Bar(x=df['Make'], y=df['Price'])])  # pd
fig.update_layout(  # pd
    title='Car Prices by Make',  # pd
    xaxis_title='Make',  # pd
    yaxis_title='Price'  # pd
)  # pd

pio.write_image(fig, output_png, format='png')  # io

import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

input_csv = snakemake.input[0]
output_png = snakemake.output[0]

# Read the CSV file using Pandas
df = pd.read_csv(input_csv)

# Extract 'Make' and 'Price' for plotting
makes = df['Make']
prices = df['Price']

# Create a bar plot using Plotly
fig = go.Figure(data=[go.Bar(x=makes, y=prices)])
fig.update_layout(
    title='Car Prices by Make',
    xaxis_title='Make',
    yaxis_title='Price'
)

# Export the plot to a PNG file
pio.write_image(fig, output_png, format='png')

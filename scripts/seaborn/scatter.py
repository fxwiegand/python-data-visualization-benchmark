import pandas as pd  # i
import seaborn as sns  # i
import matplotlib.pyplot as plt  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

plt.figure(figsize=(10, 6))  # pd
sns.scatterplot(data=df, x=snakemake.config["scatter_x"], y=snakemake.config["y"])  # pd
plt.title(snakemake.config["title"])  # pd

plt.savefig(output_svg, format="svg")  # io

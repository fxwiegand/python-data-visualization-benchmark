import pandas as pd  # i
import seaborn as sns  # i
import matplotlib.pyplot as plt  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

plt.figure(figsize=(10, 6))  # pd
sns.scatterplot(  # pd
    data=df,  # pd
    x=snakemake.config["scatter_x"],  # pd
    y=snakemake.config["y"],  # pd
    hue=snakemake.config["color"],  # pd
)  # pd
plt.title(snakemake.config["title"])  # pd

plt.savefig(output_svg, format="svg")  # io

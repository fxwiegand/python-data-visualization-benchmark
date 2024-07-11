import pandas as pd  # i
import matplotlib.pyplot as plt  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

plt.figure(figsize=(10, 6))  # pd
plt.scatter(  # pd
    df[snakemake.config["scatter_x"]],  # pd
    df[snakemake.config["y"]],  # pd
    c=df[snakemake.config["color"]],  # pd
)  # pd
plt.xlabel(snakemake.config["scatter_x"])  # pd
plt.ylabel(snakemake.config["y"])  # pd
plt.title(snakemake.config["title"])  # pd
plt.xticks(rotation=45)  # pd
plt.tight_layout()  # pd
plt.savefig(output_svg, format="svg")  # io
plt.close()  # io

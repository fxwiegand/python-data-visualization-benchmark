import pandas as pd  # i
import matplotlib.pyplot as plt  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

plt.figure(figsize=(10, 6))  # pd
plt.bar(df[snakemake.config["x"]], df[snakemake.config["y"]], color="skyblue")  # pd
plt.xlabel(snakemake.config["x"])  # pd
plt.ylabel(snakemake.config["y"])  # pd
plt.title(snakemake.config["title"])  # pd
plt.xticks(rotation=45)  # pd
plt.tight_layout()  # pd
plt.savefig(output_svg, format="svg")  # io
plt.close()  # io

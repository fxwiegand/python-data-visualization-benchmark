import pandas as pd  # i
import seaborn as sns  # i
import matplotlib.pyplot as plt  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

plt.figure(figsize=(10, 6))  # pd
sns.barplot(data=df, x='Make', y='Price')  # pd
plt.title('Car Prices by Make')  # pd

plt.savefig(output_svg, format="svg")  # io

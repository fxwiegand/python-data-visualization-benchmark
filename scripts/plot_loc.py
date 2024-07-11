import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(snakemake.input[0])
df = df.pivot(index="Library", columns="Plot Type", values="Lines of Code")
df.plot(kind="bar", stacked=False)
plt.savefig(snakemake.output[0])

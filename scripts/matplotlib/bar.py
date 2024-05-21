import pandas as pd
import matplotlib.pyplot as plt

input_csv = snakemake.input[0]
output_png = snakemake.output[0]

df = pd.read_csv(input_csv)

plt.figure(figsize=(10, 6))
plt.bar(df['Make'], df['Price'], color='skyblue')
plt.xlabel('Make')
plt.ylabel('Price')
plt.title('Car Prices by Make')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_png)
plt.close()

import pandas as pd  # i
import matplotlib.pyplot as plt  # i

input_csv = snakemake.input[0]  # io
output_png = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

plt.figure(figsize=(10, 6))  # pd
plt.bar(df['Make'], df['Price'], color='skyblue')  # pd
plt.xlabel('Make')  # pd
plt.ylabel('Price')  # pd
plt.title('Car Prices by Make')  # pd
plt.xticks(rotation=45)  # pd
plt.tight_layout()  # pd
plt.savefig(output_png)  # io
plt.close()  # io

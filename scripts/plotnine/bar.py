import pandas as pd  # i
from plotnine import ggplot, aes, geom_bar, labs, theme_minimal  # i

input_csv = snakemake.input[0]  # io
output_svg = snakemake.output[0]  # io

df = pd.read_csv(input_csv)  # io

bar_chart = (ggplot(df)  # pd
             + aes(x=snakemake.config["x"], y=snakemake.config["y"])  # pd
             + geom_bar(stat='identity')  # pd
             + labs(title=snakemake.config["title"], x=snakemake.config["x"], y=snakemake.config["y"])  # pd
             + theme_minimal()  # pd
             )

bar_chart.save(output_svg, format='svg')  # io

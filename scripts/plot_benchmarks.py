import os
import pandas as pd
import matplotlib.pyplot as plt


def read_benchmark_data(folder_path):
    data = []
    for file in snakemake.input:
        library_name = file.split("/")[-2]
        plot_type = file.split("/")[-1].split(".")[0]

        # Read data into pandas DataFrame
        df = pd.read_csv(file, sep="\t")

        # Calculate average runtime
        avg_runtime = df["s"].mean()

        # Append to data list
        data.append(
            {
                "Library": library_name,
                "Plot Type": plot_type,
                "Avg Runtime (s)": avg_runtime,
            }
        )
    return pd.DataFrame(data)


def plot_bar_chart(data):
    # Pivot data for plotting
    pivot_data = data.pivot(
        index="Library", columns="Plot Type", values="Avg Runtime (s)"
    )

    # Plotting
    pivot_data.plot(kind="bar", figsize=(10, 6))
    plt.xlabel("Library")
    plt.ylabel("Average Runtime (s)")
    plt.title("Average Runtime Comparison Across Libraries and Plot Types")
    plt.legend(title="Plot Type")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(snakemake.output[0])
    plt.close()


plot_bar_chart(read_benchmark_data(snakemake.input[0]))

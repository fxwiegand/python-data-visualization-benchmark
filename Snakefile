import os

DATASET = "cars"

rule all:
    input:
        "results/altair.png",
        "results/matplotlib.png",
        "results/plotly.png",
        "results/loc.csv"

rule altair:
    input:
        f"data/{DATASET}.csv"
    output:
        "results/altair.png",
    conda:
        "envs/altair.yaml"
    script:
        "scripts/altair/bar.py"

rule matplotlib:
    input:
        f"data/{DATASET}.csv"
    output:
        "results/matplotlib.png",
    conda:
        "envs/matplotlib.yaml"
    script:
        "scripts/matplotlib/bar.py"

rule plotly:
    input:
        f"data/{DATASET}.csv"
    output:
        "results/plotly.png",
    conda:
        "envs/plotly.yaml"
    script:
        "scripts/plotly/bar.py"


def get_all_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root,file))
    return py_files


rule count_loc:
    input:
        scripts=get_all_py_files("scripts")
    output:
        "results/loc.csv"
    run:
        loc_dict = {}

        for file in input.scripts:
            with open(file) as f:
                num_lines = sum(1 for line in f if line.strip())

            loc_dict[file] = num_lines

        with open(output[0],'w') as csv_file:
            csv_file.write("File Name,Lines of Code\n")
            for file, loc in loc_dict.items():
                csv_file.write(f"{file},{loc}\n")




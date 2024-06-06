import os

configfile: "config.yaml"

libraries = ["altair", "plotly", "matplotlib", "seaborn", "pygal", "plotnine", "leather"]

rule all:
    input:
        expand("results/{library}.svg", library=libraries),
        "results/loc.csv",
        "results/loc_types.csv"

rule bar:
    input:
        config["dataset"],
    output:
        "results/{library}.svg",
    conda:
        "envs/{library}.yaml"
    benchmark:
        repeat("results/benchmarks/{library}.benchmark.txt", 10)
    script:
        "scripts/{wildcards.library}/bar.py"


def get_all_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "loc_types.py":
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


rule loc_types:
    input:
        scripts=expand("scripts/{library}/bar.py", library=libraries)
    output:
        summary="results/loc_types.csv"
    script:
        "scripts/loc_types.py"

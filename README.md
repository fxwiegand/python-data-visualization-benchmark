# Python Plotting Libraries Comparison with Snakemake

This Snakemake workflow compares different plotting libraries in Python.

## Installation

1. **Install Mamba**: Mamba is a faster alternative to Conda for package management. You can install it via Conda with the following command:

`conda install mamba -n base -c conda-forge`


2. **Create Environment**: Create a dedicated Conda environment for the workflow using Mamba:

`mamba create -c conda-forge -c bioconda -n snakemake snakemake`

3. **Activate Environment**: Activate the created environment:

`mamba activate snakemake`

## Running the Workflow

To execute the Snakemake workflow, run the following command:

`snakemake --cores all --use-conda`
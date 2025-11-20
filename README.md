# occ-coding-tests: demo and test of occupation coding tools

# Introduction

## About

**As of November 2023, this repository is under active development: things will change rapidly so please be aware of updates**

This repo aims to (1) demonstrate the use of tools for coding occupation descriptions to the ISCO-08 scheme, and (2) serve as a demonstration of the "accuracy" of these approaches relative to a common baseline test data set which has been manually coded.

For an overview of occupation coding generally, and the ISCO-08 scheme specifically, please see the [Quarto documentation pages](docs/_site/index.html).

## Installation / pre-requisites
Before rendering the repo documentation (see below), you will need to ensure you have all package dependencies installed. These are specified in the `requirements.txt` file. You can install these dependencies using pip:
```bash
pip install -r requirements.txt
```

## Use
The core of this repo is the documentation included in the docs/ folder, generated using Quarto. To build the documentation locally, you will need to have Quarto installed. Installation of the command line tools for this (`quarto-cli`) should be taken care of by the `requirements.txt` file above, but in case you want to install Quarto separately or need to troubleshoot, you can find installation instructions on the [Quarto website](https://quarto.org/docs/get-started/). 

Once you have Quarto installed, you can build the documentation by running the following command in the root directory of the repo:
```bash
quarto render docs/
```
This will generate the documentation in the `docs/` folder. You can then open the `index.html` file in your web browser to view the documentation.

## Example benchmark data & contributions to this
This repository includes some synthetic benchmark data for testing occupation coding tools, located in the `data/` folder. If you have additional benchmark data that you would like to contribute, please feel free to submit a pull request with your data included in the `data/` folder. Please ensure that your data is properly formatted and includes any necessary documentation. See the [Example Data section](docs/_site/example_data.html) in the documentation for more details on the expected format.

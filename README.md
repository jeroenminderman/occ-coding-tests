# occ-coding-tests: demo and test of occupation coding tools

# Introduction

## About

**As of December 2025, this repository is under active development: things will change rapidly so please be aware of updates**

This repo aims to (1) demonstrate the use of tools for coding occupation descriptions to the ISCO-08 scheme, and (2) show the performance ("accurary") of these approaches on a synthetic test data set.  

The code in this repo is demonstrated and documented through a set of pages generated using [Quarto](https://quarto.org/), with the source files located in the `docs/` folder, including:  

- An [introduction to the background of occupation coding](https://jeroenminderman.github.io/occ-coding-tests/), the ISCO-08 scheme, and coding tools in general.
- Details of the background to, creation of, and structure of the [Example Data](https://jeroenminderman.github.io/occ-coding-tests/example_data.html) used for testing.
- Demonstration of the use of tools including [occupationcoder-international](https://jeroenminderman.github.io/occ-coding-tests/demos_performance.html#occupationcoder-international) and [Classifai](https://jeroenminderman.github.io/occ-coding-tests/demos_performance.html#classifai) to do coding to ISCO-08, as well as a [comparison of their performance](https://jeroenminderman.github.io/occ-coding-tests/demos_performance.html#summary-comparison).

## Installation / pre-requisites
Before rendering the repo documentation (see below), you will need to ensure you have all package dependencies installed. These are specified in the `requirements.txt` file. You can install these dependencies using pip:
```bash
pip install -r requirements.txt
```

## Use
The core of this repo is the documentation included in the [docs/](docs/) folder, generated using Quarto. Please see there for details on the occupation coding tools demonstrated here, the benchmark data included, and the results of the tests run.  

To build the documentation locally, you will need to have Quarto installed. Installation of the command line tools for this (`quarto-cli`) should be taken care of by the `requirements.txt` file above, but in case you want to install Quarto separately or need to troubleshoot, you can find installation instructions on the [Quarto website](https://quarto.org/docs/get-started/). 

Once you have Quarto installed, you can build the documentation by running the following command in the root directory of the repo:
```bash
quarto render docs/
```
This will generate the documentation in the `docs/` folder. You can then open the `index.html` file in your web browser to view the documentation.

## Example benchmark data & contributions to this
This repository includes some synthetic benchmark data for testing occupation coding tools, located in the `data/` folder. If you have additional benchmark data that you would like to contribute, please feel free to submit a pull request with your data included in the `data/` folder. Please ensure that your data is properly formatted and includes any necessary documentation. See the [Example Data section](https://jeroenminderman.github.io/occ-coding-tests/example_data.html) in the documentation for more details on the expected format.

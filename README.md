![CCIVR_LOGO](CCIVR_logo.png)


# CCIVR

## Overview
**CCIVR** (**C**omprehensive **C**is-NATs **I**dentifier **V**ia **R**NA-seq data) is a Python package tool that facilitates the identification of total cis-NATs (cis-natural antisense transcripts) from gene datasets. CCIVR requires a CSV-formatted input file that contains gene datasets with their locational information including chromosome number where the genes are located, their strand direction, transcription start site (TSS), and transcription termination site (TTS), with or without expression profiling data from RNA-seq, including TPM, FPKM, fold-change, and padj (q-value). CCIVR generates two CSV-formatted output files: a table file containing a list of total extracted cis-NATs accompanied by their structural characteristics, including embedded (EB), fully-overlapped (FO), head-to-head (HH), and tail-to-tail (TT) types; a summary file containing the absolute number and percentage of each type of extracted cis-NAT. For more details, please see Ohhata T *et al.*, ***Sci Rep.***, 12:15525, 2022.

## Requirement

* Python 3.8+

## Installation
You can install CCIVR via a package manager `pip` by typing the following command:           

```
pip install git+https://github.com/CCIVR/ccivr.git
```

It should be noted, however, that this doesn't work when you don't have git on your computer. In that case, please download the ZIP file offered by this site and type the following command:

```
pip install [full path of unzipped package]
```

If the package manager `pip` does not work, please try `pip3` instead.

To check whether CCIVR is correctly installed, please type the following command:

```
ccivr --help
```
If this does not work, please check the setting of the `$PATH` environment. 


The location of CCIVR installation can be found by typing the following command:

```
pip show ccivr
``` 

## Input file preparation
For CCIVR analysis, a CSV-formatted file is required as an input file. The input file must contain five different gene annotations listed in their independent columns, as follows: 

- **id**: gene id of each gene. Example: ENSMUSG00000085715   
- **Chr**: chromosome number where the gene is located. Example: X
- **Strand**: strand direction of the gene. Example: +
- **Start**: the minimum number of the gene location. Example: 103431517
- **End**: the maximum number of the gene location. Example: 103484957

(The example above is for the murine *Tsix* gene, from Ensembl GRCm39)  

The order of these five columns is changeable because CCIVR recognizes their characters (*i.e.*, **id**, **Chr**, **Strand**, **Start**, **End**) but not their order.

These gene annotations can be obtained from the Ensembl database. 

Attaching other gene annotations is available during the CCIVR process by adding extra columns such as “**GeneSymbol**”, “**gene_source**”, “**gene_biotype**”, “**GO_analysis**”, and so on to the input file.

Attaching information for expression profiling obtained from RNA-seq analysis is also available during the CCIVR process by adding extra columns such as **“TPM”**, **“FPKM”**, **“fold_change”**, **“padj”**, and so on to the input file. 

Please see [the test file](data/Test_file.csv) for an example of the input file. 
(The test file contains human gene datasets accompanied by expression profiling of human hepatoma Huh-7 cells with TGFß
stimulation, which is consistent with the input file used for the CCIVR analysis in figure 4 of our paper, Ohhata T *et al.*, ***Sci Rep.***, 12:15525, 2022.)


## Usage

For running "CCIVR", please specify the absolute or relative path of the input file```[path of input CSV]``` and type the following command:

```
ccivr [path of input CSV] 
```

By default, output files will be saved in the same directory as the input file. For saving the output files to a different directory, please add the optional argument and specify the absolute or relative path of the directory```[path of saving directory]``` and type the following command:

```
ccivr [path of input CSV] --output [path of saving directory]
```

If it runs successfully, processing status will be displayed as follows (this is an example from running with [the test file](data/Test_file.csv):

```
Reading [path of input CSV]
EB
Plus-to-minus extracting
Minus-to-plus extracting
FO
Plus-to-minus extracting
Minus-to-plus extracting
HH
Plus-to-minus extracting
Minus-to-plus extracting
TT
Plus-to-minus extracting
Minus-to-plus extracting
< Result >
total genes : 65065
genes with cisNats : 27351 [42.04%]
     EB : 8112 [12.47%]
     FO : 12194 [18.74%]
     HH : 5992 [9.21%]
     TT : 6097 [9.37%]
Writing the table to [path of output CSV, ending with "Table.csv"]
Writing the summary to [path of output CSV, ending with "Summary.csv"]
```

Two CSV formatted output files **"Table.csv"** and **"Summary.csv"** will be generated and saved in a new directory named **"ccivr_output"**.  

**Table.csv** contains a list of all extracted cis-NATs accompanied by their structural characteristics.  
**Summary.csv** contains the absolute number of each type of extracted cis-NATs with its percentages of the total genes. 

An example of "Table.csv" obtained from [the test file](data/Test_file.csv), can be found [here](data/Table.csv).

An example of "Summary.csv" obtained from [the test file](data/Test_file.csv), can be found [here](data/Summary.csv).



To complete the whole CCIVR process with the test file may take from a few to dozens of minutes using a standard-powered computer (for example, it takes 6 minutes 34 seconds using an iMac 2017 equipped with a 3.4 GHz Intel Core i5).

## Uninstallation
When you no longer use the package, you can uninstall it by typing the following command:

```
pip uninstall ccivr
```

## Authors
Tatsuya Ohhata conceptualized CCIVR. Maya Suzuki and Tatsuya Ohhata designed the CCIVR algorithm. Maya Suzuki implemented the CCIVR software.

## License
CCIVR is licensed under the [MIT license](LICENSE).

## Reference
Ohhata T *et al.*, ***Sci Rep.***, 12:15525, 2022.

Updated May 4th, 2024

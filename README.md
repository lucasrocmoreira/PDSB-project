# iGenome

**Author**: Lucas R. Moreira

**E-mail**: lr2767@columbia.edu

Low-coverage whole genome sequences have become a new trend in population genetics and phylogenetics due to the rise of new sequencing platforms that yield massive amounts of genetic data for reasonably low prices (1,2). The analysis of these data, however, is very computationally demanding and requires several consecutive steps that use different bioinformatic algorithms. Despite the recent popularity of this approach, very few bioinformatic pipelines have been developed to automatize this process and make it more user-friendly.

I propose to develop a program, called *iGenome*, that takes as input a set of individual fastq files and a “parameters” file and returns a multi-sample vcf file with nicely filtered and curated SNPs. The program is a wrapper inspired by ipyrad (3) and will be written in python with the purpose of being primarily accessed through a command-line interface (CLI). 

The workflow involves ten sequential steps (shown in the diagram below), which call different programs and use parallel processing. Each step will be run separately and can be branched out so that different parameters can be tested. The program will be tested with a subset of low-coverage whole genome data from *Picoides villosus*, recently obtained. *iGenome* will be freely available through GitHub and will hopefully be of use to other interested users.

![Image of Workflow](https://github.com/lucasrocmoreira/PDSB-project/blob/master/documents/iGenome.png)

### References
1. Oyler-McCance, S. J., Oh, K. P., Langin, K. M. & Aldridge, C. L. A field ornithologist’s guide to genomics: practical considerations for ecology and conservation. Auk 133, 626–648 (2016).
2. Lemmon, E. M. & Lemmon, A. R. High-throughput genomic data in systematics and phylogenetics. Annu. Rev. Ecol. Evol. Syst. 44, 99–121 (2013).
3. Eaton, D. A. R. PyRAD: Assembly of de novo RADseq loci for phylogenetic analyses. Bioinformatics 30, 1844–1849 (2014).

### Version notes

This is a beta version of iGenome. This version is limited to:

1) Linux OS machines.
2) Single sample processing.
3) Only step 1 (Trimming and quality control) of pipeline (next ones will be implemented shortly).
4) No parallel processing.

### Requirements:

1) Python 3.0 or above.
2) Anaconda.
3) Java.
4) Git.

### Installation

* Install Java.
* Install [Anaconda](https://docs.anaconda.com/anaconda/install/).
* Clone this repository.
`git clone https://github.com/lucasrocmoreira/PDSB-project.git`
* `cd PDSB-project`
* `cd project`
* Install iGenome
`pip install .`

### Usage:

```
usage: iGenome [-h] [-v] [-p params] [-s steps]

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -p params      path to params file for Assembly
  -s steps       Set of assembly steps to perform, e.g., -s 123 (Default=None)

  * Example command-line usage:
    iGenome -p params-data.txt            ## run iGenome with settings in params file.
    iGenome -p params-data.txt -s 123     ## run only steps 1-3 of assembly.
  * Documentation: https://github.com/lucasrocmoreira/PDSB-project.git
```

### Input files

#### 1) Raw reads

Raw reads are input as paired-end [.fastq](http://support.illumina.com/content/dam/illumina-support/help/BaseSpaceHelp_v2/Content/Vault/Informatics/Sequencing_Analysis/BS/swSEQ_mBS_FASTQFiles.htm) files.

#### 2) Reference genome

The reference genome is input as a [.fa](https://en.wikipedia.org/wiki/FASTA_format) file.

#### 3) Params file

The params file specifies all of the parameter settings necessary to complete an assembly. It follows the following format:

```
------- iGenome params file (v.0.1)-------------------------------------------
Sample1				                    ## [0] [sample_name]: Sample name.
						    ## [1] [project_dir]: Project dir (made in curdir if not present)					   
path\to\data\toy_1_dataset.fastq	            ## [2] [raw_fastq1_path]: Location of raw demultiplexed fastq file 1
path\to\data\toy_2_dataset.fastq		    ## [3] [raw_fastq2_path]: Location of raw demultiplexed fastq file 2							   
path\to\reference.fa				    ## [4] [reference_sequence]: Location of reference sequence file
```
Note: Absolute paths are required in the params file.

Example run:
[Jupyter notebook](https://github.com/lucasrocmoreira/PDSB-project/blob/master/notebooks/Example%20iGenome%20run.ipynb)



import iGenome as ig
import argparse
import sys
import pkg_resources
from collections import OrderedDict

def parse_command_line():
    """ Parse CLI args."""

    ## create the parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\n
  * Example command-line usage: 
    iGenome -p params-data.txt            ## run iGenome with settings in params file.
    iGenome -p params-data.txt -s 123     ## run only steps 1-3 of assembly.
  * Documentation: https://github.com/lucasrocmoreira/PDSB-project.git
    """)

    ## add arguments 
    parser.add_argument('-v', '--version', action='version', 
        version=str(pkg_resources.get_distribution('iGenome')))
    parser.add_argument('-p', metavar='params', dest="params",
        type=str, default=None,
        help="path to params file for Assembly")
    parser.add_argument('-s', metavar="steps", dest="steps",
        type=str, default=None,
        help="Set of assembly steps to perform, e.g., -s 123 (Default=None)")
    # parser.add_argument("-c", mepkg_resourcestavar="cores", dest="cores",
    #     type=int, default=0,
    #     help="number of CPU cores to use (Default=0=All)")

    ## if no args then return help message
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    ## parse args
    args = parser.parse_args()

    if not "params" and "step" in vars(args).keys():
        print("Bad arguments: ipyrad command must include"\
                +"`-p` or `-s`\n")
        parser.print_help()
        sys.exit(1)

    return args

def parse_params(args):
    """ Parse the params file args, create and return Assembly object."""

    ## check that params.txt file is correctly formatted.
    try:
        with open(args.params) as paramsin:
            plines = paramsin.readlines()
    except IOError:
        sys.exit("  No params file found")

    ## make into a dict. Ignore blank lines at the end of file
    ## Really this will ignore all blank lines
    items = [i.split("##")[0].strip() for i in plines[1:] if not i.strip() == ""]

    #keys = [i.split("]")[-2][-1] for i in plines[1:]]
    #keys = range(len(plines)-1)
    paramsdict = OrderedDict([
                   ("sample_name", ""),
                   ("project_dir", ""),
                   ("raw_fastq1_path", ""),
                   ("raw_fastq2_path", ""),
                   ("reference_sequence", "")
    ])
    keys = paramsdict.keys()
    parsedict = {str(i):j for i, j in zip(keys, items)}
    return parsedict    

def main():
    """ main function """

    ## parse params file input (returns to stdout if --help or --version)
    args = parse_command_line()

    ## param file must be present
    if not args.params:
        print("""
    Must provide params file.
    e.g., iGenome -p params-test.txt -s 12           ## runs steps 1 & 2
    """)

    else:
        if not args.steps:
            print("""
    Must provide step argument along with -p argument for params file. 
    e.g., iGenome -p params-test.txt -s 12           ## runs steps 1 & 2
    """)
            sys.exit(2)
        else:
            parsedict = parse_params(args)

            ## run assembly steps
            steps = sorted(list(args.steps))

            if '1' in steps:
            	print('Trimming adapters')
            	trim = ig.Trimmomatic(name=parsedict["sample_name"], read1=parsedict["raw_fastq1_path"], 
	        read2=parsedict["raw_fastq2_path"])
            	print(trim.proc.decode('ascii'))

            	print('Assessing read quality')
            	qc1 = ig.fastqc(read=trim.F_paired)
            	print(qc1.proc.decode('ascii'))
            	qc2 = ig.fastqc(read=trim.R_paired)
            	print(qc2.proc.decode('ascii'))

         #    if '2' in steps:
         #    	print('Mapping reads to reference genome')
         #    	Map = ig.bwa(name=parsedict["sample_name"], read1=trim.F_paired, 
	        # read2=trim.R_paired, reference=parsedict["reference_sequence"])
         #    	print(Map.proc.decode('ascii'))
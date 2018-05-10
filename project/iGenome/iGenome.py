import subprocess
import os

class Trimmomatic:
    def __init__(self, name, read1, read2):
        ## get current location
        path = os.path.abspath(os.path.dirname(__file__))
        ## find bin directory
        iGenome_path = os.path.dirname(path)
        bin_path = os.path.join(iGenome_path, "bin")
        trimmomatic = os.path.join(
                       os.path.abspath(bin_path),
                       "trimmomatic-0.36.jar")
        adapters = os.path.join(
                       os.path.abspath(bin_path),
                       "adapters")
        where_TruSeq3PE2 = os.path.join(
                       os.path.abspath(adapters),
                       "TruSeq3-PE-2.fa")
        TruSeq3PE2 = os.path.relpath(where_TruSeq3PE2)

        #arguments for Trimmomatic
        self.name = name
        self.read1 = read1
        self.read2 = read2
        self.F_paired = name+"-forward_paired.fq.gz"
        self.F_unpaired = name+"-forward_unpaired.fq.gz"
        self.R_paired = name+"-reverse_paired.fq.gz"
        self.R_unpaired = name+"-reverse_unpaired.fq.gz"
        self.param = "ILLUMINACLIP:"+TruSeq3PE2+":2:30:10:8:true"
        self.binary = trimmomatic
        self.command_list = self._command_list()
        #output from Trimommatic
        self.proc = self._call_trimmomatic()
		

    def _command_list(self):
        """ build the command list """
        cmd = ["java -jar",
                self.binary,
                str("PE"), 
                str(self.read1), 
                str(self.read2), 
                str(self.F_paired),
                str(self.F_unpaired),
                str(self.R_paired),
                str(self.R_unpaired),
                str(self.param)
               ]
        return " ".join(cmd)

    def _call_trimmomatic(self):
        """ call the command as sps """
        proc = subprocess.Popen(
            self.command_list,
            stderr=subprocess.STDOUT, 
            stdout=subprocess.PIPE
            )
        output,error = proc.communicate()
        print(output.decode('ascii'))
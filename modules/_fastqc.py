
import os
import subprocess
import pandas as pd

## fastqc for read quality control

def fastqc(self):
	
	# create output directory
	outdir = os.path.join(self.outdir, 'fastqc')
	if not os.path.isdir(outdir): os.mkdir(outdir)
	
	# start compiling fastq command
	fastq_files = samples.loc[:,['R1','R2']].melt().set_index('variable').dropna().value.tolist()
	fastq_files = [os.path.join(self.outdir, fastq) for fastq in fastq_files]
	' '.join(fastq_files)	

	command = [
		'fastqc',
		'-o', outdir,
		'-t', str(self.cores),
		fastq_files
	]
	command = ' '.join(fastq_files)

	# run command
	subprocess.run(command, shell=True, check=True)

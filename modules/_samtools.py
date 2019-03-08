
def process_bams(self):

	bams = [file for file in os.listdir(os.path.join(self.outdir, 'aligned')) if file.endswith('.bam')]
	for bam in bams:
		command = 

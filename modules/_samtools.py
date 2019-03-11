
def process_bams(self):

	# get list of bam files
	bams = [file for file in os.listdir(os.path.join(self.outdir, 'aligned')) if file.endswith('.bam')]
	for bam in bams:
		# prepare cleaned bam output name
		bam_name = os.path.basename(bam)
		bam_name = ps.path.splitext(bam_name)[0] + '_cleaned.bam'
		# build samtools command
		command = [
			'samtools sort -n -@', str(self.threads), bam, '|',
			'samtools fixmate - - |',
			'samtools sort -@', str(self.threads), '- |',
			'samtools markdup - - |',
			'samtools view -F 3852 -f 3 -O BAM -@', str(self.threads), '-o', os.path.join(self.outdir, 'results', 'aligned', bam_name)
		]
		# submit samtools command
		subprocess(command, shell=True, check=True)

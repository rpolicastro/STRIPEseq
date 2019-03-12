

def count_reads(self):

	# create output directory if it doesn't exist
	outdir = os.path.join(self.outdir, 'counts')
	if not os.path.isdir(outdir): os.mkdir(outdir)

	# function to count reads
	def _count(row):
		# start building command
		command = [
			'featureCounts',
			'-F GTF -t exon -g gene_id',
			'--minOverlap 10 --largestOverlap',
			'--primary -s 1 -T', str(self.threads)
		]
		# add paired end options where appropriate
		if row['paired'].lower() == 'paired': command.extend(['-p -B -C'])
		# finishing command
		command.extend([
                        '-a', self.genome_gtf,
			'-o', os.path.join(self.outdir, 'counts', row['sample_ID'] + '_' + row['condition'] + '_' + row['replicate'] + '_counts.tsv'),
			os.path.join(self.outdir, 'aligned', row['sample_ID'] + '_' + row['condition'] + '_' + row['replicate'] + '_cleaned.bam'
		])
		command = ' '.join(command)
		# submit command
		subprocess.run(command, shell=True, check=True)

	# run counting command
	self.sample_sheet.apply(_count, axis=1)

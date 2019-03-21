

#def count_reads(self):
#
#	# create output directory if it doesn't exist
#	outdir = os.path.join(self.outdir, 'counts')
#	if not os.path.isdir(outdir): os.mkdir(outdir)
#
#	# function to count reads
#	def _count(row):
#		# start building command
#		command = [
#			'featureCounts',
#			'-F GTF -t exon -g gene_id',
#			'--minOverlap 10 --largestOverlap',
#			'--primary -s 1 -T', str(self.threads)
#		]
#		# add paired end options where appropriate
#		if row['paired'].lower() == 'paired': command.extend(['-p -B -C'])
#		# finishing command
#		command.extend([
#                       '-a', self.genome_gtf,
#			'-o', os.path.join(self.outdir, 'counts', row['sample_ID'] + '_' + row['condition'] + '_' + row['replicate'] + '_counts.tsv'),
#			os.path.join(self.outdir, 'aligned', row['sample_ID'] + '_' + row['condition'] + '_' + row['replicate'] + '_cleaned.bam'
#		])
#		command = ' '.join(command)
#		# submit command
#		subprocess.run(command, shell=True, check=True)
#
#	# run counting command
#	self.sample_sheet.apply(_count, axis=1)
#
#	# combine results files
#	count_files = [f for f in os.listdir(self.outdir, 'counts') if f.endswith('_counts.tsv')]
#	index = 1
#	for count_file in count_files:
#		df = pandas.read_csv(os.path.join(self.outdir, 'counts', count_file), sep='\t', header=0, index_col=0)
#		if index == 1:
#			master = df
#			index += 1
#		else:
#			master.join(df, how='outer', sort=True)
#			index += 1
#	master.to_csv(os.path.join(self.outdir, 'counts', 'merged_counts.tsv'), sep='\t', header=True, index=True, quoting=csv.QUOTE_NONE)

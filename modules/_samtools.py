
import subprocess
import os

def process_bams(self):

	os.chdir(os.path.join(self.outdir, 'aligned'))
	# get list of bam files
	bams = [file for file in os.listdir(os.path.join(self.outdir, 'aligned')) if file.endswith('.bam')]
	bams = [os.path.join(self.outdir, 'aligned', b) for b in bams]
	for bam in bams:
		# prepare cleaned bam output name
		bam_name = os.path.basename(bam)
		bam_name = os.path.splitext(bam_name)[0] + '_cleaned.bam'
		# build samtools command
		command = [
			'samtools sort -n -@', str(self.cores), bam, '|',
			'samtools fixmate - - |',
			'samtools sort -@', str(self.cores), '- |',
			'samtools markdup - - |',
			'samtools view -F 3852 -f 3 -O BAM -@', str(self.cores), '-o', os.path.join(self.outdir, 'results', 'aligned', bam_name)
		]
		command = ' '.join(command)
		# submit samtools command
		subprocess.run(command, shell=True, check=True)

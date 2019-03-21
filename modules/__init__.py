
import os

class STRIPEseq(object):

	def __init__(self, projectID, projectName, organism, seqDir, cores=1, outDir=None):
		self.project_id = projectID
		self.project_name = projectName
		self.organism = organism
		self.cores = cores
		self.seqdir = seqDir
		self.outdir = outDir
		if not self.outdir: self.outdir = os.getcwd()

	from ._samplesheet import sample_sheet
	from ._fastqc import fastqc
	from ._star import star_genome, star_align
	from ._samtools import process_bams
	#from ._subread import count_reads

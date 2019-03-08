
import os
import subprocess
import pandas

class STRIPEseq(object):

	def __init__(self, projectID, projectName, organism, cores=1, outDir=None, seqDir):
		self.project_id = projectID
		self.project_name = projectName
		self.organism = organism
		self.cores = cores
		self.paired = paired
		self.seqdir = seqDir
		self.outdir = outDir
		if not self.outdir: self.outdir = os.getcwd()

	from ._samplesheet import sample_sheet
	from ._fastqc import fastqc
	from ._star import star_genome, star_align

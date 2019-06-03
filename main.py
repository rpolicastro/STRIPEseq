from modules import STRIPEseq
import os

os.chdir('')

# start STRIPE-seq object
stripe = STRIPEseq(
	projectID = '',
	projectName = '',
	organism = '',
	cores = 1,
	outDir = '',
	seqDir = ''
)

# add sample info from sample sheet
stripe.sample_sheet(sampleSheet = '')

# fastqc of reads
stripe.fastqc()

# generate STAR genome index
stripe.star_genome(
	genomeGTF = '',
	genomeFasta = ''
)

# align reads to genome using STAR
stripe.star_align()

# clean bams using samtools
stripe.process_bams()

# raw read counts with subread
stripe.count_reads(
	genomeGTF = '',
	genomeFasta = ''
)

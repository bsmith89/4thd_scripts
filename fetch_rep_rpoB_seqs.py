# !/usr/bin/env python
#
# v0.2 2011-07-07
# Fetches N number of representative sequences from each cluster in
# cluster and sequences from fasta file.  Reps are chosen as the first
# N reference sequences, or, if there are fewer than N, all references
# seqs and then the first N environmental seqs.
# WARNING: this differentiation is specific to the 'eisen' projects
# and based on all of the environmental sequences starting with
# '10' and none of the references seqs.
#
# TODO: Make this universal by checking names against the names file
# for each of these classes.  See fetch_rep_names.py for ideas on how
# to do this
#
# Potential use scenario:
# 
# 	  python fetch_rep_seqs.py -f recA/recA_all.pep
#                	-c recA/recA_all.clust -n 4 >recA.reps4.seqs.pep

import sys
import optparse
import re

p = optparse.OptionParser()
p.add_option('--fasta', '-f')
p.add_option('--clusters', '-c')
p.add_option('--num-reps', '-n', default = 4)
opts, args = p.parse_args()
clusters_file = open(opts.clusters)
num_reps = int(opts.num_reps)
fasta_file = open(opts.fasta)
fasta_string = fasta_file.read()
for cluster in clusters_file:
	names = cluster.split()
	clust_reps = []
	assert clust_reps != None
	if len(names) <= num_reps:
		clust_reps = names
		assert clust_reps != None
	else:
		env_names = []
		ref_names = []
		for name in names:
			if len(ref_names) == num_reps:
				clust_reps = ref_names
				assert clust_reps != None
				break
			else:
				if re.match('^GOS_', name.strip()):
					env_names.append(name)
				else:
					ref_names.append(name)
				assert clust_reps != None
		ref_reps = ref_names
		env_reps = env_names[:num_reps - len(ref_reps)]
		clust_reps = ref_reps + env_reps
		assert clust_reps != None
	for name in clust_reps:
		finds = re.findall('(^\>%s[^\>]*)' % name.strip(), fasta_string, flags=re.MULTILINE)
		if len(finds) == 0:
			sys.stderr.write("The sequence with name '%s' was not found.\n" % name)
		elif len(finds)> 1:
			sys.stderr.write("The name '%s' was not specific enough, more than one sequence found.\n" % name)
		elif len(finds)== 1:
			sys.stdout.write(finds[0])
fasta_file.close()
clusters_file.close()			



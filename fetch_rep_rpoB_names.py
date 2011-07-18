# !/usr/bin/env python
#
# v0.1 2011-07-12
# v0.2 2011-07-14 (applied to rpoB_newreps)
#
# Fetches the names of N number of representatives from each cluster in
#+ cluster.  Reps are chosen as the first
#+ N reference sequences, or, if there are fewer than N, all references
#+ seqs and then the first N environmental seqs.
# Also aliases these names by adding ":ID%d" to the end of the alias
# WARNING: this differentiation is specific to the rpo seqs of the
#+ 'eisen' projects and based on all of the environmental sequences
#+ starting with 'GOS_10' and none of the references seqs.
#
# TODO: Make this universal by checking names against the names file
#+ for each of these classes.
#
# Potential use scenario:
# 
# 	  python fetch_rep_seqs.py -f recA/recA_all.pep
#                	-c recA/recA_all.clust -n 4 >recA.reps4.seqs.pep
#
import sys
import optparse
import re

p = optparse.OptionParser()
p.add_option('--clusters', '-c')
p.add_option('--num-reps', '-n', default = 4)
opts, args = p.parse_args()
clusters_file = open(opts.clusters)
num_reps = int(opts.num_reps)
clust_id = 1
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
		sys.stdout.write("%s\t%s=ID%03d\n" % (name, name, clust_id))
	clust_id += 1
clusters_file.close()			



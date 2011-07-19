# !/usr/bin/env python
#
# add_grp_ID_to_alias.py
# v0.1 2011-07-14
#
# For each name in a .aliases file, adds ('=ID%03d' % clust_number) 
#+ to the end of it.  The clust-number is the line in the .clust file
#+ on which that name was found.  This means that I can make a 
#+ names file with "fetch_rep_rpoB_names.py" and then add aliases to
#+ with add_grp_ID_to_alias.py
#
# Potential use scenario:
# 
# 	  python add_grp_ID_to_alias.py -a recA/recA_all_clust1.aliases
#+ 							        -c recA/recA_all.clust2
#+							         > recA_all.clust2_IDs.aliases
#

import sys
import optparse

p = optparse.OptionParser()
p.add_option('--aliases', '-a')
p.add_option('--clusters', '-c')
opts, args = p.parse_args()
clusters_file = open(opts.clusters)
aliases_file = open(opts.aliases)
clusters = []
for line in clusters_file:
	clusters += [line.split()]
for line in aliases_file:
	name = line.split()[0]
	clust_num = 1
	for cluster in clusters:
		try:
			cluster.index(name)
			break
		except ValueError:
			clust_num += 1
			continue
	if clust_num == None:
		raise NameError("The name %s was not found in the clusters file" % name)
	alias = "%s=ID%03d" % (name, clust_num)
	sys.stdout.write("%s\t%s\n" % (name, alias))

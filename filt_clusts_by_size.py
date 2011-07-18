#!/usr/bin/env python

"""Filters clusters by size
filt_clusts_by_size.py v0.1 (2011-07-07)
Creates a cluster file that doesn't include clusters with fewer than n seqs"""

import sys
import optparse

p=optparse.OptionParser()
p.add_option('--min-members', '-m', default = 1)
p.add_option('--input-file', '-i', default = None)
p.add_option('--cut-out-file', '-c', default = None)
options, arguments = p.parse_args()
infile = None
if options.input_file == None:
	infile = sys.stdin
else:
	infile = open(options.input_file)
min_members = int(options.min_members)
if options.cut_out_file:
	cut_file = open(options.cut_out_file, 'w')
for clust in infile.readlines():
	members = clust.split()
	if len(members) >= min_members:
		sys.stdout.write("\t".join(members))
		sys.stdout.write("\n")
	elif cut_file:
		cut_file.write("\n".join(members))
		cut_file.write("\n")
infile.close()

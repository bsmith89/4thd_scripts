# !/usr/bin/env python
"""Fetches the names of N number of representatives from each cluster

Reps are chosen as the first N reference sequences, or, if there are
fewer than N, all references seqs and then the first N environmental
seqs.  Also aliases these names by adding ":ID%d" to the end of the
alias.

Takes a --type-seqs 'identifier' option with an argument of either rpoB
(default) or recA which assigns '^GOS_10' or '^10' as the environmental
sequence regular expression respectively.

Can also take a custom --env-pat 'regex' which should be a pythonic
regex.

Potential use scenario:

    python fetch_rep_seqs.py -f recA/recA_all.pep
                      -c recA/recA_all.clust -n 4 >recA.reps4.seqs.pep
"""

import sys
import optparse
import re

seq_type_re_dict={'rpoB':'^GOS_10', 'recA':'^10'}

p = optparse.OptionParser()
p.add_option('--clusters', '-c')
p.add_option('--num-reps', '-n', default = 1)
p.add_option('--env-pat', '-p')
p.add_option('--type-seqs', '-t', default='rpoB')
p.add_option('--out-file', '-o')
opts, args = p.parse_args()
env_seq_re = None
if opts.env_pat:
    assert opts.type_seqs == None
    env_seq_re = opts.env_pat
else
    env_seq_re = seq_type_re_dict[opts.type_seqs]
out_file = None
if opts.out_file == None:
    out_file = sys.stdout
else:
    out_file = open(opts.out_file)
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
                if re.match(env_seq_re, name.strip()):
                    env_names.append(name)
                else:
                    ref_names.append(name)
                assert clust_reps != None
        ref_reps = ref_names
        env_reps = env_names[:num_reps - len(ref_reps)]
        clust_reps = ref_reps + env_reps
        assert clust_reps != None
    for name in clust_reps:
        out_file.write("%s\t%s=ID%03d\n" % (name, name, clust_id))
    clust_id += 1
clusters_file.close()

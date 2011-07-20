# !/usr/bin/env python
"""

For each name in a .aliases file, adds (by default) '=ID<clust#> to
the end of it.  The clust-number is the line in the .clust file on which
that name was found.  This means that I can make a names file with
"fetch_rep_rpoB_names.py" and then add aliases to with
add_grp_ID_to_alias.py

NEW: Option to specify your own alias format with the python formatting
standard.  The default is "%s=ID%03d' where %s is the sequence name and
%03d is the cluster number padded to 3 digits with zeros.

Potential use scenario:
 
    python add_grp_ID_to_alias.py -a recA/recA_all_clust1.aliases
                                  -c recA/recA_all.clust2
                                   > recA_all.clust2_IDs.aliases

"""

import sys
import optparse

default_alias_format = r'%s=ID%03d'

p = optparse.OptionParser()
p.add_option('--aliases', '-a')
p.add_option('--clusters', '-c')
p.add_option('--format-alias', '-f')
opts, args = p.parse_args()
clusters_file = open(opts.clusters)
aliases_file = open(opts.aliases)
if opts.format_alias:
    format_string = opts.format_alias
else:
    format_string = default_alias_format
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
        raise NameError("The name %s was not found in the clusters file" %
                        name)
    
    alias = format_string % (name, clust_num)
    sys.stdout.write("%s\t%s\n" % (name, alias))

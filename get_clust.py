# !/usr/bin/env python

import sys

outfile = None
infile = None
try:
    cu_file_path = sys.argv[1]
    infile = open(cu_file_path)
    out_file_path = sys.argv[2]
    outfile = open(out_file_path)
except IndexError:
    infile = sys.stdin
    outfile = sys.stdout
clusters = {}
for record in infile:
    if record[0] == "#":
        continue
    fields = record.split("\t")
    if fields[0].strip() == "C":
        continue
    group_id = fields[1].strip()
    seq_name = fields[8].split()[0].strip()
    if group_id in clusters.keys():
        clusters[group_id] += [seq_name]
    else:
        clusters[group_id] = [seq_name]
for group_id in sorted(clusters.keys()):
    for seq_name in clusters[group_id]:
        outfile.write("%s\t" % seq_name)
    outfile.write("\n")
infile.close()
outfile.close()

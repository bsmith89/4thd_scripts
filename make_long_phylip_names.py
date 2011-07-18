# ! /usr/bin/env python
#
# Replaces the truncated (10 character) names that come out of clustalx
# with their full names from a file with a single column of names in the
# correct order.  This can easily be created from the .msf file that can
# also be output from clustalx like so:
#
# 	awk '/Name:/ {print($2)}' recA.reps2.ali.trim.msf > names.txt
#
# Use the script like so:
#
#	python make_long_phylip_names.py -n names.txt
#		-p recA.reps2.ali.trim.phy >recA.reps2.ali.trim.long_names.phy

import optparse
import sys
import re

p = optparse.OptionParser()
p.add_option('--names-file', '-n')
p.add_option('--phylip-file', '-p')
opts, args = p.parse_args()
names = open(opts.names_file)
phylip_file = open(opts.phylip_file)
phylip_string = phylip_file.read()
lines = phylip_string.split('\n')
line_index = 1
for name in names:
	name = name.strip()
	trunc_name = name[:10]
	lines[line_index], number_made = re.subn(re.escape(trunc_name), name, lines[line_index])
	assert number_made == 1
	sys.stderr.write("replaced %s with %s in line %d\n" % (trunc_name, name, line_index+1))
	sys.stderr.write("%s\n" % lines[line_index])
	line_index += 1
out_string = '\n'.join(lines)
sys.stdout.write(out_string)
names.close()
phylip_file.close()



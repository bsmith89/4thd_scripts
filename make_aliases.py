#!/usr/bin/env python

# Make aliases for a list of names
# v0.1 2007-07-08
#  Takes a list of names to stdin and creates
#+ an .aliases file, which contains the names in the
#+ first column and aliases in the second.

import sys

names = sys.stdin
output = ""
index = 1
for name in names:
	output += "%s\t%010d\n" % (name.strip(), index)
	index += 1
sys.stdout.write(output)

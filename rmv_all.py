# !/usr/bin/env python
#
# Removes all lines which have the words listed in namesfile from
#+ infile, and outputs the result to stdout
import sys
import re

inpath = sys.argv[1]
namespath = sys.argv[2]
infile = open(inpath)
namesfile = open(namespath)
outfile = sys.stdout
outstring = infile.read()
for name in namesfile:
	outstring, n = re.subn('^.*%s.*$' % name.strip(), '', outstring, flags=re.MULTILINE)
	sys.stderr.write("'%s' : %d\n" % (name.strip(), n))
outfile.write(outstring)


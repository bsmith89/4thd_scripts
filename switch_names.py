#!/usr/bin/env python
"""Replace names with aliases and vice-versa

Script to read an aliases file (two columns of names) and replace
every instance, in another file, of the name in one column with the
name in the other column"""

import optparse
import sys
import re



def parse_columns(col1, col2, file, delimeter = None):
    column1 = []
    column2 = []
    for line in file:
        line = line.split()
        column1 += [line[col1]]
        column2 += [line[col2]]
    return column1, column2

def swap_words(current_words, new_words, file):
    file_string = file.read()
    assert(len(current_words) == len(new_words))
    for index in range(len(current_words)):
        file_string = file_string.replace(current_words[index],
                                          new_words[index])
    return file_string

def main():
    p = optparse.OptionParser(usage = "usage: %prog ([option] [argument])*")
    p.add_option('-a', '--aliases-file', dest = "apath")
    p.add_option('-f', '--file', help = "file to operate on", dest = 'fpath')
    p.add_option('-c', '--column', default = 2, type = 'int',
                 help = "which column contains the names to be switched\
                         in [default: %default]")
    opts, args = p.parse_args()
    aliases = []
    names = []
    acol = opts.column
    assert(acol == 1 or acol == 2)
    ncol = 0
    if acol == 1:
        ncol = 2
    else:
        ncol = 1
    afile = open(opts.apath)
    names, aliases = parse_columns(ncol-1, acol-1, afile)
    afile.close()
    main_file = open(opts.fpath)
    output_string = swap_words(names, aliases, main_file)
    sys.stdout.write(output_string)

if __name__ == "__main__":
    main()

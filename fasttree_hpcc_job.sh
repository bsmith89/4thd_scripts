#!/usr/bin/env bash
#PBS -l walltime=168:00:00,mem=4gb -M smithby1@msu.edu -m abe -N FastTree -r y
#
# Run FastTree as a non-interactive job
# 
# Take arguments for the input alignment and the output file name.
#+ Expects FastTree to be found at "~/Projects/eisen/bin/fasttree",
#+ which may or not be true on other systems (TODO).

FT_PATH_DEFAULT="~/Projects/eisen/bin/fasttree"
infile=$1
outfile=$2
STDERR_REDIRECTION_DEFAULT="`dirname outfile`.err"
FT_PATH_DEFAULT $infile >$outfile 2>$STDERR_REDIRECTION_DEFAULT

#!/usr/bin/env bash
#PBS -l walltime=168:00:00,mem=4gb -M smithby1@msu.edu -m abe -N FastTree -r y
#
# Run FastTree as a non-interactive job
# 
# Expects FastTree to be found at "~/Projects/eisen/bin/fasttree",
#+ which may or not be true on other systems (TODO).

infile=rpoB.reps_all.trim.ali
outfile=rpoB.reps_all.trim.ali.tre
FT_PATH_DEFAULT="$HOME/Projects/eisen/bin/FastTree"
STDERR_REDIRECTION_DEFAULT="`dirname outfile`/fasttree.err"
$FT_PATH_DEFAULT $infile >$outfile 2>>$STDERR_REDIRECTION_DEFAULT

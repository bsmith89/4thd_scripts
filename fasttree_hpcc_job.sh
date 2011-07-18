#!/usr/bin/env bash
#PBS -l walltime=168:00:00,mem=4gb -M smithby1@msu.edu -m abe -N 20110711_1 -r y
#
# Version 0.1
# A bash script to run FastTree as an automated job on the hpcc on a
#+ non-interactive node.
#
# Run like so:
#   > qsub fasttree_hpcc_job.sh
#
# Version dated: 2011-07-14
# Run#1: 2011-11-10
# Run#2: 2011-11-14 (made it a universal script)


cd ~/Projects/eisen/rpoB_newreps
OUTFILE=fasttree.err
echo "-------------------" >$OUTFILE
echo "Directory: $PWD" >$OUTFILE
echo "Timepoint: `date`" >$OUTFILE
echo "Job Name: 20110711_1"  >$OUTFILE
echo "\#PBS -l walltime=168:00:00,mem=4gb -M smithby1@msu.edu -m abe -N 20110711_2 -r y" >$OUTFILE
echo 'Starting FastTree with the following command:' >$OUTFILE
echo '"../bin/FastTree rpoB.trim.ali"' >$OUTFILE
../bin/FastTree rpoB.lek0.60.filt.gt1.lek0.80.reps2.ali >rpoB.lek0.60.filt.gt1.lek0.80.reps2.untrimmed.tre 2>$OUTFILE

#!/usr/bin/env bash
#PBS -l walltime=24:00:00,mem=4gb -M smithby1@msu.edu -m abe -N MUSCLE_20110716_1 -r y
#
# Version 0.2
# A bash script to run MUSCLE as an automated job on the hpcc on a
#+ non-interactive node.
#
# Run like so:
#   > qsub muscle_hpc_job.sh
#
# Version dated: 2011-07-11
# Run#1 v0.1: 2011-07-11
# Run#2: 2011-07-14 (changed directory in order to work on a dif. file)
# Run#3: 2011-07-16

cd ~/Projects/eisen/rpoB_with_pubd_reps
OUTFILE=muscle.out
../bin/muscle -in rpoB.reps_all.pep -out rpoB.reps_all.ali 2>&1 | tee $OUTFILE

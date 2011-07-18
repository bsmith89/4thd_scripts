#!/usr/bin/env bash
#PBS -l walltime=168:00:00,mem=4gb -M smithby1@msu.edu -m abe -N 20110708_2 -r y
#
# Version 0.9
# A bash script to run phyml as an automated job on the hpcc on a
# non-interactive node.
#
# Run like so:
#   > qsub rpoB_phyml_hpcc_job.sh
# Version dated: 2011-07-08
# Run#1: 2011-07-08


cd ~/Projects/eisen/rpoB_good_lek
OUTFILE=phyml.out
echo '-------------------' 1>$OUTFILE
echo "Directory: $PWD" 1>>$OUTFILE
echo "Timepoint: `date`" 1>>$OUTFILE
echo 'Starting phyml with the following command:' 1>>$OUTFILE
echo '"phyml -i rpoB.reps4.trim.long_names.phy -d aa -b 100 -m JTT -v e -a e --run_id eisen_pubd 1>>phyml.out' 1>>$OUTFILE
phyml -i rpoB.reps4.aliased.phy -d aa -b 100 -m JTT -v e -a e 1>>$OUTFILE

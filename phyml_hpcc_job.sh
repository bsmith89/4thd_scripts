#!/usr/bin/env bash
#PBS -l walltime=168:00:00,mem=4gb -M smithby1@msu.edu -m abe -N 20110708_2 -r y
#
# A bash script to run phyml as an HPCC job
#
# Run like so:
#   > qsub phyml_hpcc_job.sh

############SETTINGS#########
infile="$HOME/Projects/eisen/rpoB_good_lek" # Replace this line
run_id="PhyML_20110708_1"
outfile= # fill in a new file name if you don't want your file to be
         #+ "[infile-sans-extension].phyml_out"
phyml_path="$HOME/bin/phyml"
############END-SETTINGS#####

outfile_DEFAULT="${infile%.*}.phyml_out"

if [[ -v outfile && $outfile == '' ]]; then
    outfile=$outfile_DEFAULT
fi
echo '-------------------' 1>>$outfile
echo "Directory: $PWD" 1>>$outfile
echo "Timepoint: `date`" 1>>$outfile
echo 'Starting phyml with the following command:' 1>>$outfile
echo "'$phyml_path -i $infile -d aa -b 100 -m JTT -v e -a e --run_id $run_id 2>&1 1>>$outfile'" 1>>$outfile
$phyml_path -i $infile -d aa -b 100 -m JTT -v e -a e --run_id $run_id 2>&1 1>>$outfile # is that 2>&1 correct?

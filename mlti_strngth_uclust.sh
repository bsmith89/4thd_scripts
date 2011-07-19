#! usr/bin/env bash
# Script to run uclust at a variety of cluster cutoffs

cutoffs="0.10 0.20 0.30"
directory=$PWD
usearch_path="$HOME/Projects/eisen/bin/usearch"
infile=$1 # be sure it's sorted
outfile_prefix=$2 # everything before the .id#.##.fmt_out
for cutoff in $cutoffs; do
    uc_name="$outfile_prefix.id$cutoff.uc_out"
    log_name="$outfile_prefix.id$cutoff.log"
    seeds_name="$outfile_prefix.id$cutoff.seeds_out"
    cons_name="$outfile_prefix.id$cutoff.cons_out"
    $usearch_path --cluster $infile --id $cutoff --uc $uc_name --log $log_name --seedsout $seeds_name --consout $cons_name
done
exit $?

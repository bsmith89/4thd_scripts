#! /usr/bin/env bash
# Takes a .lek_score file and creates .clust files
#
#+ Uses various Lek cutoffs and also creates a file listing all of the
#+ cluster sizes from each .clust file

cutoffs="0.60 0.65 0.70 0.75 0.80 0.85"
generate_cluster_path=../LEK_public/generate_cluster.pl

for cutoff in $cutoffs; do
    out_name="$2.lek$cutoff.clust"
    $generate_cluster_path -i $1 -o $out_name -c $cutoff
    awk '{s=0; for (i=1; i<=NF; i++) s=s+1; print s}' $out_name  >"$out_name.sizes"
done
exit $?

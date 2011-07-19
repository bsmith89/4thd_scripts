# !/usr/bin/env awk
# Retrieves and prints all of the sequence names by cluster
# 
# Code that is SUPPOSED to print all of the names that are in
#+ each cluster, sequence names seperated by "\t", clusters by "\n".
# NOT WORKING!
# Awk says there's a syntax error, but I can't figure out why.

$1 !~ /[#C]/ {
    arr[$2,length(arr[$2])+1] = $9
}

END {
    for (i in arr) {
        for (j in arr[i]) {
            printf(arr[i,j], "\t")
        }
        printf("\n")
    }
}


#!/bin/bash
IDX=1
while IFS= read -r LINE
do
    if [[ $IDX -eq 10 ]]; then
        echo $LINE
    fi
    IDX=$IDX+1
done < file.txt

#!/bin/bash

K=2
BITS=10
MAX_K=3
MAX_DIM=4
NUMBER_POINTS=10
INPUT_FILE="../databases/USCensus1990.data.txt"
OUTPUT_FILE="../databases_converted/teste.txt"

while [ $K -lt $MAX_K ]; do
    DIM=3
    while [ $DIM -lt $MAX_DIM ]; do
        echo "kmeans_k"$K"_d"$DIM
        python3 main.py $NUMBER_POINTS $K $DIM $BITS $INPUT_FILE $OUTPUT_FILE
        let DIM=DIM*2
    done
    let K=K*2
done


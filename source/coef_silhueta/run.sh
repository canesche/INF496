#!/bin/bash

K=2
MAX_K=65
MAX_DIM=65
NUMBER_POINTS=10000
MAX_ITER=100
INPUT_FILE="../../../USCensus1990.data.txt"

while [ $K -lt $MAX_K ]; do
    DIM=2
    while [ $DIM -lt $MAX_DIM ]; do
        echo "kmeans_k"$K"_d"$DIM
        python3 main.py $NUMBER_POINTS $K $DIM $MAX_ITER $INPUT_FILE
        let DIM=DIM*2
    done
    let K=K*2
done


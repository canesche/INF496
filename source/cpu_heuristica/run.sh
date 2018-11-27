#!/bin/bash

g++ "main.cpp" -std=c++11 -O3

BITS=4
MAXBITS=17
DATABASE=~/Documentos/kmeans/USCensus1990.data.txt
DEBUG=1

while [ $BITS -lt $MAXBITS ]; do
    echo "Para "$BITS" bits"
    DIM=2
    while [ $DIM -lt 33 ]; do
        K=2
        while [ $K -lt 33 ]; do
            echo "kmeans_k"$K"_d"$DIM
            ./a.out 2000000 $K 100 $DIM $BITS "original/kmeans_k"$K"_d"$DIM"_BITS"$BITS".txt" $DATABASE $DEBUG >> results.csv    
            let K=K*2
        done
        let DIM=DIM*2
    done
    let BITS=BITS+2
done
rm a.out


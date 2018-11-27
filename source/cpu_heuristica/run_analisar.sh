
BITS=4
MAXBITS=17

while [ $BITS -lt $MAXBITS ]; do
    DIM=2
    while [ $DIM -lt 33 ]; do
        K=2
        while [ $K -lt 33 ]; do
            echo "kmeans_k"$K"_d"$DIM"_BITS"$BITS
            python3 analisar.py "original/kmeans_k"$K"_d"$DIM".txt" "original/kmeans_k"$K"_d"$DIM"_BITS"$BITS".txt" $DIM $K >> results_precision.csv    
            let K=K*2
        done
        let DIM=DIM*2
    done
    let BITS=BITS+2
done

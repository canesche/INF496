
#!/bin/bash

DIM=2
INPUT='../kmeans/USCensus1990.data.txt'
OUTPUT='text.txt'
OUTPUT_COMPRESS='text.txt.gz'

echo "delete old files"
rm "results.csv"
echo "done!"

while [ $DIM -lt 65 ]; do

	echo "--- create new file ---"
	python3 generate_data.py $INPUT $OUTPUT $DIM
	echo "done!"
	echo "--- compress data ---"
    	python3 compress.py $OUTPUT $OUTPUT_COMPRESS
	echo "done!"
	
	echo "delete data compress old ..."
	rm $data_output_compress
	echo "done!"

	let DIM=DIM*2
	
done

echo "delete trash..."
rm OUTPUT
echo "done!"

#%time

import gzip, shutil, os, sys, time
from io import BytesIO

if len(sys.argv) < 2 :
	print("invalid entry!")
	print("Entry valid below:")
	print("python3 compress.py <data_input> <data_output>")
else:
	data_input = sys.argv[1]
	data_output = sys.argv[2]

	open_arq = open("results.csv", "a")
	
	print("size uncompress = " + str(os.path.getsize(data_input)) + " bytes (" + str(os.path.getsize(data_input)/1000000) + " MB)") 

	for i in range(0, 10) :
		buf = BytesIO()
		begin = time.time()
		
		with open(data_input, 'rb') as f_in:
			with gzip.GzipFile(filename=data_output, mode='wb', compresslevel=i, fileobj=buf) as f_out:
				shutil.copyfileobj(f_in, f_out)

		total = time.time() - begin
		compressed_data = buf.getvalue()
		
		print("compress Level  = " + str(i))	
		print("size compress   = " + str(len(compressed_data)) + " bytes (" + str(len(compressed_data)/1000000) + " MB)")
		print("time            = " + str(total) + " s")
		
		open_arq.write(str(i)+",")
		open_arq.write(str(os.path.getsize(data_input))+",")
		#open_arq.write(str(os.path.getsize(data_output))+",")
		open_arq.write(str(len(compressed_data))+",")
		open_arq.write(str(os.path.getsize(data_input)/len(compressed_data))+",")
		open_arq.write(str(total)+",")
		
		# descompress data
		begin = time.time()
		gzip.decompress(compressed_data)
		total = time.time() - begin
		open_arq.write(str(total)+",")
		open_arq.write("\n")
		print("time decompress = " + str(total) + " s")

	open_arq.close()

	

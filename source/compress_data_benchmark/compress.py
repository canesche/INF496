#%time

import gzip, shutil, os, sys, time

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
		begin = time.time()
		with open(data_input, 'rt') as f_in:
			with gzip.open(data_output, 'wt', i) as f_out:
				shutil.copyfileobj(f_in, f_out)
		total = time.time() - begin
		
		print("compress Level  = " + str(i))	
		print("size compress   = " + str(os.path.getsize(data_output)) + " bytes (" + str(os.path.getsize(data_output)/1000000) + " MB)")
		print("time            = " + str(total) + " s")
		
		open_arq.write(str(i)+",")
		open_arq.write(str(os.path.getsize(data_input))+",")
		open_arq.write(str(os.path.getsize(data_output))+",")
		open_arq.write(str(os.path.getsize(data_input)/os.path.getsize(data_output))+",")
		open_arq.write(str(total))
		open_arq.write("\n")

	open_arq.close()

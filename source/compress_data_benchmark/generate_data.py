import os, sys

if len(sys.argv) < 2 :
	print("invalid entry!")
	print("Entry valid below:")
	print("python3 generate_data.py <data_input> <data_output> <dimension>")
else:
	data_input = sys.argv[1]
	data_output = sys.argv[2]
	dim = int(sys.argv[3])
	
	# verifica se o arquivo existe, caso exista exclua
	if os.path.exists(data_output):
	    os.remove(data_output)

	open_arq = open("results.csv", "a")
	open_arq.write("dim = " + str(dim) + "\nlvl,uncompress,compress,rate,time (s), time descompress (s)\n")	
	open_arq.close()
	
	print("dimension       = "+ str(dim))

	count_line = 2000000

	arq_open = open(data_input,"r")
	arq_exit = open(data_output, "a")

	count = 0
	for line in arq_open:

		line = line.split(",")
		
		dims = 0
		for i in range(len(line)):
		    if i < 0:
		        # pula a linha
		        continue
		    elif i < dim :
		        arq_exit.write(str(line[i])+" ")
		    elif i == dim :
		        arq_exit.write(str(line[i])+"\n")
		    else :
		        break
		
		count += 1
		if(count >= count_line):
		    break;

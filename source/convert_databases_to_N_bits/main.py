# libraries
from sklearn import preprocessing
import numpy as np
import sys

def main():
	
	# ler as informacoes passadas via terminal 
	if len(sys.argv) > 6:
		num_points = int(sys.argv[1])
		num_clusters = int(sys.argv[2])
		num_dim = int(sys.argv[3])
		bits = int(sys.argv[4]) - 1
		data_in_file_path = sys.argv[5]
		data_output = sys.argv[6]
	else:
		print("invalid args!!!")
		print("usage: <num_points> <num_clusters> <num_dim> <num_bits> <data_file> <data_output>\n") 
		return

	input_file = open(data_in_file_path, "r")
	
	points = []
	counter_points = 0
	for line in input_file:
		
		line = line.replace(',',' ').split(' ')     
		
		# retira a primeira linha        
		del line[0]
		
		# deleta as dimensoes desnecessarias
		for i in range(len(line)-1, num_dim-1, -1):
			del line[i]        
		points.append(line)
		
		counter_points += 1
		if counter_points >= num_points :
			break
		
	points = np.asarray(points).astype('float64')

	print(points)
	print(points.dtype)
	
	# Processa na scala no tamanho desejado 
	min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 2 << bits))
	points = min_max_scaler.fit_transform(points)
	
	points = np.asarray(points).astype('uint')
	
	print(points)
	print(points.dtype)
	
	arq_save = open(data_output,"w")
	
	# save file
	for i in range(len(points)):
		# number of line
		arq_save.write(str(i)+" ")
		for j in range(len(points[i])):
			arq_save.write(str(points[i][j]))
			if j != len(points[i])-1:
				arq_save.write(" ")
			else :
				arq_save.write("\n")	

if __name__ == "__main__":
    main()

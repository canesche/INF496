# libraries
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import matplotlib.cm as cm
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
		
	points = np.asarray(points).astype('uint')

	clusters = np.zeros((num_clusters, num_dim), dtype=uint) 

	for i in range(num_clusters):
		for j in range(num_dim):
		    value = 0            
		    if j == 0:
		        value = i
		    clusters[i][j] = value

	# k-Means
	clusterer = KMeans(n_clusters=num_clusters, init=clusters, n_init=1, max_iter=max_iterations, n_jobs=-1)
	cluster_labels = clusterer.fit_predict(points)
		
	silhouette_avg = silhouette_score(points, cluster_labels)
	
	print("For n_clusters =", num_clusters, "The average silhouette_score is :", silhouette_avg)

if __name__ == "__main__":
    main()

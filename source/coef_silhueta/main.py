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
	if len(sys.argv) > 5:
		num_points = int(sys.argv[1])
		num_clusters = int(sys.argv[2])
		num_dim = int(sys.argv[3])
		max_iterations = int(sys.argv[4])
		data_in_file_path = sys.argv[5]
	else:
		print("invalid args!!!")
		print("usage: <num_points> <num_clusters> <num_dim> <max_iter> <data_file> <data_image>\n") 
		return

	input_file = open(data_in_file_path, "r")
	data_output_image = "silhueta_k"+str(num_clusters)+"_d"+str(num_dim)+".png"
	

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

	clusters = np.zeros((num_clusters, num_dim), dtype=int) 

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
	
	data_output_arq = open("results_coef_silhueta.csv", "a")
	data_output_arq.write(str(num_clusters)+","+str(num_dim)+","+str(silhouette_avg)+"\n")
	data_output_arq.close()
	
	#print("For n_clusters =", num_clusters, "The average silhouette_score is :", silhouette_avg)
	
	#-----------------------------------------------------------------
	# printer
	#-----------------------------------------------------------------
	
	fig, (ax1, ax2) = plt.subplots(1, 2)
	fig.set_size_inches(18, 7)

	ax1.set_xlim([-0.1, 1])

	ax1.set_ylim([0, len(points) + (num_clusters + 1) * 10])
	
	sample_silhouette_values = silhouette_samples(points, cluster_labels)
	
	y_lower = 10
	for i in range(num_clusters):
		# Aggregate the silhouette scores for samples belonging to
		# cluster i, and sort them
		ith_cluster_silhouette_values = \
		    sample_silhouette_values[cluster_labels == i]

		ith_cluster_silhouette_values.sort()

		size_cluster_i = ith_cluster_silhouette_values.shape[0]
		y_upper = y_lower + size_cluster_i

		color = cm.nipy_spectral(float(i) / num_clusters)
		ax1.fill_betweenx(np.arange(y_lower, y_upper),
		                  0, ith_cluster_silhouette_values,
		                  facecolor=color, edgecolor=color, alpha=0.7)

		# Label the silhouette plots with their cluster numbers at the middle
		ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

		# Compute the new y_lower for next plot
		y_lower = y_upper + 10  # 10 for the 0 samples
	
	ax1.set_title("The silhouette plot for the various clusters.")
	ax1.set_xlabel("The silhouette coefficient values")
	ax1.set_ylabel("Cluster label")

	# The vertical line for average silhouette score of all the values
	ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

	ax1.set_yticks([])  # Clear the yaxis labels / ticks
	ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

	# 2nd Plot showing the actual clusters formed
	colors = cm.nipy_spectral(cluster_labels.astype(float) / num_clusters)
	ax2.scatter(points[:, 0], points[:, 1], marker='.', s=30, lw=0, alpha=0.7, c=colors, edgecolor='k')

	# Labeling the clusters
	centers = clusterer.cluster_centers_
	# Draw white circles at cluster centers
	ax2.scatter(centers[:, 0], centers[:, 1], marker='o', c="white", alpha=1, s=200, edgecolor='k')

	for i, c in enumerate(centers):
		ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1, s=50, edgecolor='k')

	ax2.set_title("The visualization of the clustered data.")
	ax2.set_xlabel("Feature space for the 1st feature")
	ax2.set_ylabel("Feature space for the 2nd feature")

	plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
		          "with n_clusters = %d" % num_clusters), fontsize=14, fontweight='bold')

	#plt.show()
	plt.savefig(data_output_image)

if __name__ == "__main__":
    main()

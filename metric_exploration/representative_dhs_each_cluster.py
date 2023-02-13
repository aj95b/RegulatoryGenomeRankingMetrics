import gunzip
import sys
import os
import pandas as pd, numpy as np, seaborn as sns
from sklearn import svm
import matplotlib.pyplot as plt
from scipy.stats import gamma
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy
import math
from scipy.stats import fisher_exact
from sklearn.metrics.pairwise import cosine_similarity
from information_metrics.read_data_global_variables import *


def cluster_centroids():
	#Parameters:
	#1. Path to Normalized Signal
	#2. Top n DHSs to use to present in heatmap
	#3. Path to sorted metric, results of which you want to show
	#4. no. of clusters in a subset of DHSs
		
	norm_signal=sys.argv[1]
	n=int(sys.argv[2])
	sorted_metric_data=sys.argv[3]
	num_clust=int(sys.argv[4])
	
	
	#Replace with path to basis matrix
	basis = pd.read_csv('Desktop/dhs_data/2018-06-08NC16_NNDSVD_Basis.csv',sep='\t')
	#Replace with path to biosample official order
	samp_order = pd.read_csv('samples_ord_major_no1.txt',sep='\t',header=None)
	samp_dict = dict(zip(samp_order.iloc[:,0],samp_order.index))
	basis=basis.replace({"Unnamed: 0": samp_dict})
	#Replace with path to DHS vocabulary
	vocab = pd.read_csv('Desktop/dhs_data/DHS_Index_and_Vocabulary_hg38_WM20190703.txt',sep='\t')
	
	
	#metric_to_use = 'snr' ## Comment out for atomic metrics
	
	signal=pd.read_csv(norm_signal,sep='\t',header=None)
	srtd_metric=pd.read_csv(sorted_metric_data,sep='\t')
	
	
	srtd_metric = srtd_metric.iloc[0:n,:]
	#metric_indices = srtd_metric.dhs_index[srtd_metric.max_metric==metric_to_use]	##No need for atomic metrics	
	#x = signal.iloc[metric_indices,:] ##Use for general sorted metric, modify as under for atomic metrics
	
	x = signal.iloc[srtd_metric.iloc[:,0],:]
	x = x.reset_index() ##Preserving true DHS index
	
	Z  = hierarchy.ward(x.iloc[:,1:])
	
	a=hierarchy.cut_tree(Z, num_clust)
	a = np.transpose(a)
	clust_centers = []
	biosample_cos = np.load(sys.argv[5]) #cosine similarity between biosamples, NMF
	biosample_cos = pd.DataFrame(data=biosample_cos)
	for i in range(num_clust):
		clust = x.iloc[np.where(a[0]==i)[0],:]
		
		
		centroid = np.mean(clust.iloc[:,1:],axis=0)
		dists_from_centroid = [math.dist(centroid,clust.iloc[j,1:]) for j in range(len(clust))]
		ind_of_min_dist = dists_from_centroid.index(min(dists_from_centroid))
		#individual_clusts(clust.iloc[ind_of_min_dist,1:],vocab,biosample_cos,clust.iloc[ind_of_min_dist,0])
		clust_centers.append(clust.iloc[ind_of_min_dist,0])
		
	for_bed=vocab.iloc[clust_centers,0:3]
	for_bed=for_bed.reset_index(drop=True)
	metric_name=sorted_metric_data.rsplit('/')[-1]
	#for_bed.to_csv('Desktop/similarity_metrics/results/'+metric_name+str(n)+metric_to_use+'.bed',sep='\t',index=False,header=None)
	###Modify as under for atomic metric
	for_bed.to_csv('Desktop/similarity_metrics/results/'+metric_name+'_'+str(n)+'.bed',sep='\t',index=False,header=None)
	

def individual_clusts(clust_center_dhs,vocab,biosample_cos,ind_of_min_dist):
	#Parameter 1: center DHS from cluster of DHSs
	#Parameter 2: DHS index vocabulary
	
	vector_1 = clust_center_dhs.to_numpy()
	biosample_indices = np.nonzero(vector_1)
	sum_cos_similarity = 0
	for i in biosample_indices[0]:
		for j in biosample_indices[0]:
			if(j>i):
				sum_cos_similarity += biosample_cos.iloc[i,j]
	M = len(biosample_indices[0])
	mean_cos_similarity = sum_cos_similarity/(M*(M-1)*0.5)
	print(vocab.iloc[ind_of_min_dist,0],end='\t')
	print(vocab.iloc[ind_of_min_dist,1],end='\t')
	print(vocab.iloc[ind_of_min_dist,2],end='\t')
	print(vocab.component[ind_of_min_dist],end='\t')
	print(vocab.numsamples[ind_of_min_dist],end='\t')
	print(mean_cos_similarity)
	
	for_bed=vocab.iloc[clust.iloc[:,0],0:3]
	for_bed=for_bed.reset_index(drop=True)
	metric_name=sorted_metric_data.rsplit('/')[-1]
	for_bed.to_csv('Desktop/similarity_metrics/results/'+metric_name+'_'+str(n)+'_clust'+str(i)+'.bed',sep='\t',index=False,header=None)

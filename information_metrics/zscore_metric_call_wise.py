'''
There is an apparent decrease in most of the metrics with the number of calls (the number of samples with significant signal in each region).
To mitigate this, we performed z-scoring on each given number of samples. It is valid since there are over 3.5 million regions and only 733 samples
and there are many DHSs with the same number of samples. Z-scoring at each value of the number of samples makes the metric less dependent on the number
of samples.
'''

from read_data_global_variables import *

#After executing the function, sort the file with dhs_index, to obtain z-scoring with genomic index wise
def zscore_metric_k_wise(metric_file): #Path to file containing metric score for each DHS
	 metric = pd.read_csv(metric_file,sep='\t')
	 print('dhs_index'+'\t'+'z-scored_fix_k')
	 for i in range(1,biosamples+1):
	 	len_k = len(metric.iloc[np.where(calls==i)[0],0])
	 	x = pd.DataFrame(data=stats.zscore(metric.iloc[np.where(calls==i)[0],0]))
	 	for j in range(len_k):
	 		print(x.index[j],end='\t')
	 		print(x.iloc[j,0])

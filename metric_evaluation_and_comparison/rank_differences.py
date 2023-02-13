from information_metrics.read_data_global_variables import *
import math
import rbo
from scipy import stats

def evaluate_realtive_metric_rank(srtd_metric1=sys.argv[1],srtd_metric2=sys.argv[2],comp_index=int(sys.argv[3])):
	#Parameters:
	#1. Path to first sorted metric file (likely from biased end of the spectrum)
	#2. Path to second sorted metric file (likely from unbiased end of the spectrum)
	#3. NMF component

	#component = list(cscheme.keys())[comp_index]
	metric1 = pd.read_csv(srtd_metric1,sep='\t')
	#metric1 = metric1.iloc[np.where(metric1.component==component)[0],:]
	#metric1 = metric1.reset_index(drop=True)
	metric2 = pd.read_csv(srtd_metric2,sep='\t')
	#metric2 = metric2.iloc[np.where(metric2.component==component)[0],:]
	#metric2 = metric2.reset_index(drop=True)
	metric_name1 = srtd_metric1.rsplit('/')[-1]
	metric_name2 = srtd_metric2.rsplit('/')[-1]
	print(metric_name1+'\t'+metric_name2)
	for i,j in enumerate(metric1.dhs_index):
		print(1 + metric1.index[i], end='\t')
		print(1 + metric2.index[metric2['dhs_index']==j][0])
    

def relative_rank_difference(srtd_metric1=sys.argv[1],srtd_metric2=sys.argv[2],comp_index=int(sys.argv[3])):
	#Parameters:
	#1. Path to first sorted metric file (likely from biased end of the spectrum)
	#2. Path to second sorted metric file (likely from unbiased end of the spectrum)
	#3. NMF component

	#component = list(cscheme.keys())[comp_index]
	metric1 = pd.read_csv(srtd_metric1,sep='\t')
	#metric1 = metric1.iloc[np.where(metric1.component==component)[0],:]
	#metric1 = metric1.reset_index(drop=True)
	metric2 = pd.read_csv(srtd_metric2,sep='\t')
	#metric2 = metric2.iloc[np.where(metric2.component==component)[0],:]
	#metric2 = metric2.reset_index(drop=True)
	
	#print(component)
	
	N = len(metric1)
	
	window_size = 1000
	
	slider = 1 
	print("window_size="+str(window_size)+",slide="+str(slider))
	
	for i in range(0,N,slider):
		metric1_temp = metric1.loc[i:i+window_size,'dhs_index'] #Slice/Window of DHSs to process taken from metric1
		metric1_temp = pd.DataFrame(data=metric1_temp)
		metric2_temp = pd.DataFrame(index=metric2.dhs_index,columns=['index2'],data=range(0,num_dhs))
		ranks_1 = metric1_temp.index
		ranks_2 = metric2_temp.index2[metric1_temp.dhs_index]
		ranks_1=list(ranks_1)
		ranks_2=list(ranks_2)
		print(rbo.RankingSimilarity(ranks_1,ranks_2).rbo())

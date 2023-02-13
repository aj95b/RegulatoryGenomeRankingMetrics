from information_metrics.read_data_global_variables import *
from scipy import stats
from scipy.stats import fisher_exact

def sliding_window_fisher(srtd_metric1=sys.argv[1],srtd_metric2=sys.argv[2],comp_index=int(sys.argv[3])):
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
	#window_size = int(N/10000)
	window_size = 1000
	#slider = int(window_size/2)
	slider = 1 
	#print("window_size="+str(window_size)+",slide="+str(slider))
	print("overlap"+'\t'+"statistic"+"\t"+"pvalue")
	for i in range(0,N,slider):
		metric1_temp = metric1.loc[i:i+window_size,'dhs_index'] #Slice/Window of DHSs to process taken from metric1
		metric2_temp = metric2.loc[i:i+window_size,'dhs_index']
		overlapping_dhs = len(set(metric1_temp).intersection(set(metric2_temp)))
		print(overlapping_dhs,end='\t')
		non_overlap = window_size - overlapping_dhs
		table=np.array([[overlapping_dhs,non_overlap],[non_overlap,num_dhs - (window_size+non_overlap)]])
		print(str(fisher_exact(table)[0])+'\t'+str(fisher_exact(table)[1]))

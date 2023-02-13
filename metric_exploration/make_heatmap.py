def make_heatmap_first_n_dhs():
	#Parameters:
	#1. Path to Normalized Signal
	#2. Top n DHSs to use to present in heatmap
	#3. Path to sorted metric, results of which you want to show
	
	norm_signal=sys.argv[1]
	n=int(sys.argv[2])
	sorted_metric_data=sys.argv[3]
	
	
	signal=pd.read_csv(norm_signal,sep='\t',header=None)
	srtd_metric=pd.read_csv(sorted_metric_data,sep='\t')
	
	#Replace with path to basis matrix
	basis = pd.read_csv('Desktop/dhs_data/2018-06-08NC16_NNDSVD_Basis.csv',sep='\t')
	samp_order = pd.read_csv('samples_ord_major_no1.txt',sep='\t',header=None) #The official order of biosamples
	samp_dict = dict(zip(samp_order.iloc[:,0],samp_order.index))
	basis=basis.replace({"Unnamed: 0": samp_dict})
	
	#####x = signal.iloc[srtd_metric.iloc[0:n,0],:] ##Use for general sorted metric
	x = signal.iloc[np.where((srtd_metric.index<10001)&(srtd_metric.max_metric=='snr'))[0],:]
	x = x.reset_index(drop=True) ##Drop index for heatmaps
	
	###############################################################################################################################################################
	###################   FOR SELECT BIOSAMPLES IN MEAN TFIDF      ###################
	#bios=pd.read_csv('Desktop/similarity_metrics/results/biosamples_for_mean_tfidf',sep='\t')
	#blist=list(bios.iloc[:,0])
	#x = x.iloc[:,blist]
	#x.columns=range(x.shape[1])
	#basis=basis.iloc[blist,:]
	#basis=basis.reset_index(drop=True)
	###############################################################################################################################################################
	
  #Use hierarchical clustering for normalized sliced signal for 'n' DHSs
	Z = hierarchy.ward(x)
	#Order teh DHSs optimally
	optimal_order = hierarchy.leaves_list(hierarchy.optimal_leaf_ordering(Z, x))
	y = x.reindex(optimal_order)
	
	y = np.transpose(y)
	y = y.reset_index(drop=True)
	y = pd.concat([y, basis.loc[:,'Unnamed: 0']],axis=1)
	y = y.sort_values(by='Unnamed: 0')
	y = y.drop('Unnamed: 0', axis=1)
	y = y.reset_index(drop=True)
	
	print(y.shape)
	ax = sns.heatmap(y)
	
	#Replace with path to where you want to save the heatmap
	metric_name=sorted_metric_data.rsplit('/')[-1]
	plt.savefig('Desktop/similarity_metrics/results/Figures/'+metric_name+str(n)+'.png')
	plt.close()

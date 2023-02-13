from information_metrics.read_data_global_variables import *
import math
from scipy import stats
from scipy.stats import poisson
from sklearn.preprocessing import LabelEncoder


def genome_fixed_size_region_info():
	#Parameter 1: DHS Vocabulary data
	#Parameter 2: 25KB genome region file
	#Parameter 3: Chromosome to process
	#Parameter 4: Metric to use for ranks in the region, sorted	
	vocab_data = sys.argv[1]
	genome_regions = sys.argv[2]
	chromosome = sys.argv[3]
	sorted_metric = sys.argv[4]
	metric_unsorted = sys.argv[5]
	
	vocab = pd.read_csv(vocab_data,sep='\t')
	srtd_metric = pd.read_csv(sorted_metric,sep='\t')
	metric = pd.read_csv(metric_unsorted,sep='\t')
	regions = pd.read_csv(genome_regions,sep='\t',header=None)
	chr_indices = np.where(regions.iloc[:,0] == 'chr'+str(chromosome))[0]
	
	metric_name=metric_unsorted.rsplit('/')[-1]
	print("seqname"+'\t'+'start'+'\t'+'end'+'\t'+'no_of_dhs'+'\t'+'sum_'+metric_name+'\t'+'mean_'+metric_name+'\t'
        +'std_'+metric_name+'\t'+'no_of_unique_components'+'\t'+'variance_comp')
  
	for i in chr_indices:		
		x = np.where((vocab.seqname=='chr'+str(chromosome)) & (vocab.start >= regions.iloc[i,1]) & (vocab.start <= regions.iloc[i,2]) )[0]
		no_of_dhs_in_region = len(x)
		if no_of_dhs_in_region==0:
			continue					
		#sum_of_ranks = sum(1+srtd_metric.index[srtd_metric['dhs_index'].isin(x)])
		sum_metric = np.nansum(metric.iloc[x,0])
		mean_metric = sum_metric/no_of_dhs_in_region
		std = np.std(metric.iloc[x,0])
		unique_comps = len(pd.unique(vocab.component[x]))
		
		##Extract numbers for components
		lb_make = LabelEncoder()
		comp = pd.DataFrame(data=vocab.component[x])
		comp['encode_comp'] = lb_make.fit_transform(comp['component'])
		comp_var = np.var(comp['encode_comp'])		
		print(regions.iloc[i,0]+'\t'+str(regions.iloc[i,1])+'\t'+str(regions.iloc[i,2]),end='\t')
		print(no_of_dhs_in_region,end='\t')		
		print(sum_metric,end='\t')
		print(mean_metric,end='\t')
		print(std,end='\t')
		print(unique_comps,end='\t')
		print(comp_var)
    
    
def component_enrichment_per_region():
	#Parameter 1: chromosome info file, computed using genome_fixed_size_region_info()
	#Parameter 2: DHS Vocabulary data
	#Parameter 3: Chromosome to process
	
	regions = pd.read_csv(sys.argv[1],sep='\t')
	vocab = pd.read_csv(sys.argv[2],sep='\t')
	chromosome = sys.argv[3]
	
	#num_regions = len(regions)
  num_regions = 98629
	print("seqname"+'\t'+'start'+'\t'+'end',end='\t')
	
	component_expectancy = {}
	for comp in pd.unique(vocab.component):
		component_expectancy[comp] = len(np.where(vocab.component==comp)[0])/num_regions
		print(comp,end='\t')
	print()
	
	chr_indices = np.where(regions.iloc[:,0] == 'chr'+str(chromosome))[0]
		
	for i in chr_indices:
		x = np.where((vocab.seqname=='chr'+str(chromosome)) & (vocab.start >= regions.iloc[i,1]) & (vocab.start <= regions.iloc[i,2]) )[0]
		if len(x)==0: continue
		vocab1 = vocab.iloc[x,:]
		print(regions.iloc[i,0]+'\t'+str(regions.iloc[i,1])+'\t'+str(regions.iloc[i,2]),end='\t')
		for comp in component_expectancy.keys():
			print(np.log2(len(np.where(vocab1.component==comp)[0])/component_expectancy[comp]), end='\t')
		print()

		
def corank_regions():
	#Parameter 1: Information metrics on genomic regions
	
	regions_info = pd.read_csv(sys.argv[1],sep='\t')
	N = len(regions_info)
	x1 = regions_info.sort_values(by='mean_metric',ascending=False,ignore_index=True)
	x2 = regions_info.sort_values(by='variance_comp',ignore_index=True)
	print("seqname"+'\t'+'start'+'\t'+'end'+'\t'+'no_of_dhs'+'\t'+'variance_comp'+'\t'+'mean_coranks')
	num_metrics = 2
	for i in range(N):
		rank_1 = x1.index[x1['start']==regions_info.start[i]].tolist()[0]
		rank_2 = x2.index[x2['start']==regions_info.start[i]].tolist()[0]
		mean_coranks = (rank_1+rank_2)/num_metrics
		
		print(regions_info.iloc[i,0]+'\t'+str(regions_info.iloc[i,1])+'\t'+str(regions_info.iloc[i,2])+
          '\t'+str(regions_info.iloc[i,3])+'\t'+str(regions_info.loc[i,'variance_comp']),end='\t')
		print(mean_coranks)


def main():
	genome_fixed_size_region_info()
  component_enrichment_per_region()
	corank_regions()
	
	 	
if __name__ == "__main__":
    main()	

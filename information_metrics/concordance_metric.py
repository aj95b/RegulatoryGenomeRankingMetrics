from read_data_global_variables import *

def concordance_metric(dhs_data):
	dhs_data = sys.argv[1] #Path to presence absence matrix
	mix = read_mixture_matrix()
	basis = read_basis_matrix()
	calls = read_aclls()
	print('concordance_metric=mean_cos_simi_between_dhs_NMF_loadings_and_its_biosamples_NMF_loadings')
	f = open(dhs_data, 'r')
	i=0
	for dhs in f :
		vector_dhs = np.array([float(j) for j in dhs.split("\t")])
		biosample_indices = np.nonzero(vector_dhs)
		vector_mix = mix.iloc[i,:]
		mean_cosine_similarity=0
		for k in biosample_indices[0]:
			mean_cosine_similarity += cosine_similarity(vector_mix.to_numpy().reshape(1,-1),basis.iloc[k,:].to_numpy().reshape(1,-1))[0][0]
		mean_cosine_similarity = mean_cosine_similarity/len(biosample_indices[0])
		i=i+1
		print(mean_cosine_similarity)

from read_data_global_variables import *

def mean_cosine_similarity():
  calls = read_calls()
  pres_abs = read_pres_abs_matrix()
  print("corrected_mean_cos_pres_abs")
  path_to_biosample_similarity = sys.argv[1] # Precomputed cosine similarity between all 733 biosamples
	biosample_cos = pd.DataFrame(path_to_biosample_similarity, sep='\t')
  
  for i in raneg(num_dhs):
    vector_1 = np.array(pres_abs.iloc[i,:])
		biosample_indices = np.nonzero(vector_1)
		sum_cos_similarity = 0
		for j in biosample_indices[0]:
			for k in biosample_indices[0]:
				if(k>j):
					sum_cos_similarity += biosample_cos.iloc[j,k]
		mean_cos_similarity = sum_cos_similarity/(calls[i]*(1-calls[i])*0.5)
		print(mean_cos_similarity)
  

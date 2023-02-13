from read_data_global_variables import *

def snr_peak_signal_metric(signal):
	pres_abs = read_pres_abs_matrix()
	f = open(signal, 'r') #signal is DHS_peak_signal_hg38.75_20.normalized.GRCh38_no_alts_CT20220208.tsv
	next(f)
	print('peak_signal_snr_metric')
	
	k=0
	for dhs in f :
		dhs_vector = np.array([j for j in dhs.split("\t")])
		dhs_vector = dhs_vector[2:]
		dhs_vector = dhs_vector.astype(np.float)
		biosample_indices = np.nonzero(pres_abs.iloc[k,:].to_numpy())
		signal_sum = 0
		noise_sum = 0
		for i in range(biosamples):
			if(i in biosample_indices[0]):
				signal_sum += dhs_vector[i]
			else:
				noise_sum += dhs_vector[i]
		avg_signal = signal_sum/len(biosample_indices[0])
		if(len(biosample_indices[0]) == 733):
			avg_noise = 0.00000001 #Can use np.nextafter(0,1) instead
		else:
			avg_noise = noise_sum/(biosamples-len(biosample_indices[0]))
		
		print(avg_signal/avg_noise)
		k += 1

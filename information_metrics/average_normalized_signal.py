from read_data_global_variables import *

def average_norm_signal(signal):
	print("mean_normalized_signal")
	f = open(signal,'r')
	for dhs in f :
		dhs_vector = np.array([float(j) for j in dhs.split("\t")])
		biosample_indices = np.nonzero(dhs_vector)
		calls = len(biosample_indices[0])
		signal_sum = 0
		for i in biosample_indices[0]:
			signal_sum += dhs_vector[i]
		print(signal_sum/calls)

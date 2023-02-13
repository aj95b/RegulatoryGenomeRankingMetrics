import pandas as pd
from read_data_global_variables import read_signal_matrix

def normalize_signal():
  signal = read_signal_matrix()
	for i in range(num_dhs):
		max_signal = max(signal.iloc[i,:])
		for k in range(0,biosamples):
			if(k<biosamples-1):
				print(signal.iloc[i,k]/max_signal,end='\t')
			else:
				print(signal.iloc[i,k]/max_signal)
	

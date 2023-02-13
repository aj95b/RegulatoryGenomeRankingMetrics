from read_data_global_variables import *

def entropy_dhs():
	calls = read_calls()
	entropy = calls*np.log(biosamples/calls)
	return entropy

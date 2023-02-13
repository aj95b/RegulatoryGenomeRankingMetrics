from read_data_global_variables import *

def info_all_dhs_signal(dhs_signal):
	print("Manhattan(p=1)"+"\t"+"Euclidean(p=2)"+"\t"+"p=2.5"+"\t"+"Variance"+"\t"+"Info_metric_1")
	f = open(dhs_signal,'r')
	i=0
	for dhs_1 in f :
		#dhs_1 = f.readlines()[i]
		#i=i+1		
		vector_1 = np.array([float(j) for j in dhs_1.split("\t")])
		position_vect_manhattan = linalg.norm(vector_1,ord=1)
		print(position_vect_manhattan, end='\t')
		print(linalg.norm(vector_1,ord=2), end='\t')
		print(linalg.norm(vector_1,ord=2.5), end='\t')
		variance_vect = np.var(vector_1)
		print(variance_vect,end='\t')
		info_metric_1 = position_vect_manhattan*variance_vect
		print(info_metric_1)	
	f.close()

def main():
	dhs_data = sys.argv[1]
	info_all_dhs_signal(dhs_data)
			
if __name__ == "__main__":
    main()

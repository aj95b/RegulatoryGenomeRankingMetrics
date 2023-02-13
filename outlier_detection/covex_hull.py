import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import umap.umap_ as umap
from scipy.spatial import ConvexHull

def read_data():
  dhs_data = sys.argv[1]
  dhs_data = pd.read_csv(dhs_data, '\t')
  dhs_data = dhs_data.drop('Unnamed: 0',axis=1)
  return dhs_data

def embed_hull(data_matrix):
	N = len(data_matrix)
	reducer = umap.UMAP()
	embedding = reducer.fit_transform(data_matrix)
	emb_df = pd.DataFrame(data = embedding, columns=['Embedding_1','Embedding_2'])
	plt.scatter(emb_df.iloc[:,0],emb_df.iloc[:,1])                                                                                                                                                                 
	hull = ConvexHull(emb_df)
                                                                                                                                                                                                                 
	for simplex in hull.simplices:                                                                                                                                                                                  
	  plt.plot(emb_df.iloc[simplex,0],emb_df.iloc[simplex,1], 'k-') 
    
	plt.plot(emb_df.iloc[hull.vertices,0],emb_df.iloc[hull.vertices,1], 'r--', lw=2)                                                                                                                                
	plt.plot(emb_df.iloc[hull.vertices[0],0],emb_df.iloc[hull.vertices[0],1], 'ro')
	plt.show()

def component_wise_hull(dhs_data, dhs_vocab_path, nmf_component):
    dhs_vocab = pd.read_table(dhs_vocab_path,sep='\t')
    indices_of_interest = dhs_vocab.index[dhs_vocab['component'] == nmf_component].tolist()
    mix_component = dhs_data.iloc[indices_of_interest,:]
    pca = PCA(n_components=3)
    component_pcs = pca.fit_transform(mix_component)
    pcs_df = pd.DataFrame(data=component_pcs)
    hull_component = ConvexHull(pcs_df)
    plt.scatter(pc_df.iloc[:,0],pc_df.iloc[:,1])
    plt.scatter(pc_df.iloc[hull_component.vertices,0],pc_df.iloc[hull_component.vertices,1], c='black') 
  

def main():
	dhs_data = read_data()
	embed_hull(dhs_data)

if __name__ == "__main__":
	main()

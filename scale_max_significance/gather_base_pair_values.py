import sys
import os
import pandas as pd, numpy as np, seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import rankdata

def gather_pvals():
    #Vocabulary with DHS indices
    #vocab = pd.read_csv('../../dhs_data/DHS_Index_and_Vocabulary_hg38_WM20190703.txt',sep='\t')
    #vocab_slice=vocab.iloc[np.where(vocab.seqname=='chr1')[0],:]
    #N = len(vocab_slice)
    ch = sys.argv[1]
    chr_10kb=pd.read_csv('../results/10kb/'+ch,sep='\t')
    chr_25kb=pd.read_csv('../results/25kb/'+ch,sep='\t')
    chr_50kb=pd.read_csv('../results/50kb/'+ch,sep='\t')
    chr_100kb=pd.read_csv('../results/100kb/'+ch,sep='\t')
    print('start'+'\t'+'end',end='\t')#+'\t'+'10kb'+'\t'+'25kb'+'\t'+'50kb'+'\t'+'100kb')
    print('10kb_pval'+'\t'+'10kb_zscore'+'\t'+'25kb_pval'+'\t'+'25kb_zscore'+'\t'+'50kb_pval'+'\t'+'50kb_zscore'+'\t'+'100kb_pval'+'\t'+'100kb_zscore')
    #chr1 = 248956600
    #length_chr = 248956600
    length_chr = int(sys.argv[2])
    for i in range(0,length_chr,500):
        print(int(i),end='\t')
        print(int(i+1000),end='\t')
        
        if (len(np.where((i>=chr_10kb.start) & ((i+1000)<chr_10kb.end))[0])==0):
            print(np.nan,end='\t')
            print(np.nan,end='\t')
        else:
            print(chr_10kb.pvalue[np.where((i>=chr_10kb.start) & ((i+1000)<chr_10kb.end))[0][0]],end='\t')
            print(chr_10kb.zscore[np.where((i>=chr_10kb.start) & ((i+1000)<chr_10kb.end))[0][0]],end='\t')
            
        if (len(np.where((i>=chr_25kb.start) & ((i+1000)<chr_25kb.end))[0])==0):
            print(np.nan,end='\t')
            print(np.nan,end='\t')
        else:
            print(chr_25kb.pvalue[np.where((i>=chr_25kb.start) & ((i+1000)<chr_25kb.end))[0][0]],end='\t')
            print(chr_25kb.zscore[np.where((i>=chr_25kb.start) & ((i+1000)<chr_25kb.end))[0][0]],end='\t')
           
        if (len(np.where((i>=chr_50kb.start) & ((i+1000)<chr_50kb.end))[0])==0):
            print(np.nan,end='\t')
            print(np.nan,end='\t')
        else:
            print(chr_50kb.pvalue[np.where((i>=chr_50kb.start) & ((i+1000)<chr_50kb.end))[0][0]],end='\t')
            print(chr_50kb.zscore[np.where((i>=chr_50kb.start) & ((i+1000)<chr_50kb.end))[0][0]],end='\t')
            
        if (len(np.where((i>=chr_100kb.start) & ((i+1000)<chr_100kb.end))[0])==0):
            print(np.nan,end='\t')
            print(np.nan)
        else:
            print(chr_100kb.pvalue[np.where((i>=chr_100kb.start) & ((i+1000)<chr_100kb.end))[0][0]],end='\t')
            print(chr_100kb.zscore[np.where((i>=chr_100kb.start) & ((i+1000)<chr_100kb.end))[0][0]])





def main():
    gather_pvals()

if __name__ == "__main__":
    main()

import gunzip
import pandas as pd
import numpy as np
from numpy import linalg
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances 
from scipy.spatial import distance
from scipy import stats
import sys
import os
import fileinput
import linecache
import matplotlib.pyplot as plt
from scipy.stats import gamma
import umap.umap_ as umap

biosamples = 733
num_components = 16
num_dhs = 3591898
color_scheme = {'Placental / trophoblast': '#FFE500', 'Lymphoid': '#FE8102', 'Myeloid / erythroid': '#FF0000', 'Cardiac': '#07AF00',
           'Musculoskeletal': '#4C7D14', 'Vascular / endothelial': '#414613', 'Primitive / embryonic': '#05C1D9', 'Neural': '#0467FD',
           'Digestive': '#009588','Stromal A': '#BB2DD4', 'Stromal B': '#7A00FF', 'Renal / cancer': '#4A6876',
           'Cancer / epithelial': '#08245B', 'Pulmonary devel.': '#B9461D','Organ devel. / renal': '#692108', 'Tissue invariant': '#C3C3C3'}


def read_calls():
  path_to_calls = sys.argv[1]
  calls = pd.read_csv(path_to_calls,sep='\t',header=None)
  return calls

def read_signal_matrix():
  path_to_signal_matrix = sys.argv[2]
  signal = pd.read_csv(path_to_signal_matrix,sep='\t',header=None)
  return signal

def read_pres_abs_matrix():
  path_to_pres_abs_matrix = sys.argv[3]
  pres_abs = pd.read_csv(path_to_pres_abs_matrix,sep='\t',header=None)
  return pres_abs

def read_mixture_matrix():
  path_to_mixture_matrix = sys.argv[4]
  mix = pd.read_csv(path_to_mixture_matrix,sep='\t')
	mix = mix.drop('Unnamed: 0',axis=1)
  return mix

def read_basis_matrix():
  path_to_basis_matrix = sys.argv[5]
	basis = pd.read_csv(path_to_basis_matrix,sep='\t')
	basis = basis.drop('Unnamed: 0', axis=1)
  return basis

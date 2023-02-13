# regulatory_genome_ranking_metrics
Regulatory elements of the human genome correspond to approximately 100-200 basepair long regions where the chromatin is more prone to be cleaved by the DNAse-I enzyme. Such a site is referred to as the DNAse-I Hypersensitive Site (DHS). The underlying data was curated as a part of https://www.nature.com/articles/s41586-020-2559-3
## information_metrics
To sample interesting regions, there are metrics to measure the information content and quality of individual DHSs, namely:
#### 1. Entropy:
the randomness of a DHS
#### 2. Average Normalized Signal:
a comparable way to measure the accesibility levels of DHSs
#### 3. Signal to Noise Ratio (SNR):
the fraction that represents the ratio of highly represented biosamples in a DHS to that of lowly expressed ones.
#### 4. Mean Cosine Similarity (MCS):
measure of similarity among the most highly expressed biosamples of a DHS
#### 5. Concordance Metric:
the only metric that utilizes the reduced representation of the data, using NMF. It is computed as the average similarity is classification of a DHS into a cell type with that of the classification of the corresponding biosamples that are highly represented in it. We use this metric as teh ground truth to evaluate others.
Co-ranking just the SNR and MCS produced best results. 
## metric_exploration
We cluster the most highly ranked DHSs by each metric and order them optimally to create a heatmap to visualize the effect of ranking by each metic and find out of there is any cell-type specificity to the DHSs picked by a certain metric.
## metric_evaluation_and_comparison
We compare the ranked lists from various metrics and compute the similarity in ranking using [Fisher exact statistic](https://en.wikipedia.org/wiki/Fisher%27s_exact_test), [Rank Biased Overlap] (http://blog.mobile.codalism.com/research/papers/wmz10_tois.pdf).
## 25kb_dhs_regions
As a proof of concept to measure information content at scale, using the ranking metrics above, we divided the whole human genome into 25kb regions created as a result of using the chromatin states data that use an information theoretic metric to extract surprisal scores along the entire genome. We ranked the resulting approximately 100,000 regions based on:
   1. Their significance scores obtained using the mean co-ranks of DHSs in the region. Co-ranks based on the information metrics descrined above. Then         use the Central Limit Theorem to ascertain their significance.
   2. The homogeneity of enrichment of the signal from various NMF components (cell types).
   3. Again, we co-ranked the two scores from above to obtain a ranking of the  25kb regions of DHS data that are significantly informative in terms of         their constituent DHSs.
## scale_max_significance
ranking_roi_at_scale_AJ20221122.ipynb: Given a genomic region of interest, find the scale at which it maximizes its information content.

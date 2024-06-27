# Analyzing Citation Networks

## Dependency libraries used

1. PyTorch and PyTorch geometric

2. Networkx for building graph and analysis

3. Matplotlib for plotting

4. Sklearn's TSNE for visualizing node embeddings and others for Logistic Regression

5. Random module from python

6. Numpy

7. Gensim.models for Word2Vec (Node2Vec uses Word2Vec)

## Directory Structure

```
.
├── Analysis.ipynb
├── BasedOnYear.ipynb
├── BuildGraphFile.ipynb
├── CommDetection.ipynb
├── Datasets
│   ├── 1992to1993.txt
│   ├── 1992to1994.txt
│   ├── 1992to1995.txt
│   ├── 1992to1996.txt
│   ├── 1992to1997.txt
│   ├── 1992to1998.txt
│   ├── 1992to1999.txt
│   ├── 1992to2000.txt
│   ├── 1992to2001.txt
│   ├── 1994to1998.txt
│   ├── 1994to2001.txt
│   ├── 1996to2002.txt
│   ├── 1997to2002.txt
│   ├── 2000to2002.txt
│   ├── cit-HepPh-dates.txt
│   └── cit-HepPh.txt
├── datasetTime.py
├── GNNCommDet.ipynb
├── Graphs
│   ├── 1992to1995.png
│   ├── 1992to1998wolabs.png
│   ├── Graph1.png
│   └── Graph25%.png
├── node2vec.ipynb
├── PaperPredictor.ipynb
├── Paper-reading task.pptx
├── Plots and metrics
│   ├── 1992to1996.png
│   ├── 1994to1998.png
│   ├── close_cent.png
│   ├── ClustCo_emb.png
│   ├── density_cent.png
│   ├── eigen_cent.png
│   ├── nodeembvis92to98.png
│   ├── nodeembvispf.png
│   ├── noofcitations.png
│   ├── noofcomm_Girvan-Newmann.png
│   ├── noofcomm_Louvain.png
│   ├── noofpapers.png
│   ├── num_papervscit.png
│   ├── num_papervsref.png
│   ├── strconncomp.png
│   └── YearofPaperMostUsed.png
├── README.md
├── Report.pdf
└── Unsup.ipynb

3 directories, 48 files

```
## What are these files and directories?

1. Analysis.ipynb has all the code for graph analysis done and mentioned in the report.

2. BasedOnYear.ipynb has the GNN supervised model which uses year of submission as label.

3. BuildGraphFile.ipynb has the code for building Gephi supported file for Graph rendering.

4. CommDetection.ipynb has the code for Girvan-Newmann (naive Louvain) and efficient Louvain community analysis.

5. Datasets folder has all the datasets that were created using the datasetTime.py file and also has original dataset from the given source.

6. GNNCommDet.ipynb has the code for supervised GNN using clustering coefficient as the label.

7. Graphs folder has some graphs rendered using Gephi.

8. node2vec.ipynb has implementation for node2vec algorithm and node classification+link prediction tasks using the same.

9. PaperPredictor.ipynb has the model that could be used for predicting number of papers in upcoming years after 2001. (We predicted number of papers overall in 2002 using this).

10. Plots and metrics has all the plots that were included in the report.

11. Report.pdf is the report that includes all the findings, methodologies and approach followed for completing the tasks.

12. Unsup.ipynb has the unsupervised GNN model that gives node embeddings. This GNN was used for link prediction task as well, embeddings were visualized here as well.


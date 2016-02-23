# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:10:31 2015

@author: lizzybradley
"""

# Basic math operations:
import numpy as np 

# Data munging
import pandas as pd

# Learning and Transforming
from sklearn.decomposition import PCA

# Graphing utilities:
import matplotlib.pyplot as plt

# Rows are observations, columns are features of each run
# Turn it into a pandas DataFrame, normalize it
X = np.recfromcsv("../Data/19_frequency.csv",
                     delimiter=',', case_sensitive=True, deletechars='', 
                     replace_space=' ', usecols=(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,38,39,40,41,42,43))

df = pd.DataFrame(X, copy=True)
# df = (df - df.mean()) / df.std()
df = df / (df.max() - df.min())

n = min(df.shape)
pca = PCA(n_components = n)
pca.fit(df)
var = pca.explained_variance_ratio_
expVar = np.cumsum(var)

threshold = 0.95
numExp = len([x for x in expVar if x < threshold])

i = 0
for name in list(df):
    print str(i) + " " + name
    i += 1

expVarFig = plt.figure()
expVarPlot = plt.plot(range(0, len(expVar)), expVar,'b', lw = 2)
thresholdPlot = plt.plot([0, len(expVar)], [threshold, threshold], 'r', lw = 1)
cutoffPlot = plt.plot([numExp, numExp], [0,1], 'r', lw = 1)
plt.title('Cumulative Explained Variance of PCs')
plt.xlabel('PC')
plt.ylabel('Portion of Explained Variance')
plt.savefig('img/PCA/VarianceExplained.png')

# Find the contributing features
topPCs = np.abs(pca.components_[0:numExp,:])
topPCsScaled = np.array([var[i] * topPCs[i,:] for i in range(0, topPCs.shape[0])])
totals = topPCsScaled.sum(0)

print (totals)
importancePlt = plt.figure()
plt.title('Scaled Feature Contribution to PCs')
plt.xlabel('Feature')
plt.ylabel('Contribution to top 95\% PCs (a.u.)')
plt.bar(range(0,len(totals)), totals)
plt.savefig('img/PCA/FeatureImportance.png')
plt.show()
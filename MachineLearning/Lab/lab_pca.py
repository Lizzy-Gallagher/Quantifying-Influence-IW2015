# Basic math operations:
import numpy as np 
import math

# Data munging
import scipy.io as MATload
import pandas as pd
# from sklearn.cross_validation import train_test_split


# Learning and Transforming
from sklearn.decomposition import PCA

# Graphing utilities:
import matplotlib.pyplot as plt

# Rows are observations, columns are features of each run
# Turn it into a pandas DataFrame, normalize it
X = np.array(MATload.loadmat('Cancer.mat')['X'])
df = pd.DataFrame(X, copy=True)
df = (df - df.mean()) / (df.max() - df.min())


n = min(df.shape)
pca = PCA(n_components = n)
pca.fit(df)
var = pca.explained_variance_ratio_
expVar = np.cumsum(var)

threshold = 0.95
numExp = len([x for x in expVar if x < threshold])

expVarFig = plt.figure()
expVarPlot = plt.plot(range(0, len(expVar)), expVar,'b', lw = 2)
thresholdPlot = plt.plot([0, len(expVar)], [threshold, threshold], 'r', lw = 1)
cutoffPlot = plt.plot([numExp, numExp], [0,1], 'r', lw = 1)
plt.title('Cumulative Explaiend Variance of PCs')
plt.xlabel('PC')
plt.ylabel('Portion of Explained Variance')
plt.savefig('PCA_VarExp.png')

# Find the contributing features
topPCs = np.abs(pca.components_[0:numExp,:])
topPCsScaled = np.array([var[i] * topPCs[i,:] for i in range(0, topPCs.shape[0])])
totals = topPCsScaled.sum(0)

print totals
importancePlt = plt.figure()
plt.title('Scaled Feature Contribution to PCs')
plt.xlabel('Feature')
plt.ylabel('Contribution to top 95\% PCs (a.u.)')
plt.bar(range(0,len(totals)), totals)
plt.savefig('PCA_FeatureImportance.png')
plt.show()

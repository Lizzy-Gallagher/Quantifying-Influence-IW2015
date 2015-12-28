# Basic math operations:
import numpy as np 
import math

# Data munging
import scipy.io as MATload
import pandas as pd
from sklearn.cross_validation import StratifiedKFold

# Learning stuff!
from sklearn.svm import SVC
from sklearn.feature_selection import RFECV

# Graphing utilities:
import matplotlib.pyplot as plt


X = np.array(MATload.loadmat('Cancer.mat')['X'])
y = np.array(MATload.loadmat('Cancer.mat')['Y'])[:,0]
df = pd.DataFrame(X, copy=True) 
df = (df - df.mean()) / (df.max() - df.min())


# Let Python handle cross validation and testing!
skf = StratifiedKFold(y, n_folds = 10) 
svc = SVC(C = 1, kernel = "linear")
# Estimator is learner to be used to determine feature importance
# Step gives the number of features removed at each step
# CV takes a cross-validation object
# Scoring accuracy option is proportional to number of correct classifications
rfecv = RFECV(estimator = svc, step = 1, cv = skf, scoring = 'accuracy')
rfecv.fit(df, y)

print("Optimal number of features : %d" % rfecv.n_features_)
print "those features are:"
print rfecv.get_support(indices = True)


# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (proportion of correct classifications)")
plt.title('Recursive Feature Elimination with CV performance. ')
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_, lw = 2)
plt.xlim([1, len(rfecv.grid_scores_)])
plt.savefig('RFECV_features.png')
plt.show()




# Basic math operations:
import numpy as np 

# Data munging
import pandas as pd
from sklearn.cross_validation import StratifiedKFold

# Learning and Transforming
from sklearn.linear_model import LassoCV

# Graphing utilities:
import matplotlib.pyplot as plt


# csv = np.genfromtxt("DataCollection/Data/4_xtools.csv", delimiter=",")

X = np.recfromcsv("DataCollection/Data/5_no_double_votes.csv",
                     delimiter=',', case_sensitive=True, deletechars='', 
                     replace_space=' ', usecols=(3,6,8,10,11,12,13,14,15,16,17,20,21,22,23,24))
y = np.recfromcsv("DataCollection/Data/5_no_double_votes.csv",
                     delimiter=',', case_sensitive=True, deletechars='', 
                     replace_space=' ', usecols=(2))

xshape = X.shape[0]
yshape = y.shape[0]


df = pd.DataFrame(X, copy=True) 
df = (df - df.mean()) / (df.max() - df.min())

# Cross Validation object
skf = StratifiedKFold(y, n_folds = 10)

# See how Lasso performs
testAlphas = np.logspace(-8, 8, 33, endpoint = True, base = 10)
lassoCV = LassoCV(alphas = testAlphas, fit_intercept = False, normalize = False,cv = skf, max_iter = 10000000, tol = 0.0001)
lassoCV.fit(X,y)
meanMSE = np.mean(lassoCV.mse_path_, 1)
optAlpha = lassoCV.alpha_
print (optAlpha)

plt.figure()
plt.plot(lassoCV.alphas_, meanMSE, lw = 2)
plt.title('Lasso performance')
plt.ylabel('Average MSE (over 10 folds)')
plt.rcParams['text.usetex'] = True
plt.xlabel(r'$\alpha$')
plt.plot([optAlpha, optAlpha], [np.min(meanMSE) * 0.8, np.max(meanMSE) * 1.2])
plt.xscale('log')
plt.savefig('Lasso_performance.png')



# Do the feature selection
sfm = SelectFromModel(LassoCV(), threshold=0.0001)
sfm.fit(X,y)
n_features = sfm.transform(X).shape[1]

while n_features / float(X.shape[1]) > 0.25:
    sfm.threshold += 0.01
    X_transform = sfm.transform(X)
    n_features = X_transform.shape[1]

# Which features were they?
X_transform = sfm.transform(X)
n_features = X_transform.shape[1]
print (sfm.get_support(indices = True))

# Show performance on just these features:
lassoCV_primaryFeatures = LassoCV(alphas = testAlphas, fit_intercept = False, normalize = False, cv = skf, max_iter = 10000000, tol = 0.0001)
lassoCV_primaryFeatures.fit(X_transform,y)
meanMSE_primaryFeatures = np.mean(lassoCV_primaryFeatures.mse_path_,1)
optAlpha = lassoCV_primaryFeatures.alpha_
plt.figure()
plt.plot(lassoCV_primaryFeatures.alphas_, meanMSE_primaryFeatures, lw = 2)
plt.title('Lasso performance on primary Features')
plt.ylabel('Average MSE (over 10 folds)')
plt.rcParams['text.usetex'] = True
plt.xlabel(r'$\alpha$')
plt.plot([optAlpha, optAlpha], [np.min(meanMSE_primaryFeatures) * 0.5, np.max(meanMSE_primaryFeatures) * 1.2])
plt.xscale('log')
plt.savefig('Lasso_performance_primaryFeatures.png')
plt.show()





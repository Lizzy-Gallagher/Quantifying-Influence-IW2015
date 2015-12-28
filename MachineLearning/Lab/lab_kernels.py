# Basic math operations:
import numpy as np 
import math

# Data munging
import scipy.io as MATload
import pandas as pd
from sklearn.cross_validation import train_test_split

# Learning stuff!
from sklearn.svm import SVC
from sklearn.feature_selection import RFECV

# Graphing utilities:
import matplotlib.pyplot as plt

# Rows are observations, columns are features of each run
# Turn it into a pandas DataFrame
X = np.array(MATload.loadmat('Cancer.mat')['X'])
y = np.array(MATload.loadmat('Cancer.mat')['Y'])[:,0]
df = pd.DataFrame(X, copy=True) 
# df = (df - df.mean()) / (df.max() - df.min())

# Split into training and testing sets
p = 0.9
dataTrain, dataTest, labelsTrain, labelsTest = train_test_split(df, y, train_size = p, random_state = 314)

# Test some different kernels for across different penalties
Cs = np.logspace(-5, 7, 13, endpoint = True, base = 10)
errLinear = []
for c in Cs: 
    print 'Linear, %f' % c
    svmLINEAR = SVC(C = c, kernel = 'linear')
    svmLINEAR.fit(dataTrain, labelsTrain)
    predictions = svmLINEAR.predict(dataTest)
    errLinear.append(len([i for i in range(0,len(predictions)) if predictions[i] != labelsTest[i]])/ float(len(predictions)))

errPoly = []
for c in Cs:
    print 'Poly, %f' % c
    svmPOLY = SVC(C = c, kernel = 'poly')
    svmPOLY.fit(dataTrain, labelsTrain)
    predictions = svmPOLY.predict(dataTest)
    errPoly.append(len([i for i in range(0,len(predictions)) if predictions[i] != labelsTest[i]])/ float(len(predictions)))

errGauss = []
for c in Cs:
    print 'Gauss, %f' % c
    svmGAUSS = SVC(C = c, kernel = 'rbf')
    svmGAUSS.fit(dataTrain, labelsTrain)
    predictions = svmGAUSS.predict(dataTest)
    errGauss.append(len([i for i in range(0,len(predictions)) if predictions[i] != labelsTest[i]])/ float(len(predictions)))

errSig = []
for c in Cs:
    print 'Sigmoid, %f' % c
    svmSIG = SVC(C = c, kernel = 'sigmoid')
    svmSIG.fit(dataTrain, labelsTrain)
    predictions = svmSIG.predict(dataTest)
    errSig.append(len([i for i in range(0,len(predictions)) if predictions[i] != labelsTest[i]])/ float(len(predictions)))



CsFig = plt.figure()
CsLinearPlot = plt.plot(Cs, errLinear, 'b', lw = 2, label = 'linear')
CsPolyPlot = plt.plot(Cs, errPoly,'r', lw = 2, label = 'polynomial')
CsGaussPlot = plt.plot(Cs, errGauss,'m', lw = 2, label = 'gaussian')
CsSigPlot = plt.plot(Cs, errSig,'c', lw = 2, label = 'sigmoid')
plt.xscale('log')
plt.xlabel('C')
plt.ylabel('Error')
plt.legend(loc = 3)
plt.title('SVM Kernels')
plt.savefig('MultiSVM_errors.png')
plt.show()







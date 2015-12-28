# Basic math operations:
import numpy as np 
import math

# Data munging
import scipy.io as MATload
import pandas as pd
from sklearn.cross_validation import train_test_split

# Learning and Transforming
from sklearn.ensemble import RandomForestClassifier

# Graphing utilities:
import matplotlib.pyplot as plt

X = np.recfromcsv("../DataCollection/Data/11_recover.csv",
                     delimiter=',', case_sensitive=True, deletechars='', 
                     replace_space=' ', usecols=(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28))
y = np.recfromcsv("../DataCollection/Data/11_recover.csv",
                     delimiter=',', case_sensitive=True, deletechars='', 
                     replace_space=' ', usecols=(2))
df = pd.DataFrame(X, copy=True) 
df = (df - df.mean()) / (df.max() - df.min())

# Split into training and testing sets
p = 0.75
dataTrain, dataTest, labelsTrain, labelsTest = train_test_split(df, y, train_size = p, random_state = 314)
print (dataTrain.shape)
print (labelsTrain.shape)
maxLearners = np.floor(np.sqrt(dataTrain.shape[0]))
nLearners = np.linspace(1, maxLearners, maxLearners)
print (nLearners)
maxDepth = np.floor(np.sqrt(X.shape[0]))
err = []
bestN = 0
for n in nLearners:
    rf = RandomForestClassifier(n_estimators = int(n), max_depth = maxDepth, max_features = 'sqrt')
    rf.fit(dataTrain, labelsTrain)
    predictions = rf.predict(dataTest)
    error = len([i for i in range(0,len(predictions)) if predictions[i] != labelsTest[i]]) / float(len(predictions))
    print (error)
    err.append(error)
    if error == np.min(err):
        bestN = n

performancePlt = plt.figure()
plt.title('Random Forest Performance')
plt.xlabel('Number of Learners')
plt.ylabel('Error Rate')
plt.plot(nLearners, err, lw = 2)
plt.savefig('RF_Performance.png')



rf = RandomForestClassifier(n_estimators = int(bestN), max_depth = maxDepth, max_features = 'sqrt')
rf.fit(dataTrain, labelsTrain)
importance = rf.feature_importances_
print (importance)
importancePlt = plt.figure()
plt.title('Feature Importance by Optimal Random Forest')
plt.xlabel('Feature')
plt.ylabel('Feature Importance')
plt.bar(range(0,len(importance)),importance)
plt.savefig('RF_FeatureImportance.png')
plt.show()

__author__ = 'lizzybradley'

filename = "../Data/19_frequency.csv"

# Basic math operations:
import numpy as np

# Data munging
import pandas as pd
from sklearn.cross_validation import train_test_split

# Learning and Transforming
from sklearn.ensemble import RandomForestClassifier

# Graphing utilities:
import matplotlib.pyplot as plt

X = np.recfromcsv(filename,
                     delimiter=',', case_sensitive=True, deletechars='',
                     replace_space=' ', usecols=(3,4,5,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32))
y = np.recfromcsv(filename,
                     delimiter=',', case_sensitive=True, deletechars='',
                     replace_space=' ', usecols=(2))
                     
df = pd.DataFrame(X, copy=True)
# df = (df - df.mean()) / (df.max() - df.min())
# df = (df - df.mean()) / df.std()

print (df.describe)

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
plt.savefig('img/RandomForest/Performance.png')
plt.show()

rf = RandomForestClassifier(n_estimators = int(bestN), max_depth = maxDepth, max_features = 'sqrt')
rf.fit(dataTrain, labelsTrain)
importance = rf.feature_importances_
print (importance)
importancePlt = plt.figure()
plt.title('Feature Importance by Optimal Random Forest')
plt.xlabel('Feature')
plt.ylabel('Feature Importance')
plt.bar(range(0,len(importance)),importance)
plt.savefig('img/RandomForest/FeatureImportance.png')
plt.show()

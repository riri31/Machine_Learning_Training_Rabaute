#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#### error ####

data_without_total=data_dict.copy()
del data_without_total['TOTAL']
data = featureFormat(data_without_total, features)

print 'Maximum salary for , bonus:{}'.format(np.amax(data, axis=0))

for item in data_without_total:
    if data_without_total[item]['salary']==np.amax(data, axis=0)[0]:
        print 'found,{},{}'.format(item,data_without_total[item])

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

#### second cleaning

bandits=[]

for point in data:
    if point[0] > 1000000 and point[1] > 5000000:
        bandits.append(point)

print bandits

for item in data_without_total:
    if data_without_total[item]['salary']>1000000 and data_without_total[item]['bonus']> 5000000 and data_without_total[item]['salary']<>'NaN' :
        print 'found,{},{}'.format(item,data_without_total[item])





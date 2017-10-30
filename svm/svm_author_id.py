#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np

svm_clf = svm.SVC(C=10000,kernel='rbf')
t0 = time()
clf = svm_clf.fit(features_train,labels_train)
#clf = gnb.fit( features_test,labels_test)
print "training time:", round(time()-t0, 3), "s"


t0 = time()                          
predict_labels=clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"

accuracy_score_mail=accuracy_score(labels_test,predict_labels)
print 'Accuracy score:{}%'.format(round(accuracy_score_mail*100,2))

for i in [10,26,50]:
    if predict_labels[i]==0:
        author='sara'
    else:
        author='chris'
    print '{}: {}({})'.format(i,author,predict_labels[i])

print 'chris ={}'.format(np.count_nonzero(predict_labels==1))  
print 'sara ={}'.format(np.count_nonzero(predict_labels==0))  
#########################################################

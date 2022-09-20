# -*- coding: utf-8 -*-
"""Decision_tree_Entropy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HKuoV1n_leDTGFMIsBhJjIGQTlqgXyH8
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing  import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import numpy as np

df=pd.read_csv("/content/heart.csv")
df

X=df.drop('output',axis=1)
Y=df['output']
X.head

Y.head()

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2)
X_train

y_train

X_train = StandardScaler().fit_transform(X_train)
X_train

X_test = StandardScaler().fit_transform(X_test)
X_test

from sklearn.tree import DecisionTreeClassifier
dtree =  DecisionTreeClassifier(criterion='entropy', random_state=0)
dtree = dtree.fit(X_train,y_train)
dtree

y_test

y_pred=dtree.predict(X_test)
y_pred

from sklearn import metrics
import matplotlib.pyplot as plt
cm=metrics.confusion_matrix(y_pred,y_test)
cm
plt.plot(cm)

from sklearn.tree import export_graphviz
import graphviz
graphviz.Source(export_graphviz(dtree,feature_names=X.columns,filled=True,class_names=['0','2','3','4','5','6']))

from sklearn import tree
tree.plot_tree(dtree)
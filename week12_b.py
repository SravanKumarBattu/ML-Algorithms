# -*- coding: utf-8 -*-
"""week12_b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wOjxSQA-z2o_VQHw77Cy7Za06yqBnqQG
"""

from sklearn.ensemble import GradientBoostingClassifier
boost_class=GradientBoostingClassifier(n_estimators=10,random_state=3)

from sklearn.datasets import load_breast_cancer
dataset=load_breast_cancer()
x=dataset.data
y=dataset.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=3)

boost_class.fit(x_train,y_train)
boost_class.score(x_test,y_test)


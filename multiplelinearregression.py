# -*- coding: utf-8 -*-
"""MultipleLinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16l90YrE04ICsNKhWOmoU2pVnyp24N2c8
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset=datasets.load_boston()

dataset

#feature engineering
dataset_pd=pd.DataFrame(dataset.data)
dataset_pd

dataset_pd.columns=dataset.feature_names
dataset_pd

dataset_pd_target=np.asarray(dataset.target)
dataset_pd

dataset_pd['House_Price']=pd.Series(dataset_pd_target)
dataset_pd

X=dataset_pd.iloc[:,:-1]
X

Y=dataset_pd.iloc[:,-1]
Y



x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.25)
y_test.mean()
print("Train data shape of X =%s and Y = %s"%(x_train.shape,y_train.shape))
print("Test data shape of X =%s and Y = %s"%(x_test.shape,y_test.shape))

#MULTIPLE LINEAR REGRESSIOn
lreg=LinearRegression()
lreg.fit(x_train,y_train)

#generate pridiction on test dataset
lreg_y_pred=lreg.predict(x_test)

#calculte mse
mean_squared_error=np.mean((lreg_y_pred-y_test)**2)

print(lreg.score(x_train,y_train))
print(lreg.score(x_test,y_test))
print("Mean Squared Error on Test set : ",mean_squared_error)

#coefficients and the features
lreg_coefficient=pd.DataFrame()
lreg_coefficient["Columns"]=x_train.columns
lreg_coefficient["Coefficient Estimate"]= pd.Series(lreg.coef_)
print(lreg_coefficient)

fig,ax=plt.subplots(figsize=(10,5))
color=['tab:gray','tab:blue','tab:orange','tab:green','tab:blue','tab:purple',
       'tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan','tab:orange','tab:green','tab:blue','tab:olive']
ax.bar(lreg_coefficient["Columns"],lreg_coefficient["Coefficient Estimate"],color=color)

ax.spines['bottom'].set_position('zero')

plt.style.use('ggplot')
plt.show()

#applying RIDGE Regularisation L2

from sklearn.linear_model import Ridge

#train
ridgeR=Ridge(alpha=1)
ridgeR.fit(x_train,y_train)
#predict
y_pred=ridgeR.predict(x_test)
print(ridgeR.score(x_train,y_train))
print(ridgeR.score(x_test,y_test))
msq=np.mean((y_pred-y_test)**2)
print("MEAN SQUARRED ERROR: ",msq)

r_co=pd.DataFrame()
r_co["Columns"]=x_train.columns
r_co["Coefficient Estimate"]=pd.Series(ridgeR.coef_)
print(r_co)

fig,ax=plt.subplots(figsize=(20,10))
color=['tab:gray','tab:blue','tab:orange','tab:green','tab:blue','tab:purple',
       'tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan','tab:orange','tab:green','tab:blue','tab:olive']
ax.bar(r_co["Columns"],r_co["Coefficient Estimate"],color=color)

ax.spines['bottom'].set_position('zero')

plt.style.use('ggplot')
plt.show()

#applying RIDGE Regularisation L2

from sklearn.linear_model import Lasso

#train
lasso=Lasso(alpha=1)
lasso.fit(x_train,y_train)
#predict
y_pred1=lasso.predict(x_test)

print(lasso.score(x_train,y_train))
print(lasso.score(x_test,y_test))
msq=np.mean((y_pred1-y_test)**2)
print("MEAN SQUARRED ERROR: ",msq)

l_co=pd.DataFrame()
l_co["Columns"]=x_train.columns
l_co["Coefficient Estimate"]=pd.Series(lasso.coef_)
print(l_co)

fig,ax=plt.subplots(figsize=(20,10))
color=['tab:gray','tab:blue','tab:orange','tab:green','tab:blue','tab:purple',
       'tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan','tab:orange','tab:green','tab:blue','tab:olive']
ax.bar(l_co["Columns"],l_co["Coefficient Estimate"],color=color)

ax.spines['bottom'].set_position('zero')

plt.style.use('ggplot')
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:31:22 2020

@author: Careen
"""

##Iris data set practise
##loading the data
from statsmodels.api import datasets

iris= datasets.get_rdataset("iris")
iris.data.columns= ["Sepal_Width", "Sepal_Length", "Petal_Length", "Petal_Width", "Species"]
iris.data

iris.data.dtypes


###plotting the data set
import matplotlib.pyplot as plt
import seaborn as sns
def plot_iris(iris, col1,col2):
    sns.lmplot(x = col1, y= col2,
               data= iris,
               hue="Species",
               fit_reg= False)
    plt.xlabel(col1) 
    plt.ylabel(col2)
    plt.title("Iris species shown by colour")
    plt.show
plot_iris(iris.data, "Petal_Length","Sepal_Width")
plot_iris(iris.data, "Sepal_Length", "Petal_Width")











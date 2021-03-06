from numpy import *
from sklearn.datasets import load_iris

iris = load_iris()
samples = iris.data
#print(samples)
target = iris.target

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression() #使用类，参数全是默认的
classifier.fit(samples,target) #训练数据来学习，不需要返回值
x = classifier.predict(array([5,3,5,2.5]).reshape(1,-1)) #测试数据，分类返回标记

print(x)
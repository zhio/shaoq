import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data[:,2:]

# plt.scatter(X[:,0],X[:,1],c = "red",marker='o',label = 'see')
# plt.xlabel('petal length')
# plt.ylabel('petal width')
# plt.legend(loc = 2)
# plt.show()
estimatr = KMeans(n_clusters=3)
estimatr.fit(X)
label_pred = estimatr.labels_
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:,0],x0[:,1],c = "red",marker='o',label='label0')
plt.scatter(x1[:,0],x1[:,1],c = "green", marker= '*',label = 'label1')
plt.scatter(x2[:,0],x2[:,1],c = 'blue', marker='+',label = 'label2')
plt.xlabel('length')
plt.ylabel('width')
plt.legend(loc=2)
plt.show()
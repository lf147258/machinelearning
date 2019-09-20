#-*- coding: UTF-8 -*-
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X,y=make_blobs(random_state=1)
kmeans=KMeans(n_clusters=3)
kmeans.fit(X)
print(kmeans.labels_)
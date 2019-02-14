import pandas as pd
import io
import json
import requests
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

r_file = 'crowdfunding_parsed.json'
json_read = pd.read_json(r_file)
abst=json_read['abstract']
print(type(abst))
##Number of clusters for each page
clust_num=round(len(abst)/10)
print(clust_num)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(abst)

true_k = clust_num
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])

print("\n")
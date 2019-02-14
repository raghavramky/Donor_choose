import pandas as pd
import io
import json
import requests
import math
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score


f=open("ss.txt","w") 
r_file = 'crowdfunding_parsed.json'
json_read = pd.read_json(r_file)
abst=json_read['abstract']
print(type(abst))
##Number of clusters for each page
clust_num=math.floor(len(abst)/10)
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
    print("\n")
    lists=[]
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        lists.append(terms[ind])
    print(lists),    
    print

print("\n")
Y = vectorizer.transform(abst)
prediction = model.predict(Y)
k=prediction

print(k)


'''
num=0
for i in range(0,126):
    clus=[]
    
    for j in range(0,clust_num):
        if(k[i]==j):
            num=num+1
            clus.append(abst[i])
            print("Cluster %d \n"%num)
            print(clus)
'''
clus0=[]
clus1=[]
clus2=[]
clus3=[]
clus4=[]
clus5=[]
clus6=[]
clus7=[]
clus8=[]
clus9=[]
clus10=[]
clus11=[]
for i in range(0,126):
    if(k[i]==0):
        clus0.append(abst[i])
    elif(k[i]==1):
        clus1.append(abst[i])
    elif(k[i]==2):
        clus2.append(abst[i])
    elif(k[i]==3):
        clus3.append(abst[i])
    elif(k[i]==4):
        clus4.append(abst[i])
    elif(k[i]==5):
        clus5.append(abst[i])
    elif(k[i]==6):
        clus6.append(abst[i])
    elif(k[i]==7):
        clus7.append(abst[i])
    elif(k[i]==8):
        clus8.append(abst[i])
    elif(k[i]==9):
        clus9.append(abst[i])
    elif(k[i]==10):
        clus10.append(abst[i])
    elif(k[i]==11):
        clus11.append(abst[i])


f.write("Clus0:\n\n")
f.write(str(clus0))
f.write("\n\nClus1:\n\n")
f.write(str(clus1))
f.write("\n\nClus2:\n\n")
f.write(str(clus2))
f.write("\n\nClus3:\n\n")
f.write(str(clus3))
f.write("\n\nClus4:\n\n")
f.write(str(clus4))
f.write("\n\nClus5:\n\n")
f.write(str(clus5))
f.write("\n\nClus6:\n\n")
f.write(str(clus6))
f.write("\n\nClus7:\n\n")
f.write(str(clus7))
f.write("\n\nClus8:\n\n")
f.write(str(clus8))
f.write("\n\nClus9:\n\n")
f.write(str(clus9))
f.write("\n\nClus10:\n\n")
f.write(str(clus10))
f.write("\n\nClus11:\n\n")
f.write(str(clus11))

f.close()

import pandas as pd
import io
import json
import requests
import math
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

f=open("ss8.txt","w") 
with open('crowdfunding_parsed.json') as f1:
    data=json.load(f1)
leng=len(data)
var=[]
for i in range(len(data)):
    var.append(data[i].get('abstract',None))    
#pprint(var)
#var=var.replace(",","\n")

clust_num=math.floor(len(var)/10)
print(clust_num)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(var)

true_k = clust_num
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1, random_state =0)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
clusters=[]
for i in range(true_k):
    print("\n")
    lists=[]
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        lists.append(terms[ind])
        clusters.append(lists)
    print(lists)

print("\n")

Y = vectorizer.transform(var)
prediction = model.predict(Y)
k=prediction
print(k)

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
        clus0.append(var[i])
    elif(k[i]==1):
        clus1.append(var[i])
    elif(k[i]==2):
        clus2.append(var[i])
    elif(k[i]==3):
        clus3.append(var[i])
    elif(k[i]==4):
        clus4.append(var[i])
    elif(k[i]==5):
        clus5.append(var[i])
    elif(k[i]==6):
        clus6.append(var[i])
    elif(k[i]==7):
        clus7.append(var[i])
    elif(k[i]==8):
        clus8.append(var[i])
    elif(k[i]==9):
        clus9.append(var[i])
    elif(k[i]==10):
        clus10.append(var[i])
    elif(k[i]==11):
        clus11.append(var[i])

    
f.write("Cluster 0:\n\n")
f.write(str(clusters[0])+"\n")
for count in range(len(clus0)):
	f.write(str(clus0[count]))
	f.write("\n\n")

f.write("\n\nCluster 1:\n\n")
f.write(str(clusters[1])+"\n")
for count in range(len(clus1)):
	f.write(str(clus1[count]))
	f.write("\n\n")

f.write("\n\nCluster 2:\n\n")
f.write(str(clusters[2])+"\n")
for count in range(len(clus2)):
	f.write(str(clus2[count]))
	f.write("\n\n")

f.write("\n\nCluster 3:\n\n")
f.write(str(clusters[3])+"\n")
for count in range(len(clus3)):
	f.write(str(clus3[count]))
	f.write("\n\n")

f.write("\n\nCluster 4:\n\n")
f.write(str(clusters[4])+"\n")
for count in range(len(clus4)):
	f.write(str(clus4[count]))
	f.write("\n\n")

f.write("\n\nCluster 5:\n\n")
f.write(str(clusters[5])+"\n")
for count in range(len(clus5)):
	f.write(str(clus5[count]))
	f.write("\n\n")

f.write("\n\nCluster 6:\n\n")
f.write(str(clusters[6])+"\n")
for count in range(len(clus6)):
	f.write(str(clus6[count]))
	f.write("\n\n")

f.write("\n\nCluster 7:\n\n")
f.write(str(clusters[7])+"\n")
for count in range(len(clus7)):
	f.write(str(clus7[count]))
	f.write("\n\n")

f.write("\n\nCluster 8:\n\n")
f.write(str(clusters[8])+"\n")
for count in range(len(clus7)):
	f.write(str(clus7[count]))
	f.write("\n\n")

f.write("\n\nCluster 9:\n\n")
f.write(str(clusters[9])+"\n")
for count in range(len(clus9)):
	f.write(str(clus9[count]))
	f.write("\n\n")
f.write("\n\nCluster 10:\n\n")
f.write(str(clusters[10])+"\n")
for count in range(len(clus10)):
	f.write(str(clus10[count]))
	f.write("\n\n")
f.write("\n\nCluster 11:\n\n")
f.write(str(clusters[11])+"\n")
for count in range(len(clus11)):
	f.write(str(clus11[count]))
	f.write("\n\n")

f.close()


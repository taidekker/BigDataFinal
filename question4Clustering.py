'''
(Clustering) Cluster the data using this columns:
bedrooms, bathrooms, sqft_living, floors, waterfront, price. Name the clusters.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

dataset = pd.read_csv('C:\\Users\\Christian\\Desktop\\archive\\kc_house_data.csv')
#print(dataset)

cols = ['bedrooms','bathrooms','sqft_living','floors','waterfront','price']
data = dataset[cols]
#print(data)

from sklearn.cluster import AgglomerativeClustering
 
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
cluster.fit(data.values)

print(cluster.labels_)

cluster0 = data[cluster.labels_ == 0]
cluster1 = data[cluster.labels_ == 1]
cluster2 = data[cluster.labels_ == 2]
 
import statistics as st
 
print("Cluster 0")
for i in range(6):
    print(str(round(st.mean(cluster0.iloc[:,i]), 2)) + ": " + cluster0.columns[i])
 
print("\n")
print("Cluster 1")
for i in range(6):
    print(str(round(st.mean(cluster1.iloc[:,i]), 2)) + ": " + cluster0.columns[i])
 
print("\n") 
print("Cluster 2")
for i in range(6):
    print(str(round(st.mean(cluster2.iloc[:,i]), 2)) + ": " + cluster0.columns[i])
  
plt.scatter(data['price'], data['sqft_living'], c=cluster.labels_, cmap='rainbow')
plt.show()

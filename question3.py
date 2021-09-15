import numpy as np
import pandas as pd
import sklearn as sk
import sklearn.preprocessing as pre
import sklearn.tree as tree
from PIL import Image
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("./kc_house_data.csv")

label_encoder = pre.LabelEncoder()

label_encoder.fit(data['date'].astype(str))
data['date'] = label_encoder.transform(data['date'].astype(str))

X = data.drop(['waterfront'], axis=1)
Y = data['waterfront']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=50)

classifier = tree.DecisionTreeClassifier(max_depth=5, random_state=0)
decision_tree = classifier.fit(X_train, Y_train)

"""
out = open("tree1.dot","w")
dot_output = tree.export_graphviz(decision_tree, out_file=out,feature_names=['id','date','price', 'bedrooms','bathrooms','sqft_living','sqft_lot','floors','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15'],
    class_names = ['0','1'])

"""

print(decision_tree.predict(X_test))

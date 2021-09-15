import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

data = pd.read_csv('C:\\Users\\Christian\\Desktop\\archive\\kc_house_data.csv')

floors = data['floors']
aveNumFloors = np.mean(floors)
std = np.std(floors)
minFloors = np.min(floors)
maxFloors = np.max(floors)

print("Max Floors: " + str(round(maxFloors,2)))
print("Min Floors: " + str(round(minFloors,2)))
print("Average number of floors: " + str(round(aveNumFloors,2)))
print("Standard deviation: " + str(round(std,2)))

plt.hist(floors)
plt.show()

percentHomeWith2Floors = stats.norm.cdf(maxFloors,loc=aveNumFloors,scale=std) - stats.norm.cdf(2,loc=aveNumFloors,scale=std)
print("Percentage of houses with more than two floors" + str(round(percentHomeWith2Floors,2)))
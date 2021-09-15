import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

data = pd.read_csv('C:\\Users\\Christian\\Desktop\\archive\\kc_house_data.csv')

# Get homes with less than 2 floors
lessFloors = data['floors'] < 2
lessFloorsHomes = data[lessFloors]


# Get homes with 2 or more floors
moreFloors = data['floors'] > 2
moreFloorsHomes = data[moreFloors]


# Less than two floors price stats
lessFloorsPrice = lessFloorsHomes['price']
lessFloorsAvePrice = np.mean(lessFloorsPrice)
lessFloorMedianPrice = np.median(lessFloorsPrice)
lessFloorstd = np.std(lessFloorsPrice)
minLessFloorsPrice = np.min(lessFloorsPrice)
maxLessFloorsPrice = np.max(lessFloorsPrice)


# More than two floors price stats
morePrice = moreFloorsHomes['price']
moreFloorMedianPrice = np.median(morePrice)
moreFloorsAvePrice = np.mean(morePrice)
moreFloorstd = np.std(morePrice)
minMoreFloorsPrice = np.min(morePrice)
maxMoreFloorsPrice = np.max(morePrice)

# Print results for analysis
print("Price stats for homes with less than 2 floors.")
print("Min Price: " + str(round(minLessFloorsPrice,2)))
print("Max price: " + str(round(maxLessFloorsPrice,2)))
print("Median Price: " + str(round(lessFloorMedianPrice,2)))
print("Average Price: " + str(round(lessFloorsAvePrice,2)))
print("Standard deviation of ave price: " + str(round(lessFloorstd,2)))

print("")
print("***************************************************************************************")

print("Price stats for homes with less than 2 floors.")
print("Min Price: " + str(round(minMoreFloorsPrice,2)))
print("Max price: " + str(round(maxMoreFloorsPrice,2)))
print("Median Price: " + str(round(moreFloorMedianPrice,2)))
print("Average Price: " + str(round(moreFloorsAvePrice,2)))
print("Standard deviation of ave price: " + str(round(moreFloorstd,2)))
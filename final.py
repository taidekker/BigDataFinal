import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_pacf

# QUESTION 1
# (Statistics) What is the average home price in the zip code 98034 and what is the standard deviation.

data = pd.read_csv('./kc_house_data.csv')
# print(data)
data.head()

# shows us an information about our tables
data.info()
zip_code = data['zipcode'] == 98034
filterzip = data[zip_code]
price = filterzip['price']
price_avg = np.mean(price)
price_sd = np.std(price)

print("Average home price: " + str(round(price_avg, 2)))
print("Standard deviation: " + str(round(price_sd, 2)))

# QUESTION 2
# (Regression) What are the best predictors for home price from the ones in the file? Show the model.

plot_pacf(data['price'])
pyplot.show()

s = 'price'
shift = [1, 2, 23, 42, 43]
S = data[s]
s1 = S.shift(periods=1)
s2 = S.shift(periods=2)
s23 = S.shift(periods=23)
s42 = S.shift(periods=42)
s43 = S.shift(periods=43)

predictor = pd.DataFrame({'s1': s1, 's2': s2, 's23': s23, 's42': s42, 's43': s43})
Y = S[43:]
X = predictor[43:]
model = sm.OLS(Y, X)
print(model.fit().summary())
t = S.size
period = pd.DataFrame({'s1': [S[t - 1]], 's2': [S[t - 2]], 's23': [S[t - 23]], 's42': [S[t - 42]], 's43' : [S[t-43]]})
print(round(float(model.fit().predict(period)), 2))

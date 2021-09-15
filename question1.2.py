import folium
import pandas as pd

# How would you visualize houses location on the map ??

data = pd.read_csv('./kc_house_data.csv')


# finding the center of the map which will allow us to plot the data
# then we add each house as a circle onto the map. User can zoom in and out to see location of the houses

def findTheCenter(data):
    findCenterForLat = (data['lat'].max() + data['lat'].min()) / 2
    findCenterForLong = (data['long'].max() + data['long'].min()) / 2
    return findCenterForLat, findCenterForLong


center = findTheCenter(data)
makeMap = folium.Map(location=center, zoom_start=9)

for i in range(len(data)):
    folium.Circle(
        location=[data.iloc[i]['lat'], data.iloc[i]['long']],
        radius=10,
    ).add_to(makeMap)
# we save this as html file that we are able to open and see the map it allows us to zoom in and out
makeMap.save('houses-map.html')



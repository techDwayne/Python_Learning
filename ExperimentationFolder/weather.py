import requests
import json
import geocoder

# establish location
loc = input("City, ST?" )
 # pip install geocoder
g = geocoder.osm( loc )
results = g.json
#print(json.dumps(results, indent=4))
#print(results['lat'], results['lng'])
LAT = results['lat']
LNG = results['lng']
print(LAT)
print(LNG)

# get station and grid ids
url = f'https://api.weather.gov/points/{LAT},{LNG}'
station = requests.get(url)
station = station.json()
prop = station['properties']
grid_id = prop['gridId']
grid_x = prop['gridX']
grid_y = prop['gridY']

# get the forecast from the station
url = f'https://api.weather.gov/gridpoints' \
      f'/{grid_id}/{grid_x},{grid_y}/forecast/hourly'
fcast = requests.get(url)
fcast = fcast.json()


#print(json.dumps(fcast, indent=4))

#write to file
with open('fcast.json', 'w') as f:
      json.dump(fcast, f)

#how many hours to display
hours = input("Number of hours of forecast? ")
hrs=int(hours)
#print(hrs)
#loop through forecast, extract and print time, temp, windspd and short forcast for each hour
for i in range(0,hrs):
      time = fcast['properties']['periods'][i]["startTime"]
      temp = fcast['properties']['periods'][i]['temperature']
      wndspd = fcast['properties']['periods'][i]['windSpeed']
      shrtFore = fcast['properties']['periods'][i]['shortForecast']

      print(time)
      print(temp, 'F')
      print(wndspd)
      print(shrtFore)
      print('')








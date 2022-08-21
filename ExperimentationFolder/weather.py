import requests
import json

# establish location
LAT = 40.09768
LNG = -76.72323


# get station and grid ids
url = f'https://api.weather.gov/points/{LAT},{LNG}'
station = requests.get(url)
station = station.json()
prop = station['properties']
grid_id = prop['gridId']
grid_x = prop['gridX']
grid_y = prop['gridY']

# get the forecast
url = f'https://api.weather.gov/gridpoints' \
      f'/{grid_id}/{grid_x},{grid_y}/forecast/hourly'
fcast = requests.get(url)
fcast = fcast.json()

print(json.dumps(fcast, indent=4))

time = fcast['properties']['periods'][0]["startTime"]
temp = fcast['properties']['periods'][0]['temperature']
wndspd = fcast['properties']['periods'][0]['windSpeed']
shrtFore = fcast['properties']['periods'][0]['shortForecast']

print(time)
print(temp)
print(wndspd)
print(shrtFore)








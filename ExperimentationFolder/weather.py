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
forecast = requests.get(url)
forecast = forecast.json()

#print(json.dumps(forecast, indent=4))

time = forecast['properties']['periods'][0]["startTime"]
temp = forecast['properties']['periods'][0]['temperature']
wndspd = forecast['properties']['periods'][0]['windSpeed']
shrtFore = forecast['properties']['periods'][0]['shortForecast']

print(time)
print(temp)
print(wndspd)
print(shrtFore)








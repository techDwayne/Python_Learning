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

today = forecast['properties']['periods'][0]
text = today['shortForecast']

#print(today)
print(json.dumps(forecast, indent=4))
print(json.dumps(text,indent=4))









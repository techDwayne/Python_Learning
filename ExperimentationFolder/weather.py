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


#tdy = fcast['properties']['periods'][0]
#txt = tdy['shortForecast']
#temp_read=tdy['temperature']

#print(temp_read)
#print(txt)

fcast.raise_for_status()
fcast_data=json.loads(fcast.text)
weather=fcast_data['list']
print(weather)

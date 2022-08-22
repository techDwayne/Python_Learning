import json
import geocoder
import json

# establish location
loc = input("City, ST?" )
 # pip install geocoder
g = geocoder.bing( loc, key='AvTfZ0MIRpbOKdJcsRIy5mp-5g0fxHmZof_aYB7e0mTzHyhRh_SNBF6STx2SWPc4')
results = g.json
print(json.dumps(results, indent=4))
print(results['lat'], results['lng'])
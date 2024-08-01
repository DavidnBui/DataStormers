import sys
from utils import load_config, fetch_api_data

config = load_config('config.json')

weather_api_key = config.get('Visual Crossing', {}).get('key')
if not weather_api_key:
    print("Weather API key not found in the configuration file.")
    sys.exit()

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Peoria"
params = {
    "unitGroup": "metric",
    "key": weather_api_key,
    "contentType": "json"
}

data = fetch_api_data(url, params=params, method='GET')
print(data)

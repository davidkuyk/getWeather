#! python3

# getWeather.py - Prints the weather for a location using OpenWeatherMap.org's API.

import json, requests
import datetime

# once you create an account with openWeatherMap.org, get this API key from home.openweathermap.org/api_keys
APPID = 'yourAPIKey'

# Change these to the latitude and longitude for your current location
lat = 'yourLat'
lon = 'yourLong'

# Download JSON data from OpenWeatherMap.org's API. Pick an API from https://openweathermap.org/api and the docs will show you the API call url to include here.
url='https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&units=imperial&appid=%s' % (lat, lon,
APPID)
response = requests.get(url)
response.raise_for_status()
# Uncomment the next line to see the raw JSON text.
#print(response.text)

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

current_f = str(int(round(weatherData['current']['temp'])))
current_feels_like = str(int(round(weatherData['current']['feels_like'])))
description = weatherData['current']['weather'][0]['description']
high = str(int(round(weatherData['daily'][0]['temp']['max'])))
low = str(int(round(weatherData['daily'][0]['temp']['min'])))
pop = str(int(round(weatherData['daily'][0]['pop']))*100)
humid = str(int(round(weatherData['current']['humidity'])))
tom_high = str(int(round(weatherData['daily'][1]['temp']['max'])))
tom_low = str(int(round(weatherData['daily'][1]['temp']['min'])))
tom_pop = str(int(round(weatherData['daily'][1]['pop']))*100)
tom_humid = str(int(round(weatherData['daily'][1]['humidity'])))
tom_description = weatherData['daily'][1]['weather'][0]['description']
minute15 = weatherData['minutely'][15]['precipitation']
minute30 = weatherData['minutely'][30]['precipitation']
minute60 = weatherData['minutely'][60]['precipitation']
hour1t = datetime.datetime.fromtimestamp(weatherData['hourly'][1]['dt'])
hour2t = datetime.datetime.fromtimestamp(weatherData['hourly'][2]['dt'])
hour3t = datetime.datetime.fromtimestamp(weatherData['hourly'][3]['dt'])
hour4t = datetime.datetime.fromtimestamp(weatherData['hourly'][4]['dt'])
hour5t = datetime.datetime.fromtimestamp(weatherData['hourly'][5]['dt'])
hour6t = datetime.datetime.fromtimestamp(weatherData['hourly'][6]['dt'])
hour7t = datetime.datetime.fromtimestamp(weatherData['hourly'][7]['dt'])
hour8t = datetime.datetime.fromtimestamp(weatherData['hourly'][8]['dt'])
hour9t = datetime.datetime.fromtimestamp(weatherData['hourly'][9]['dt'])
hour10t = datetime.datetime.fromtimestamp(weatherData['hourly'][10]['dt'])
hour11t = datetime.datetime.fromtimestamp(weatherData['hourly'][11]['dt'])
hour12t = datetime.datetime.fromtimestamp(weatherData['hourly'][12]['dt'])
hour13t = datetime.datetime.fromtimestamp(weatherData['hourly'][13]['dt'])
hour14t = datetime.datetime.fromtimestamp(weatherData['hourly'][14]['dt'])
hour15t = datetime.datetime.fromtimestamp(weatherData['hourly'][15]['dt'])
hour16t = datetime.datetime.fromtimestamp(weatherData['hourly'][16]['dt'])
hour17t = datetime.datetime.fromtimestamp(weatherData['hourly'][17]['dt'])
hour18t = datetime.datetime.fromtimestamp(weatherData['hourly'][18]['dt'])
hour19t = datetime.datetime.fromtimestamp(weatherData['hourly'][19]['dt'])
hour20t = datetime.datetime.fromtimestamp(weatherData['hourly'][20]['dt'])
hour21t = datetime.datetime.fromtimestamp(weatherData['hourly'][21]['dt'])
hour22t = datetime.datetime.fromtimestamp(weatherData['hourly'][22]['dt'])
hour23t = datetime.datetime.fromtimestamp(weatherData['hourly'][23]['dt'])
hour24t = datetime.datetime.fromtimestamp(weatherData['hourly'][24]['dt'])
hour1w = weatherData['hourly'][1]['weather'][0]['description']
hour2w = weatherData['hourly'][2]['weather'][0]['description']
hour3w = weatherData['hourly'][3]['weather'][0]['description']
hour4w = weatherData['hourly'][4]['weather'][0]['description']
hour5w = weatherData['hourly'][5]['weather'][0]['description']
hour6w = weatherData['hourly'][6]['weather'][0]['description']
hour7w = weatherData['hourly'][7]['weather'][0]['description']
hour8w = weatherData['hourly'][8]['weather'][0]['description']
hour9w = weatherData['hourly'][9]['weather'][0]['description']
hour10w = weatherData['hourly'][10]['weather'][0]['description']
hour11w = weatherData['hourly'][11]['weather'][0]['description']
hour12w = weatherData['hourly'][12]['weather'][0]['description']
hour13w = weatherData['hourly'][13]['weather'][0]['description']
hour14w = weatherData['hourly'][14]['weather'][0]['description']
hour15w = weatherData['hourly'][15]['weather'][0]['description']
hour16w = weatherData['hourly'][16]['weather'][0]['description']
hour17w = weatherData['hourly'][17]['weather'][0]['description']
hour18w = weatherData['hourly'][18]['weather'][0]['description']
hour19w = weatherData['hourly'][19]['weather'][0]['description']
hour20w = weatherData['hourly'][20]['weather'][0]['description']
hour21w = weatherData['hourly'][21]['weather'][0]['description']
hour22w = weatherData['hourly'][22]['weather'][0]['description']
hour23w = weatherData['hourly'][23]['weather'][0]['description']
hour24w = weatherData['hourly'][24]['weather'][0]['description']

# Print weather descriptions to command line
weatherReport = f'''
TODAY:
15 minutes: {minute15} mm of precipitation
30 minutes: {minute30} mm of precipitation
1 hour: {minute60} mm of precipitation
current temp: {current_f} F
feels like: {current_feels_like} F
current humidity: {humid}%
high: {high} F
low: {low} F
precipitation: {pop}%
{description}

TOMORROW:
humidity: {tom_humid}%
high: {tom_high} F
low: {tom_low} F
precipitation: {tom_pop}%
{tom_description}

NEXT 24 HOURS:
{hour1t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour1w}
{hour2t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour2w}
{hour3t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour3w}
{hour4t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour4w}
{hour5t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour5w}
{hour6t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour6w}
{hour7t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour7w}
{hour8t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour8w}
{hour9t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour9w}
{hour10t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour10w}
{hour11t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour11w}
{hour12t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour12w}
{hour13t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour13w}
{hour14t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour14w}
{hour15t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour15w}
{hour16t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour16w}
{hour17t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour17w}
{hour18t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour18w}
{hour19t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour19w}
{hour20t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour20w}
{hour21t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour21w}
{hour22t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour22w}
{hour23t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour23w}
{hour24t.strftime('%I %p').lstrip("0").replace(" 0", " ")}: {hour24w}
'''
import json
import urllib.request
from device import Device

class WeatherStation(Device):
  def __init__(self, deviceName, HHMMSS):
    super().__init__(deviceName, HHMMSS, None)
    
    self.content =  """{
   "coord":{
      "lon":4.8897,
      "lat":52.374
   },
   "weather":[
      {
         "id":801,
         "main":"Clouds",
         "description":"few clouds",
         "icon":"02n"
      }
   ],
   "base":"stations",
   "main":{
      "temp":9.29,
      "feels_like":8.55,
      "temp_min":7.18,
      "temp_max":11.94,
      "pressure":1024,
      "humidity":82
   },
   "visibility":10000,
   "wind":{
      "speed":1.79,
      "deg":320,
      "gust":3.13
   },
   "clouds":{
      "all":20
   },
   "dt":1634066325,
   "sys":{
      "type":2,
      "id":2011826,
      "country":"NL",
      "sunrise":1634018420,
      "sunset":1634057589
   },
   "timezone":7200,
   "id":2759794,
   "name":"Amsterdam",
   "cod":200
}"""

  def getRDF(self):
    DEBUG = True
    if DEBUG:
      weatherMeasurements = json.loads(self.content)
    else:
      url = """http://api.openweathermap.org/data/2.5/weather?units=metric&q=Amsterdam,nl&APPID=d04692b59314f535e129e2acd8bdd"""
      req = urllib.request.Request(url)
      with urllib.request.urlopen(req) as response:
        weatherMeasurements = json.loads(response.read().decode('utf-8'))

    SUNRISE = weatherMeasurements['sys']['sunrise']
    SUNSET = weatherMeasurements['sys']['sunset']
    TEMP = weatherMeasurements['main']['temp']
    WEATHER = "Clear"

    return f"""ex:WS1 rdf:type smart:SmartWeatherStation ;
       saref:hasTimestamp "2020-12-02T14:30:00"^^xsd:dateTime  ;
       smart:hasUnixTimestamp "1606919400"^^xsd:integer  ;
       smart:hasSunriseTime {SUNRISE} ;
       smart:hasSunsetTime {SUNSET} ;
       smart:hasTemperature {TEMP} ;
       smart:hasWeatherCondition smart:WeatherCondition{WEATHER} ;
."""

__author__ = 'smorris'

#!/usr/bin/python

# Imports
import json
import urllib2

# Constants
json_weather = 'http://api.openweathermap.org/data/2.5/weather?q='
city = 'okotoks,ca'
home = '/home/you'
weather_file = '.bashweather'

def get_data(site):
    site_data = urllib2.urlopen(site)
    return site_data

def get_json_data(raw_json, item_name):
    formatted_json = json.load(raw_json)
    return formatted_json[item_name]

def write_config(write_item, config_location):
    try:
        write_file = open(config_location + '.bashweather', 'w')
        write_file.write(write_item)
        write_file.close()
        return True
    except:
        print "Error in accessing the configuration file. Please check the file location setting..."
        return False

if __name__ == "__main__":
    raw_weather = get_data(json_weather + city)
    main_section = get_json_data(raw_weather, 'weather')
    raw_weather = get_data(json_weather + city)
    other_section = get_json_data(raw_weather, 'main')
    weather_data = str(main_section[0]['main']) + " " + str(round(float(other_section['temp']) - 272.15, 1)) + "C"
    write_config(weather_data, home)

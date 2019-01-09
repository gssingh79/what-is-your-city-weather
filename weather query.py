# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
city_address = "http://api.openweathermap.org/data/2.5/weather?appid=ce4b6aeeab26d8c8891e9311b6ae4c29&q={}"
city_name = input("enter city name:")
url = city_address.format(city_name)
data = requests.get(url).json()
detail = input("choose: 'id' or 'main' or 'description' or 'icon':")
formatted_data = data['weather'][0][detail]
print("weather of city",city_name,"is",formatted_data) 
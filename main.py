#Please scroll to bottom for:
# a) how to set up API key.
# b) how I am using the API.
# c) info on imported packages.

import requests
import math
import random

#(TEST- BARBADOS!)
#LONGITUDE) -59.543198
#LATITUDE) 13.193887

#(TEST - DONCASTER!)
#LONGITUDE) -1.128462
#LATITUDE) 53.522820

#USER INPUT
longitude = input("Please input your longitude for precise weather prediction (Geocode E.g. -1.128462): ")
latitude = input("Please input your latitude for a precise weather prediction (Geocode E.g. 53.522820): ")

#API REQUEST
API_key = "c584cb3af22d80d155415746dbc4e49a"
response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&cnt=8&appid={API_key}&units=metric")
weather = response.json()

#LOCATION
print()
location = f"Please see weather data for {weather['city']['name']}" + f", {weather['city']['country']}"
print(location)
print("________________________________________________________________________")

#TEMPERATURES
temp_list = []
for conditions in response.json()["list"]:
     temp_list.append(conditions["main"]["temp"])
#MAX TEMP
maximum = math.floor(max(temp_list))
#MEAN TEMP
a = sum(temp_list)
b = len(temp_list)
def mean(a,b):
     return a / b        #RETURN

result = (int(mean(a,b)))
print(f"The mean temperature today is approximately: {result}{chr(176)}c\n")


print(f"The maximum temperature today is approximately: {maximum}{chr(176)}c\n")

print(f"Accurate temperature({chr(176)}c) from nearest hour then every three hours:")

print(temp_list)
print("________________________________________________________________________")

#OUTFIT GENERATOR
def present_outfit():    #IF ELIF ELSE
          if maximum >= 20:
                         print(f"       It is hot today - why not try this outfit?")
          elif maximum >= 10 and maximum <=19:
                         print("        It is temperate today - why not try this outfit?")
          else:
                         print("        It is cold today - why not try this outfit?")

#OUTFIT - COLD WEATHER
c_top = ["Heavy sports jacket", "Woolen coat", "Gilet"]
c_inner = ["Thick jumper", "Thermal top", "long-sleeved shirt", "cardigan"]
c_bottom = ["Thick trousers", "Heavy Jeans", "Thermal joggers"]
#OUTFIT - TEMPERATE WEATHER
t_top = ["Light jumper", "Cardigan", "Hoodie"]
t_inner = ["T-shirt", "Vest", "Short-sleeved shirt"]
t_bottom = ["Jeans", "Light trousers/skirt"]
#OUTFIT - HOT WEATHER
h_top = ("Jumpers or overcoats not needed today")
h_inner = ["T-shirt", "Vest", "Short-sleeved shirt"]
h_bottom = ["Shorts", "Light linen trousers/skirt", "Cropped trousers"]

present_outfit()

#RANDOM (RANDOM.CHOICE) PACKAGE
def cold_outfit():
     if maximum <=10:
        print(f"                   COLD WEATHER OUTFIT \nTop - {random.choice(c_top)}\nInner - {random.choice(c_inner)}\nBottom - {random.choice(c_bottom)}")

cold_outfit()

def temperate_outfit():
     if maximum <= 19 and maximum >=11:
          print(f"                 TEMPERATE WEATHER OUTFIT \nTop - {random.choice(t_top)}\nInner - {random.choice(t_inner)}\nBottom - {random.choice(t_bottom)}")

temperate_outfit()

def hot_outfit():
     if maximum >= 20:
          print(f"                 HOT WEATHER OUTFIT \nTop - {h_top}\nInner - {random.choice(h_inner)}\nBottom - {random.choice(h_bottom)}")

hot_outfit()
print("________________________________________________________________________")

#RAIN CHECK
def desc_conditions(): #USED STRING SLICING TO GET JUST TIME RATHER THAN YEAR,MONTH,DAY
     is_raining = input("Would you like to check for rain? y/n ")

     if is_raining == 'y':
          print(f"{weather['list'][0]['weather'][0]['description']}" + (f" at:{weather['list'][0]['dt_txt'][10:-3]} hours\n"))

          print(f"{weather['list'][1]['weather'][0]['description']}" + (f" at:{weather['list'][1]['dt_txt'][10:-3]} hours\n"))

          print(f"{weather['list'][2]['weather'][0]['description']}" + (f" at:{weather['list'][2]['dt_txt'][10:-3]} hours\n"))

          print(f"{weather['list'][3]['weather'][0]['description']}" + (f" at:{weather['list'][3]['dt_txt'][10:-3]} hours\n"))

          print(f"{weather['list'][4]['weather'][0]['description']}" + (f" at:{weather['list'][4]['dt_txt'][10:-3]} hours\n"))

          print(f"{weather['list'][5]['weather'][0]['description']}" + (f" at:{weather['list'][5]['dt_txt'][10:-3]} hours\n"))

          print(f"{weather['list'][6]['weather'][0]['description']}" + (f" at:{weather['list'][6]['dt_txt'][10:-3]} hours\n"))

          print(f"{weather['list'][7]['weather'][0]['description']}" + (f" at:{weather['list'][7]['dt_txt'][10:-3]} hours\n"))

          conditions_1 = (f"{weather['list'][0]['weather'][0]['description']}")
          conditions_2 = (f"{weather['list'][1]['weather'][0]['description']}")
          conditions_3 = (f"{weather['list'][2]['weather'][0]['description']}")
          conditions_4 = (f"{weather['list'][3]['weather'][0]['description']}")
          conditions_5 = (f"{weather['list'][4]['weather'][0]['description']}")
          conditions_6 = (f"{weather['list'][5]['weather'][0]['description']}")
          conditions_7 = (f"{weather['list'][6]['weather'][0]['description']}")
          conditions_8 = (f"{weather['list'][7]['weather'][0]['description']}")


          todays_conditions = conditions_1, conditions_2, conditions_3, conditions_4, conditions_5, conditions_6, conditions_7, conditions_8

          if todays_conditions == "light rain" or "rain":
               print("It may rain today! Consider using waterproofs!")

          else:
               print("There is no rain today - enjoy your day!")
     else:
          return (print("Enjoy your day!"))       #RETURN

desc_conditions()

#WRITE TO TEXT FILE
weather_data = response.json()

with open('weatherdata.txt', 'w') as text_file:
    text_file.write((location) + "\n" + "\n")
with open('weatherdata.txt', 'a') as text_file:
    for results in weather_data['list']:
        text_file.write(results['weather'][0]['description'] + " (+3h)" + "\n")
with open('weatherdata.txt', 'a') as text_file:
    text_file.write("\nTODAY'S MEAN TEMPERATURE \n")
with open('weatherdata.txt', 'a') as text_file:
    text_file.write (str(mean(a,b)))
with open('weatherdata.txt', 'a') as text_file:
    text_file.write("\nTODAY'S MAX TEMPERATURE \n")
with open ('weatherdata.txt', 'a') as text_file:
    text_file.write(str(maximum))

#a) How to set up API key - as you can see in the url at the top for Openweather there are curley braces refering to my API key.
    #When using OpenWeather they provide the user with a unique API key which helps monitor users of the API data.
    #You can then copy this API key into the curley braces in the url - this allows you to access JSON data from the site.

#b) How I am using this API - I am taking the latitudinal and longitudinal data provided by the user in order to generate
    #information on weather data including max & mean temperatures and chance of rain. I then use this data
    #in order to generate the user ideas of what to wear that day. Even though this is a 5 days forcast providing data
    #every 3 hours, I have restricted the number of time stamps to 8 using the url ('&cnt=8') which means I will only recieve
    #24 hours worth of information.

#c) Imported packages - import requests in order to obtain the JSON data from the API (requests.get)
#                     - import math in order to use math.floor to simplify max temp data: from decimal to integer.
#                     - import random to randomly generate an outfit (random.choice) based on clothing items added to relevant temperature list.
# I always import/install packages by entering the title of the package, waiting for the red lightbulb prompt immediately next
# to the import and click install. You can also check whether they're installed by checking 'python packages', its icon is
#next to console.
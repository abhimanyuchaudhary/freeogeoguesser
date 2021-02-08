#!/usr/bin/python

import sys
import requests, random
# 3.043108, 101.621052
x1 = int(sys.argv[1]);
x2 = int(sys.argv[2]);
y1 = int(sys.argv[3]);
y2 = int(sys.argv[4]);
country =str(sys.argv[5]);

randomX = random.uniform(x1, x2)
randomY = random.uniform(y1, y2)
randomX = 3.043108
randomY = 101.621052
googleApiKey = "AIzaSyDMEIMOMiplkCFiyXazvI5gV-sRXRLfrVo"
streetApiCall = "https://maps.googleapis.com/maps/api/streetview?size=400x400&location="+ str(randomX) +","+ str(randomY) +"&key="+googleApiKey
print(streetApiCall)
response = requests.get(streetApiCall)
print(response.json)
print(response.text)

# x = 3.043108
# y = 101.621052
# country = 'Malaysia'
# query = {'lat':x, 'lon':y, 'country':country}
# response = requests.post('http://localhost:3000/putLocation/'+str(x)+'/'+str(y)+'/'+str(country))
# print(response.text)
# print(response.json)


# print(length1, length2, country)
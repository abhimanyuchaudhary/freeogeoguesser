#!/usr/bin/python
import json
import sys
import requests, random
from bs4 import BeautifulSoup
# 3.043108, 101.621052
from PIL import Image 
  
def doesStreetViewExist(randomX, randomY, key):
	streetApiCall = "https://maps.googleapis.com/maps/api/streetview/metadata?size=400x400&location="+ str(randomX) +","+ str(randomY) +"&key="+googleApiKey+"&format=text"
	print(streetApiCall)
	response = requests.get(streetApiCall)
	print(response.json()["status"])
	return (response.json()["status"] == "OK")
	# Read image 
	# img = Image.open(response.text, "JPEG") 
	  
	# # Output Images 
	# img.show() 
	  
	# print(response.headers)

x1 = int(sys.argv[1]);
x2 = int(sys.argv[2]);
y1 = int(sys.argv[3]);
y2 = int(sys.argv[4]);
country =str(sys.argv[5]);

randomX = random.uniform(x1, x2)
randomY = random.uniform(y1, y2)
randomX =  28.509309 #3.043108
randomY =  77.143120 #101.621052
randomX =  3.043108
randomY =  101.621052
googleApiKey = "AIzaSyAorC8wLyYrEJNkSQPOV7PJ83FJj6wHe9M"
print(doesStreetViewExist(randomX, randomY, googleApiKey))

# getResponse(randomX, randomY, googleApiKey)
# print(response.json())
# res = json.loads(response.json())
# print(response)

# x = 3.043108
# y = 101.621052
# country = 'Malaysia'
# query = {'lat':x, 'lon':y, 'country':country}
# response = requests.post('http://localhost:3000/putLocation/'+str(x)+'/'+str(y)+'/'+str(country))
# print(response.text)
# print(response.json)


# print(length1, length2, country)
!/usr/bin/python
import json
import sys
import requests, random
from bs4 import BeautifulSoup
# 3.043108, 101.621052
from PIL import Image 
# [
#     {
#         "_id": "601cf60bca1d4a4490afa944",
#         "lat": 42.345573,
#         "lon": -71.098326,
#         "country": "USA",
#         "__v": 0
#     },
#     {
#         "_id": "601cf62fca1d4a4490afa945",
#         "lat": 52.163564,
#         "lon": 21.084532,
#         "country": "Poland",
#         "__v": 0
#     },
#     {
#         "_id": "601cf65fca1d4a4490afa946",
#         "lat": 46.75711,
#         "lon": 7.624709,
#         "country": "Switzerland",
#         "__v": 0
#     },
#     {
#         "_id": "601cf8b5ca1d4a4490afa947",
#         "lat": 48.824507,
#         "lon": 2.325784,
#         "country": "France",
#         "__v": 0
#     },
#     {
#         "_id": "601cf8f2ca1d4a4490afa948",
#         "lat": 43.088865,
#         "lon": 12.438406,
#         "country": "Italy",
#         "__v": 0
#     },
# ]


def doesStreetViewExist(randomX, randomY, key):
	streetApiCall = "https://maps.googleapis.com/maps/api/streetview/metadata?size=400x400&location="+ str(randomX) +","+ str(randomY) +"&key="+googleApiKey+"&format=text"
	response = requests.get(streetApiCall)
	print(response)
	return (response.json()["status"] == "OK")
def sendToDb(x, y, country):
	query = {'lat':x, 'lon':y, 'country':country}
	response = requests.post('http://localhost:3000/putLocation', data = query)



x1 = float(sys.argv[1]);
x2 = float(sys.argv[2]);
# y1 = float(sys.argv[3]);
# y2 = float(sys.argv[4]);
country =str(sys.argv[3]);

sendToDb(x1, x2, country)



class entity(id){
	String id = id;
}

class Comment(id, parentId, text){
	String id = id;
	Time t = System.currentTime;
	String parentId = parentId
	String content = text
}

E = entity(id)

c1 = new comment(uniqueId_1, E.id, "asdf")
c2 = new comment(uniqueId_2, E.id, "asdf")

c11 = new comment(uniqueId_11, c1.id, "test")

commenttable = <id , t, parentId, text>

E

listCommentsID = select id from commenttable where parentId = E.id

render(Comment c):
	print(c.content)
	listCommentsID = select id from commenttable where parentId = c.id
	for i in listCommentsID:
		render(i)



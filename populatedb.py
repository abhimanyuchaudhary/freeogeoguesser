#!/usr/bin/python




class comments:
	content = ""
	comment_id = 0
	parent_id = 0
	def __init__(self, comment_id, parent_id, content):
		self.comment_id = comment_id;
		self.parent_id = parent_id
		self.content = content
	def display(self):
		return self.content;

class entity:
	entity_id = -1;
	def __init__(self, entity_id):
		self.entity_id = entity_id;

commentList = []

def addCommentToEntity(parentId, text):
	currId = len(commentList)
	commentList.append(comments(len(commentList), parentId, text))
	return currId

def displayCommentsForEntity(e):
	print(e.entity_id)
	for comment in commentList:
		if(comment.parent_id == e.entity_id):
			displayCommentsForComments(comment)

def displayCommentsForComments(c):
	print(c.content)
	for subcomment in commentList:
		if(subcomment.parent_id == c.comment_id):
			displayCommentsForComments(subcomment);

if __name__ == "__main__":
	e = entity(100)
	id1 = addCommentToEntity(100, "hi");
	id2 = addCommentToEntity(100, "bye");
	id1_1 = addCommentToEntity(id1, "hi_child_1")
	id1_2 = addCommentToEntity(id1, "hi_child_2")
	id2_1 = addCommentToEntity(id2, "bye_child")
	id1_1_1 = addCommentToEntity(id1_1, "smallestComment")
	displayCommentsForEntity(e)

# import json
# import sys
# import requests, random
# from bs4 import BeautifulSoup
# # 3.043108, 101.621052
# from PIL import Image 
# # [
# #     {
# #         "_id": "601cf60bca1d4a4490afa944",
# #         "lat": 42.345573,
# #         "lon": -71.098326,
# #         "country": "USA",
# #         "__v": 0
# #     },
# #     {
# #         "_id": "601cf62fca1d4a4490afa945",
# #         "lat": 52.163564,
# #         "lon": 21.084532,
# #         "country": "Poland",
# #         "__v": 0
# #     },
# #     {
# #         "_id": "601cf65fca1d4a4490afa946",
# #         "lat": 46.75711,
# #         "lon": 7.624709,
# #         "country": "Switzerland",
# #         "__v": 0
# #     },
# #     {
# #         "_id": "601cf8b5ca1d4a4490afa947",
# #         "lat": 48.824507,
# #         "lon": 2.325784,
# #         "country": "France",
# #         "__v": 0
# #     },
# #     {
# #         "_id": "601cf8f2ca1d4a4490afa948",
# #         "lat": 43.088865,
# #         "lon": 12.438406,
# #         "country": "Italy",
# #         "__v": 0
# #     },
# # ]


# def doesStreetViewExist(randomX, randomY, key):
# 	streetApiCall = "https://maps.googleapis.com/maps/api/streetview/metadata?size=400x400&location="+ str(randomX) +","+ str(randomY) +"&key="+googleApiKey+"&format=text"
# 	response = requests.get(streetApiCall)
# 	print(response)
# 	return (response.json()["status"] == "OK")
# def sendToDb(x, y, country):
# 	query = {'lat':x, 'lon':y, 'country':country}
# 	response = requests.post('http://localhost:3000/putLocation', data = query)



# x1 = float(sys.argv[1]);
# x2 = float(sys.argv[2]);
# # y1 = float(sys.argv[3]);
# # y2 = float(sys.argv[4]);
# country =str(sys.argv[3]);

# sendToDb(x1, x2, country)

# # if(x1>x2):
# # 	x1,x2 = x2,x1
# # if(y1>y2):
# # 	y1,y2 = y2,y1

# # i = 0;
# # while(i<10):
# # 	randomX = random.uniform(x1, x2)
# # 	randomY = random.uniform(y1, y2)
# # 	googleApiKey = "AIzaSyAorC8wLyYrEJNkSQPOV7PJ83FJj6wHe9M"
# # 	if(doesStreetViewExist(randomX, randomY, googleApiKey)):
# # 		i += 1
# # 		print("done: " + str(i))
# # 		sendToDb(randomX, randomY, country)

# # comments service, add comments to any entity, can have nested comments



# class entity(id){
# 	String id = id;
# }

# class Comment(id, parentId, text){
# 	String id = id;
# 	Time t = System.currentTime;
# 	String parentId = parentId
# 	String content = text
# }

# E = entity(id)

# c1 = new comment(uniqueId_1, E.id, "asdf")
# c2 = new comment(uniqueId_2, E.id, "asdf")

# c11 = new comment(uniqueId_11, c1.id, "test")

# commenttable = <id , t, parentId, text>

# E

# listCommentsID = select id from commenttable where parentId = E.id

# render(Comment c):
# 	print(c.content)
# 	listCommentsID = select id from commenttable where parentId = c.id
# 	for i in listCommentsID:
# 		render(i)



# Ibnul Jahan and Jawadul Kadir
# SoftDev2 pd7
# K04 -- Mi only nyam ital food, mon!
# 2018-02-14  

from pymongo import MongoClient

#connects to server
c = MongoClient('lisa.stuy.edu', 27017)
#switches to test database
mfDB = c.test
#access restaurants collection
collie = mfDB.restaurants

#finds restaurants by borough
def find_by_borough(borough):
	results = collie.find({"borough" : borough})
	print("Restaurants in " + borough + ":")
	for restaurant in results:
		print("\t" + str(restaurant))

#finds restaurants by zip code
def find_by_zip_code(zip_code):
	results = collie.find({"address.zipcode" : zip_code})
	print("Restaurants with zip code " + zip_code + ":")
	for restaurant in results:
		print("\t" + str(restaurant))

#finds restaurants by zip code and grade
def find_by_zip_code_and_grade(zip_code, grade):
	results = collie.find({"$and" : [{"address.zipcode" : zip_code}, {"grades.grade" : grade}]})
	print("Restaurants with zip code " + zip_code + "and grade" + grade + ":")
	for restaurant in results:
		print("\t" + str(restaurant))

#finds restaurants by zip code and with a score below a threshold
def find_by_zip_code_and_score_threshold(zip_code, score):
	results = collie.find({"$and" : [{"address.zipcode" : zip_code}, {"grades.score" : {"$lt" : score}}]})
	print("Restaurants with zip code " + zip_code + "and score below" + str(score) + ":")
	for restaurant in results:
		print("\t" + str(restaurant))

#finds restaurants by building number and type of cuisine
def find_by_building_and_cusine(building, cuisine):
	results = collie.find({"$and" : [{"address.building" : building}, {"cuisine" : cuisine}]})
	print("Restaurants in building " + building + "and " + cuisine + "cuisine:")
	for restaurant in results:
		print("\t" + str(restaurant))

find_by_borough("Manhattan")
find_by_zip_code("10282")
find_by_zip_code_and_grade("10282", "A")
find_by_zip_code_and_score_threshold("10282", 10)
find_by_building_and_cusine("102", "American")


'''Ibnul Jahan
SoftDev1 pd7
HW13 -- A RESTful Journey Skyward
2017-11-08



import urllib2
from flask import Flask, render_template, request, session, redirect, url_for
import json


"""api_key = "1I3RG0HH1aH67s0fi9nWhhc5oudr3UvzxprRK35f"
data_file = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key="+ api_key)
info = data_file.read()
data = json.loads(info)
img= data['hdurl']
explanation= data['explanation']
"""



app = Flask(__name__) #create instance of class 

#assign following fxn to run when
#root route requested

@app.route("/")
def hello():
    data_file = urllib2.urlopen("http://jservice.io/api/random")
    info = data_file.read()
    data = json.loads(info)
    question= data[0]['question']
    answer= data[0]['answer']
    category = data[0]['category']['title']
    return render_template("temp.html", title = "Jeopardy", category = category, question = question, answer = answer)


if __name__=="__main__":
    app.debug = True
app.run()
'''

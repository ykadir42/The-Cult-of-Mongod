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
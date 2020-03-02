import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
acidDatabase = client["acid_storage"]#acid Storage is the database name
mycol = acidDatabase["storages_data"] #storage data is the collection name i.e. Table name

def retriveDataAndPlot():
	A = [] , T = []
	for x in mycol.find({},{ "_id": 0, "A": 1, "T": 1, "G":1,"C":1}):
			print(x)
			#x is a dict having {'A': 144, 'T': 143, 'G': 148, 'C': 132}
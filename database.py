import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
acidDatabase = client["acid_storage"]#acid Storage is the database name
mycol = acidDatabase["storages_data"] #storage data is the collection name i.e. Table name

def pushToDatabase(ACID_LABEL,sequence, Acid, A,T,G,C):
	mycol.insert_one({'LABEL':ACID_LABEL,'SEQUENCE': sequence,'CORR_ACID': Acid, 'A': A,'T':T,'G':G,'C':C})
def retrieveDatabase():
	for x in mycol.find({},{ "_id": 0, "A": 1, "T": 1, "G":1,"C":1}):
		print(x)
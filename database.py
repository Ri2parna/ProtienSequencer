import pymongo
import matplotlib.pyplot as plt
client = pymongo.MongoClient("mongodb://localhost:27017/")
acidDatabase = client["acid_storage"]  # acid Storage is the database name
# storage data is the collection name i.e. Table name
mycol = acidDatabase["storages_data"]


def plot(sequenceCount):
    """funct to plot the given data in a graph"""
    list_ = [x for x in sequenceCount.keys()]
    key = [y for y in sequenceCount.values()]
    plt.bar(sequenceCount.keys(), sequenceCount.values(), 1, color='g')
    plt.show()
    print(list_, key)


def pushToDatabase(ACID_LABEL, sequence, Acid, A, T, G, C):
    mycol.insert_one({'LABEL': ACID_LABEL, 'SEQUENCE': sequence,
                      'CORR_ACID': Acid, 'A': A, 'T': T, 'G': G, 'C': C})


def retrieveDatabase():
    sequenceCount = {
        'A': 0,
        'T': 0,
        'G': 0,
        'C': 0
    }
    for sequenceDictionary in mycol.find({}, {"_id": 0, "A": 1, "T": 1, "G": 1, "C": 1}):
        for item in sequenceDictionary:
            sequenceCount[item] += sequenceDictionary[item]
    print('Sequence Count is : ', sequenceCount)
    return (sequenceCount)

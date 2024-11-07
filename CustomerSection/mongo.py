from pymongo import MongoClient


MONGO_URL = 'mongodb://localhost:27017/'
DATA_BASE_NAME = 'feedback_db'
CLUSTER_NAME = 'feedback'
ANALISE_CLUSTER = 'feedback_analysis'


client = MongoClient(MONGO_URL)  # Adjust the URI if needed
db = client[DATA_BASE_NAME]  # Use your MongoDB database name here
collection1 = db[CLUSTER_NAME]
collection2 = db[ANALISE_CLUSTER]


# write feedback
def insert_feedback(feedback_data):
    result = collection1.insert_one(feedback_data)
    return result.inserted_id


# Read all feedback
def get_all_feedback(filter=None):
    if filter:
        feedback_list = list(collection1.find({'username':filter}))
        return feedback_list
    feedback_list = list(collection1.find({}))  # Retrieve all feedback data
    return feedback_list


def delete_analysis():
    first_document = collection2.find_one()
    if first_document:
        collection2.delete_one({"_id": first_document["_id"]})  # Delete by unique _id
        print("First document deleted:", first_document)
    else:
        print("No documents to delete.")


def get_analysis():
    first_document = collection2.find_one()
    return first_document


def insert_analysis(analysis_data):
    collection2.insert_one(analysis_data)


def modify_analysis(analysis_data):
    doc = get_analysis()
    if not doc:
        insert_analysis(analysis_data)
    else:
        filter_query = {'_id': doc['_id']}
        collection2.update_one(filter_query, {"$set": analysis_data})

from pymongo import MongoClient


MONGO_URL = 'mongodb://db:27017/'
DATA_BASE_NAME = 'feedback_db'
CLUSTER_NAME = 'feedback'


client = MongoClient(MONGO_URL)  # Adjust the URI if needed
db = client[DATA_BASE_NAME]  # Use your MongoDB database name here
collection = db[CLUSTER_NAME]


# write feedback
def insert_feedback(feedback_data):
    result = collection.insert_one(feedback_data)
    return result.inserted_id


# Read all feedback
def get_all_feedback(filter=None):
    if filter:
        feedback_list = list(collection.find({'username':filter}))
        return feedback_list
    feedback_list = list(collection.find({}))  # Retrieve all feedback data
    return feedback_list
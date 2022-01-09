import pandas as pd
from pymongo import MongoClient
import json

def mongoimport(csv_path, db_name, coll_name, db_url='mongodb+srv://root:R0ld3x0p@cluster0.9f7ty.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'):
    client = MongoClient(db_url)
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert_many(payload)
    return coll.count()


print(mongoimport('binnnu.txt','jocasta', 'bins'))
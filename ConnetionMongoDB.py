import pandas as pd
from pymongo import MongoClient

def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        return data.to_dict(orient='records')
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def upload_csv_to_mongodb(collection, data):
    if data:
        result = collection.insert_many(data)
        print(f"Inserted {len(result.inserted_ids)} documents into MongoDB")
    else:
        print("No data to insert")

def main():
    csv_file_path = "productData.csv"
    MONGODB_URI = "mongodb+srv://"server":"password"@nhan.uxnpv.mongodb.net/"
    DB_NAME = "test"
    COLLECTION_NAME = "products"

    csv_data = read_csv_file(csv_file_path)
    collection = connect_to_mongodb(MONGODB_URI, DB_NAME, COLLECTION_NAME)
    upload_csv_to_mongodb(collection, csv_data)

if __name__ == "__main__":
    main()


import os
from dotenv import load_dotenv
import pymongo
import certifi
import gridfs

load_dotenv()

MONGO_DB_URL = os.getenv("mongoURI")
ca = certifi.where()

class ZipDataHandler:
    def __init__(self):
        try:
            # Establish MongoDB client and GridFS
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.fs = gridfs.GridFS(self.mongo_client["ConcerMLOps"])  # Use the specified database
        except Exception as e:
            raise e

    def insert_zip_to_mongodb(self, zip_file_path):
        try:
            # Read the .zip file in binary mode
            with open(zip_file_path, "rb") as file:
                file_data = file.read()
                # Store the file in GridFS
                file_id = self.fs.put(file_data, filename=os.path.basename(zip_file_path))
            print(f"File '{zip_file_path}' inserted with file_id: {file_id}")
            return file_id
        except Exception as e:
            raise e

if __name__ == '__main__':
    ZIP_FILE_PATH = "artifacts/data_zip/cancer-dataset.zip"
    
    zip_handler = ZipDataHandler()
    file_id = zip_handler.insert_zip_to_mongodb(ZIP_FILE_PATH)

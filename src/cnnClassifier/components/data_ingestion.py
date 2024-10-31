import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.config.config_entity import DataIngestionConfig
from pymongo import MongoClient
import certifi
import gridfs
from bson import ObjectId

class DataIngestion:
    def __init__(self, mongoURL, fileID, config: DataIngestionConfig):
        self.config = config
        self.mongoURL = mongoURL
        self.fileID = fileID
        self.mongo_client = MongoClient(mongoURL, tlsCAFile=certifi.where())
        self.fs = gridfs.GridFS(self.mongo_client["CancerMLOps"])  # Specify the database with GridFS
    
    def download_file_from_mongo(self) -> str:
        try:
            # Retrieve file from MongoDB GridFS by file_id
            file_data = self.fs.get(ObjectId('6723d6f00bf47e26638ce25b')).read()
            with open(self.config.local_data_file, "wb") as file:
                file.write(file_data)
            
            logger.info(f"File retrieved from MongoDB and saved to {self.config.local_data_file}")
            return self.config.local_data_file
        except Exception as e:
            raise e

        except Exception as e:
            raise e
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted {self.config.local_data_file} to {unzip_path}")
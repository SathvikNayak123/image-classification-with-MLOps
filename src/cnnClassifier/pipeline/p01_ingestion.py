from cnnClassifier.config.config_entity import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
import os
from dotenv import load_dotenv
load_dotenv()

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(os.getenv("mongoURI"),
                                       os.getenv("fileID"),
                                       config=data_ingestion_config)
        data_ingestion.download_file_from_mongo()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f"\n>>>>>> Data Ingestion started <<<<<<\n")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"\n>>>>>> Data Ingestion completed <<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e